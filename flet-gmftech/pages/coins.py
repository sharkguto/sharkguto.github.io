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


# Função assíncrona para buscar os dados da API
async def fetch_usd_brl_data():
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15"
    if IS_PYODIDE:
        # Usar pyfetch no ambiente web
        try:
            response = await pyfetch(url, method="GET")
            if response.status == 200:
                return await response.json()
            else:
                print(f"Erro: status code {response.status}")
                return []
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")
            return []
    else:
        # Usar httpx no ambiente desktop/servidor
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url)
                if response.status_code == 200:
                    return response.json()
                else:
                    print(f"Erro: status code {response.status_code}")
                    return []
            except Exception as e:
                print(f"Erro ao buscar dados: {e}")
                return []


# Função para criar o gráfico com Pyecharts
def create_chart(data):
    dates = [
        datetime.fromtimestamp(int(entry["timestamp"])).strftime("%d/%m")
        for entry in data[::-1]
    ]
    highs = [float(entry["high"]) for entry in data[::-1]]
    lows = [float(entry["low"]) for entry in data[::-1]]
    pct_changes = [float(entry["pctChange"]) for entry in data[::-1]]

    bar = (
        Bar(
            init_opts=opts.InitOpts(width="100%", height="400px", theme=ThemeType.LIGHT)
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

    # Buscar os dados
    data = await fetch_usd_brl_data()
    if not data:
        chart_container.content = ft.Text(
            "Erro ao carregar dados", color=COLORS["error"], font_family="Roboto"
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
    data_url = f"data:text/html;base64,{encoded_html}"
    chart_webview = ft.WebView(
        url=data_url,
        expand=True,
        bgcolor=COLORS["surface"],
    )
    chart_container.content = chart_webview
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

    async def init_chart():
        await load_chart(page, chart_container)

    # Carregar o gráfico de forma assíncrona
    page.add_async_callback(init_chart)

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
