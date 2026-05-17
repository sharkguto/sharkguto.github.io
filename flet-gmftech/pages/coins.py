#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# coins.py
# @Author : Gustavo (gustavo@gmf-tech.com)

import flet as ft
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

# Função para criar o gráfico com controles nativos do Flet
def create_chart(data, chart_height="400px"):
    if not data:
        return None
    
    points = []
    for entry in data[::-1]:
        try:
            points.append(
                {
                    "date": datetime.fromtimestamp(int(entry["timestamp"])).strftime("%d/%m"),
                    "high": float(entry["high"]),
                    "low": float(entry["low"]),
                    "pct_change": float(entry.get("pctChange", 0)),
                }
            )
        except (KeyError, TypeError, ValueError, OSError):
            continue

    if not points:
        return None

    height = _parse_chart_height(chart_height)
    max_bar_height = max(min(height - 150, 240), 110)
    high_value = max(point["high"] for point in points)
    low_value = min(point["low"] for point in points)
    spread = max(high_value - low_value, 0.01)

    def bar_height(value):
        return max(14, int(18 + ((value - low_value) / spread) * (max_bar_height - 18)))

    day_columns = []
    for point in points:
        pct_color = COLORS["success"] if point["pct_change"] >= 0 else COLORS["error"]
        day_columns.append(
            ft.Container(
                width=76,
                content=ft.Column(
                    [
                        ft.Container(
                            height=max_bar_height,
                            alignment=ft.Alignment.BOTTOM_CENTER,
                            content=ft.Row(
                                [
                                    ft.Container(
                                        width=18,
                                        height=bar_height(point["low"]),
                                        bgcolor=COLORS["error"],
                                        border_radius=ft.BorderRadius.only(top_left=4, top_right=4),
                                        tooltip=f"Mínima: R$ {point['low']:.2f}",
                                    ),
                                    ft.Container(
                                        width=18,
                                        height=bar_height(point["high"]),
                                        bgcolor=COLORS["accent"],
                                        border_radius=ft.BorderRadius.only(top_left=4, top_right=4),
                                        tooltip=f"Máxima: R$ {point['high']:.2f}",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                vertical_alignment=ft.CrossAxisAlignment.END,
                                spacing=4,
                            ),
                        ),
                        ft.Text(
                            point["date"],
                            size=11,
                            color=COLORS["text_secondary"],
                            text_align="center",
                        ),
                        ft.Text(
                            f"R$ {point['high']:.2f}",
                            size=11,
                            color=COLORS["text_primary"],
                            text_align="center",
                        ),
                        ft.Text(
                            f"{point['pct_change']:+.2f}%",
                            size=11,
                            color=pct_color,
                            text_align="center",
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=4,
                ),
            )
        )

    return ft.Container(
        expand=True,
        bgcolor=COLORS["surface"],
        data={"points": points, "low": low_value, "high": high_value},
        content=ft.Column(
            [
                ft.Row(
                    [
                        _legend_item("Mínima", COLORS["error"]),
                        _legend_item("Máxima", COLORS["accent"]),
                        _legend_item("Variação", COLORS["success"]),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=14,
                    wrap=True,
                ),
                ft.Row(
                    day_columns,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.END,
                    spacing=10,
                    scroll=ft.ScrollMode.AUTO,
                    expand=True,
                ),
                ft.Text(
                    f"Faixa no período: R$ {low_value:.2f} - R$ {high_value:.2f}",
                    size=12,
                    color=COLORS["text_secondary"],
                    text_align="center",
                ),
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=12,
        ),
    )


def _parse_chart_height(chart_height):
    if isinstance(chart_height, (int, float)):
        return int(chart_height)

    if isinstance(chart_height, str):
        normalized = chart_height.strip().lower().replace("px", "")
        try:
            return int(float(normalized))
        except ValueError:
            pass

    return 400


def _legend_item(label, color):
    return ft.Row(
        [
            ft.Container(
                width=12,
                height=12,
                bgcolor=color,
                border_radius=ft.BorderRadius.all(3),
            ),
            ft.Text(label, size=12, color=COLORS["text_secondary"]),
        ],
        spacing=5,
        tight=True,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

# Função assíncrona para carregar o gráfico
async def load_chart(page, chart_container, error_button, chart_height):
    width = page.width if page.width else 1024
    error_font_size = get_responsive_font_size(16, width)

    try:
        # Buscar os dados (usa cache se disponível)
        data = await fetch_usd_brl_data()

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
        chart = create_chart(data, chart_height)
        if chart:
            chart_container.content = chart
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
    error_button = ft.Button(
        "Tentar Novamente",
        bgcolor=COLORS["primary"],
        color=ft.Colors.WHITE,
    )

    chart_container = ft.Container(
        expand=True,
        bgcolor=COLORS["surface"],
        border_radius=ft.BorderRadius.all(15),
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
                    bgcolor=ft.Colors.TRANSPARENT,
                )
            ],
            expand=True,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 400),
        padding=ft.Padding.symmetric(horizontal=horizontal_padding),
    )
