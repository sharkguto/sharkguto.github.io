#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# coins.py
# @Author : Gustavo (gustavo@gmf-tech.com)

import flet as ft
import base64
from pyecharts import options as opts
from pyecharts.charts import Bar
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

    bar = (
        Bar(
            init_opts=opts.InitOpts(width="100%", height="300px", theme=ThemeType.LIGHT)
        )
        .add_xaxis(dates)
        .add_yaxis("Máxima (BRL)", highs, color="#1e88e5")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="USD/BRL - 15 Dias"),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
            tooltip_opts=opts.TooltipOpts(trigger="axis"),
        )
    )

    html = bar.render_embed()
    return base64.b64encode(html.encode("utf-8")).decode("utf-8")


# Função para carregar o gráfico em uma thread separada
def load_chart(page, chart_container):
    # Exibir mensagem de carregamento
    chart_container.content = ft.Column(
        [
            ft.Text("Carregando dados...", color=ft.Colors.GREY_600),
            ft.ProgressBar(width=300, color=ft.Colors.INDIGO_700),
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

    # Atualizar para "renderizando gráfico"
    chart_container.content = ft.Column(
        [
            ft.Text("Renderizando gráfico...", color=ft.Colors.GREY_600),
            ft.ProgressBar(width=300, color=ft.Colors.INDIGO_700),
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
                ft.ProgressBar(width=300, color=primary_color),
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
                    size=24,
                    weight="bold",
                    color=primary_color,
                    text_align="center",
                ),
                chart_container,
                ft.ElevatedButton(
                    "Voltar para Home",
                    bgcolor=secondary_color,
                    color=ft.Colors.WHITE,
                    on_click=go_to_home,
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20,
            expand=True,
        ),
        padding=ft.padding.all(20),
        bgcolor=ft.Colors.WHITE,
        expand=True,
        alignment=ft.alignment.center,
    )

    # Executar o carregamento em uma thread separada
    threading.Thread(target=load_chart, args=(page, chart_container)).start()

    return content
