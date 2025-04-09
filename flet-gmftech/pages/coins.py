#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# coins.py
# @Author : Gustavo (gustavo@gmf-tech.com)

import flet as ft
import base64
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.globals import ThemeType
from theme import COLORS, get_shadow

try:
    import pyodide
    from pyodide.http import pyfetch

    IS_PYODIDE = True
except ImportError:
    IS_PYODIDE = False
    import httpx

from datetime import datetime
import asyncio

# Cache global para os dados
_cached_data = None
_last_update = None
_is_fetching = False

# Função assíncrona para buscar os dados da API
async def fetch_usd_brl_data(force_refresh=False):
    global _cached_data, _last_update, _is_fetching
    
    # Se já estiver buscando dados, aguarda
    while _is_fetching:
        await asyncio.sleep(0.1)
    
    # Verifica se tem cache válido (menos de 5 minutos)
    now = datetime.now()
    if not force_refresh and _cached_data and _last_update:
        delta = now - _last_update
        if delta.total_seconds() < 300:  # 5 minutos
            return _cached_data

    _is_fetching = True
    try:
        url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15"
        max_retries = 3
        retry_count = 0

        while retry_count < max_retries:
            try:
                if IS_PYODIDE:
                    response = await pyfetch(url, method="GET")
                    if response.status == 200:
                        data = await response.json()
                        _cached_data = data
                        _last_update = now
                        return data
                else:
                    async with httpx.AsyncClient() as client:
                        response = await client.get(url)
                        if response.status_code == 200:
                            data = response.json()
                            _cached_data = data
                            _last_update = now
                            return data
                
                retry_count += 1
                if retry_count < max_retries:
                    await asyncio.sleep(1)
            except Exception as e:
                print(f"Tentativa {retry_count + 1} falhou: {str(e)}")
                retry_count += 1
                if retry_count < max_retries:
                    await asyncio.sleep(1)
        
        # Se chegou aqui, todas as tentativas falharam
        # Retorna cache antigo se disponível, mesmo que expirado
        return _cached_data if _cached_data else []
    finally:
        _is_fetching = False

# Iniciar o pré-carregamento dos dados
async def preload_data():
    await fetch_usd_brl_data()

# Função para criar o gráfico com Pyecharts
def create_chart(data):
    if not data:
        return None
        
    dates = [
        datetime.fromtimestamp(int(entry["timestamp"])).strftime("%d/%m")
        for entry in data[::-1]
    ]
    highs = [float(entry["high"]) for entry in data[::-1]]
    lows = [float(entry["low"]) for entry in data[::-1]]
    pct_changes = [float(entry["pctChange"]) for entry in data[::-1]]

    bar = (
        Bar(
            init_opts=opts.InitOpts(
                width="100%",
                height="400px",
                theme=ThemeType.LIGHT,
                animation_opts=opts.AnimationOpts(animation=False),  # Desativa animações
                js_host="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/",  # Usa CDN em vez de embutir
            )
        )
        .add_xaxis(dates)
        .add_yaxis(
            "Mínima (BRL)",
            lows,
            color=COLORS["error"],
            bar_width="40%",
            category_gap="20%",
            itemstyle_opts=opts.ItemStyleOpts(opacity=0.7),
        )
        .add_yaxis(
            "Máxima (BRL)",
            highs,
            color=COLORS["accent"],
            bar_width="40%",
            category_gap="20%",
            itemstyle_opts=opts.ItemStyleOpts(opacity=0.7),
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="Variação (%)",
                position="right",
                axislabel_opts=opts.LabelOpts(formatter="{value}%"),
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Cotação USD/BRL - Últimos 15 Dias"),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
            legend_opts=opts.LegendOpts(pos_top="5%"),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
    )

    line = (
        Line()
        .add_xaxis(dates)
        .add_yaxis(
            "Variação (%)",
            pct_changes,
            yaxis_index=1,
            color=COLORS["success"],
            linestyle_opts=opts.LineStyleOpts(width=4, opacity=1),
            label_opts=opts.LabelOpts(is_show=False),
            z_level=1,
        )
    )

    bar.overlap(line)
    html = bar.render_embed()
    return base64.b64encode(html.encode("utf-8")).decode("utf-8")

# Função assíncrona para carregar o gráfico
async def load_chart(page, chart_container):
    try:
        # Exibir mensagem de carregamento
        progress_ring = ft.ProgressRing(
            width=32, height=32, stroke_width=4, color=COLORS["primary"]
        )
        chart_container.content = ft.Column(
            [
                ft.Text("Carregando dados...", color=COLORS["text_secondary"], font_family="Roboto"),
                progress_ring,
            ],
            alignment="center",
            horizontal_alignment="center",
        )
        page.update()

        # Buscar os dados (usa cache se disponível)
        data = await fetch_usd_brl_data()
        if not data:
            chart_container.content = ft.Column(
                [
                    ft.Text(
                        "Erro ao carregar dados",
                        color=COLORS["error"],
                        size=16,
                        font_family="Roboto",
                        text_align="center",
                    ),
                    ft.ElevatedButton(
                        "Tentar Novamente",
                        on_click=lambda _: page.run_task(lambda: load_chart(page, chart_container)),
                        bgcolor=COLORS["primary"],
                        color=ft.Colors.WHITE,
                    ),
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=20,
            )
            page.update()
            return

        # Atualizar para renderização
        chart_container.content = ft.Column(
            [
                ft.Text("Renderizando gráfico...", color=COLORS["text_secondary"], font_family="Roboto"),
                progress_ring,
            ],
            alignment="center",
            horizontal_alignment="center",
        )
        page.update()

        # Criar e exibir o gráfico
        encoded_html = create_chart(data)
        if encoded_html:
            data_url = f"data:text/html;base64,{encoded_html}"
            chart_webview = ft.WebView(
                url=data_url,
                expand=True,
                bgcolor=COLORS["surface"],
            )
            chart_container.content = chart_webview
        else:
            chart_container.content = ft.Column(
                [
                    ft.Text(
                        "Erro ao renderizar gráfico",
                        color=COLORS["error"],
                        size=16,
                        font_family="Roboto",
                        text_align="center",
                    ),
                    ft.ElevatedButton(
                        "Tentar Novamente",
                        on_click=lambda _: page.run_task(lambda: load_chart(page, chart_container)),
                        bgcolor=COLORS["primary"],
                        color=ft.Colors.WHITE,
                    ),
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=20,
            )
        page.update()

    except Exception as e:
        chart_container.content = ft.Column(
            [
                ft.Text(
                    f"Erro inesperado: {str(e)}",
                    color=COLORS["error"],
                    size=16,
                    font_family="Roboto",
                    text_align="center",
                ),
                ft.ElevatedButton(
                    "Tentar Novamente",
                    on_click=lambda _: page.run_task(lambda: load_chart(page, chart_container)),
                    bgcolor=COLORS["primary"],
                    color=ft.Colors.WHITE,
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20,
        )
        page.update()

# Função principal do conteúdo da página
def currency_chart_content(page: ft.Page):
    chart_container = ft.Container(
        expand=True,
        bgcolor=COLORS["surface"],
        border_radius=ft.border_radius.all(15),
        shadow=get_shadow(),
        padding=20,
        height=400,
    )

    # Inicializar com mensagem de carregamento
    progress_ring = ft.ProgressRing(
        width=32, height=32, stroke_width=4, color=COLORS["primary"]
    )
    chart_container.content = ft.Column(
        [
            ft.Text("Carregando dados...", color=COLORS["text_secondary"], font_family="Roboto"),
            progress_ring,
        ],
        alignment="center",
        horizontal_alignment="center",
    )

    async def init_chart():
        await load_chart(page, chart_container)

    # Carregar o gráfico de forma assíncrona
    page.run_task(init_chart)

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Cotação USD/BRL",
                    size=32 if page.width > 600 else 24,
                    weight="bold",
                    color=COLORS["text_primary"],
                    text_align="center",
                ),
                ft.Text(
                    "Acompanhe a variação do dólar nos últimos 15 dias",
                    size=16 if page.width > 600 else 14,
                    color=COLORS["text_secondary"],
                    text_align="center",
                ),
                chart_container,
            ],
            expand=True,
            alignment="start",
            spacing=20,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 400),  # Altura mínima de 400px
        padding=ft.padding.symmetric(horizontal=40 if page.width > 600 else 20),
    )
