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
from theme import COLORS, get_shadow, get_text_style, get_responsive_font_size, get_responsive_padding
from utils.responsive import ResponsiveConfig

try:
    import pyodide
    from pyodide.http import pyfetch

    IS_PYODIDE = True
except ImportError:
    IS_PYODIDE = False
    import httpx

from datetime import datetime
import asyncio

# Cache global para os dados e gráfico
_cached_data = None
_cached_chart = None
_last_update = None
_is_fetching = False

# Função assíncrona para pré-carregar os dados
async def preload_data():
    """
    Pré-carrega os dados da cotação para melhorar a performance inicial.
    Esta função é chamada durante a inicialização da aplicação.
    """
    try:
        await fetch_usd_brl_data(force_refresh=True)
    except Exception:
        # Ignora erros durante o pré-carregamento
        pass

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
        
        # Se chegou aqui, todas as tentativas falharam
        return _cached_data if _cached_data else []
    finally:
        _is_fetching = False

# Função para criar o gráfico com Pyecharts
def create_chart(data, chart_height="400px"):
    global _cached_chart
    
    if not data:
        return None

    # Se já temos um gráfico em cache para esses dados e mesma altura, retorna ele
    if _cached_chart and _cached_data == data:
        return _cached_chart
        
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
                height=chart_height,
                theme=ThemeType.LIGHT,
                animation_opts=opts.AnimationOpts(animation=False),
                js_host="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/",
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
            title_opts=opts.TitleOpts(title=""),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(rotate=45),
                boundary_gap=True
            ),
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
            linestyle_opts=opts.LineStyleOpts(width=3, opacity=1),
            label_opts=opts.LabelOpts(is_show=False),
        )
    )

    bar.overlap(line)
    html = bar.render_embed()
    _cached_chart = base64.b64encode(html.encode("utf-8")).decode("utf-8")
    return _cached_chart

# Função assíncrona para carregar o gráfico
async def load_chart(page, chart_container, error_button, chart_height):
    try:
        # Buscar os dados (usa cache se disponível)
        data = await fetch_usd_brl_data()
        
        # Detect breakpoint for responsive error messages
        breakpoint = ResponsiveConfig.get_breakpoint(page.width if page.width else 1024)
        error_font_size = get_responsive_font_size(16, page.width if page.width else 1024)
        
        if not data:
            chart_container.content = ft.Column(
                [
                    ft.Text(
                        "Erro ao carregar dados",
                        color=COLORS["error"],
                        size=error_font_size,
                        font_family="Roboto",
                        text_align="center",
                    ),
                    error_button,
                ],
                alignment="center",
                horizontal_alignment="center",
                spacing=20,
            )
            page.update()
            return

        # Criar e exibir o gráfico
        encoded_html = create_chart(data, chart_height)
        if encoded_html:
            data_url = f"data:text/html;base64,{encoded_html}"
            chart_webview = ft.WebView(
                url=data_url,
                expand=True,
                bgcolor=COLORS["surface"],
                visible=True,
            )
            chart_container.content = chart_webview
        else:
            chart_container.content = ft.Column(
                [
                    ft.Text(
                        "Erro ao renderizar gráfico",
                        color=COLORS["error"],
                        size=error_font_size,
                        font_family="Roboto",
                        text_align="center",
                    ),
                    error_button,
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
                    size=error_font_size,
                    font_family="Roboto",
                    text_align="center",
                ),
                error_button,
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20,
        )
        page.update()

# Função principal do conteúdo da página
def currency_chart_content(page: ft.Page):
    # Detect breakpoint for responsive design
    width = page.width if page.width else 1024
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    
    # Responsive values
    title_size = get_responsive_font_size(32, width)
    subtitle_size = get_responsive_font_size(16, width)
    container_padding = get_responsive_padding(20, width)
    horizontal_padding = get_responsive_padding(40, width)
    spacing = get_responsive_padding(20, width)
    
    # Chart height based on breakpoint (mobile: 300px, tablet: 350px, desktop: 400px)
    chart_heights = {
        ResponsiveConfig.get_breakpoint(400): 300,   # Mobile
        ResponsiveConfig.get_breakpoint(768): 350,   # Tablet
        ResponsiveConfig.get_breakpoint(1920): 400   # Desktop
    }
    chart_height = chart_heights.get(breakpoint, 400)
    chart_height_str = f"{chart_height}px"
    
    # Definir o botão de erro primeiro
    error_button = ft.ElevatedButton(
        "Tentar Novamente",
        bgcolor=COLORS["primary"],
        color=ft.Colors.WHITE,
    )

    chart_container = ft.Container(
        expand=True,
        bgcolor=COLORS["surface"],
        border_radius=ft.border_radius.all(15),
        shadow=get_shadow(),
        padding=container_padding,
        height=chart_height,
    )

    # Inicializar com mensagem de carregamento - properly centered
    loading_font_size = get_responsive_font_size(16, width)
    progress_ring = ft.ProgressRing(
        width=32, height=32, stroke_width=4, color=COLORS["primary"]
    )
    chart_container.content = ft.Column(
        [
            ft.Text(
                "Carregando dados...", 
                color=COLORS["text_secondary"], 
                font_family="Roboto",
                size=loading_font_size,
                text_align="center"
            ),
            progress_ring,
        ],
        alignment="center",
        horizontal_alignment="center",
        expand=True,
    )

    async def retry_load_chart(e):
        await load_chart(page, chart_container, error_button, chart_height_str)

    error_button.on_click = retry_load_chart

    # Inicialização do gráfico
    async def init_chart():
        await load_chart(page, chart_container, error_button, chart_height_str)

    # Carregar o gráfico de forma assíncrona
    page.run_task(init_chart)

    return ft.Container(
        content=ft.Stack(
            [
                ft.Column(
                    [
                        ft.Text(
                            "Cotação USD/BRL",
                            size=title_size,
                            weight="bold",
                            color=COLORS["text_primary"],
                            text_align="center",
                        ),
                        ft.Text(
                            "Acompanhe a variação do dólar nos últimos 15 dias",
                            size=subtitle_size,
                            color=COLORS["text_secondary"],
                            text_align="center",
                        ),
                        chart_container,
                    ],
                    expand=True,
                    alignment="start",
                    spacing=spacing,
                ),
                ft.Container(
                    expand=True,
                    bgcolor=ft.colors.TRANSPARENT,
                )
            ],
            expand=True,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 400),
        padding=ft.padding.symmetric(horizontal=horizontal_padding),
    )
