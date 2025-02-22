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
import threading
from datetime import datetime


# Função para buscar os dados da API
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

    # Criar o gráfico de barras com máxima e mínima lado a lado
    bar = (
        Bar(
            init_opts=opts.InitOpts(width="100%", height="400px", theme=ThemeType.LIGHT)
        )
        .add_xaxis(dates)
        .add_yaxis(
            "Mínima (BRL)",
            lows,
            color="#ef5350",
            bar_width="40%",  # Largura das barras
            category_gap="20%",  # Espaço entre barras da mesma categoria
            itemstyle_opts=opts.ItemStyleOpts(opacity=0.7),
        )
        .add_yaxis(
            "Máxima (BRL)",
            highs,
            color="#1e88e5",
            bar_width="40%",  # Largura das barras
            category_gap="20%",  # Espaço entre barras da mesma categoria
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

    # Criar a linha de variação para ficar "na frente"
    line = (
        Line()
        .add_xaxis(dates)
        .add_yaxis(
            "Variação (%)",
            pct_changes,
            yaxis_index=1,
            color="#26a69a",
            linestyle_opts=opts.LineStyleOpts(width=4, opacity=1),  # Linha destacada
            label_opts=opts.LabelOpts(is_show=False),
            z_level=1,  # Colocar a linha na frente das barras
        )
    )

    # Sobrepor a linha às barras
    bar.overlap(line)
    html = bar.render_embed()
    return base64.b64encode(html.encode("utf-8")).decode("utf-8")


# Função para carregar o gráfico em uma thread separada
def load_chart(page, chart_container):
    chart_container.content = ft.Column(
        [
            ft.Text("Carregando dados...", color=ft.Colors.GREY_600),
            ft.ProgressBar(width=300, color=ft.Colors.INDIGO_700),
        ],
        alignment="center",
        horizontal_alignment="center",
    )
    page.update()

    data = fetch_usd_brl_data()
    if not data:
        chart_container.content = ft.Text(
            "Erro ao carregar dados", color=ft.Colors.RED_400
        )
        page.update()
        return

    chart_container.content = ft.Column(
        [
            ft.Text("Renderizando gráfico...", color=ft.Colors.GREY_600),
            ft.ProgressBar(width=300, color=ft.Colors.INDIGO_700),
        ],
        alignment="center",
        horizontal_alignment="center",
    )
    page.update()

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
        content=ft.Column(
            [
                ft.Text("Iniciando...", color=ft.Colors.GREY_600),
                ft.ProgressBar(
                    width=300 if page.width > 600 else 200, color=primary_color
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
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

    threading.Thread(target=load_chart, args=(page, chart_container)).start()
    return content
