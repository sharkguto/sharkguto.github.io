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
import requests
from datetime import datetime
import time


# Função para buscar os dados da API usando requests
def fetch_usd_brl_data():
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15"
    try:
        response = requests.get(url)
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
            color="#ef5350",
            bar_width="40%",
            category_gap="20%",
            itemstyle_opts=opts.ItemStyleOpts(opacity=0.7),
        )
        .add_yaxis(
            "Máxima (BRL)",
            highs,
            color="#1e88e5",
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
            color="#26a69a",
            linestyle_opts=opts.LineStyleOpts(width=4, opacity=1),
            label_opts=opts.LabelOpts(is_show=False),
            z_level=1,
        )
    )

    bar.overlap(line)
    html = bar.render_embed()
    return base64.b64encode(html.encode("utf-8")).decode("utf-8")


# Função para carregar o gráfico com progresso simulado
def load_chart(page, chart_container):
    # Exibir mensagem de carregamento inicial
    progress_ring = ft.ProgressRing(
        width=32, height=32, stroke_width=4, color=ft.Colors.INDIGO_700
    )
    chart_container.content = ft.Column(
        [
            ft.Text("Carregando dados...", color=ft.Colors.GREY_600),
            progress_ring,
        ],
        alignment="center",
        horizontal_alignment="center",
    )
    page.update()

    # Buscar os dados
    data = fetch_usd_brl_data()
    if not data:
        chart_container.content = ft.Text(
            "Erro ao carregar dados", color=ft.Colors.RED_400
        )
        page.update()
        return

    # Atualizar para renderização com progresso
    chart_container.content = ft.Column(
        [
            ft.Text("Renderizando gráfico...", color=ft.Colors.GREY_600),
            progress_ring,
        ],
        alignment="center",
        horizontal_alignment="center",
    )
    page.update()

    # Simular progresso incremental (0 a 100%)
    steps = 101  # De 0 a 100
    for i in range(steps):
        progress_ring.value = i / 100.0  # Progresso de 0.0 a 1.0
        time.sleep(0.02)  # Simulação de atraso
        page.update()  # Atualizar a página inteira, pois o ProgressRing já está vinculado

    # Criar e exibir o gráfico
    encoded_html = create_chart(data)
    data_url = f"data:text/html;base64,{encoded_html}"
    chart_webview = ft.WebView(
        url=data_url,
        expand=True,
        bgcolor=ft.Colors.WHITE,
    )
    chart_container.content = chart_webview
    page.update()


# Função principal do conteúdo da página
def currency_chart_content(page):
    primary_color = ft.Colors.INDIGO_700
    secondary_color = ft.Colors.AMBER_600

    def go_to_home(e):
        page.go("/")

    chart_container = ft.Container(
        content=ft.Text(
            "Iniciando...", color=ft.Colors.GREY_600
        ),  # Placeholder inicial
        alignment=ft.alignment.center,
        expand=True,
    )

    content = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Cotação USD/BRL",
                    size=36 if page.width > 600 else 24,
                    weight="bold",
                    color=primary_color,
                    text_align="center",
                ),
                ft.Text(
                    "Últimos 15 dias",
                    size=20 if page.width > 600 else 16,
                    color=ft.Colors.GREY_700,
                    text_align="center",
                ),
                chart_container,
                ft.ElevatedButton(
                    "Voltar para Home",
                    bgcolor=secondary_color,
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                    on_click=go_to_home,
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20 if page.width > 600 else 10,
            expand=True,
        ),
        padding=ft.padding.symmetric(
            vertical=50 if page.width > 600 else 30, horizontal=20
        ),
        bgcolor=ft.Colors.WHITE,
        expand=True,
        alignment=ft.alignment.center,
    )

    # Carregar o gráfico de forma síncrona com progresso simulado
    load_chart(page, chart_container)

    return content
