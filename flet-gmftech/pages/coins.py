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
import json
from datetime import datetime


# Função assíncrona para buscar dados da API
async def fetch_usd_brl_data(page):
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15"
    req = ft.HttpRequest(method="GET", url=url)
    response = await page.client_session.send(req)
    if response.status_code == 200:
        return json.loads(response.text)
    return []


# Função simplificada para criar o gráfico
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


# Função da página com gráfico
def currency_chart_content(page):
    primary_color = ft.Colors.INDIGO_700
    secondary_color = ft.Colors.AMBER_600

    # Função para voltar à home
    def go_to_home(e):
        page.go("/")

    # Container com barra de progresso inicial
    progress_bar = ft.ProgressBar(width=300, color=primary_color)
    chart_container = ft.Container(
        content=ft.Column(
            [ft.Text("Carregando dados...", color=ft.Colors.GREY_600), progress_bar],
            alignment="center",
            horizontal_alignment="center",
        ),
        alignment=ft.alignment.center,
        expand=True,
    )

    # Função assíncrona para carregar dados e gráfico
    async def load_chart():
        # Buscar dados
        data = await fetch_usd_brl_data(page)
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
                progress_bar,
            ],
            alignment="center",
            horizontal_alignment="center",
        )
        page.update()

        # Criar o gráfico
        encoded_html = create_chart(data)
        data_url = f"data:text/html;base64,{encoded_html}"

        # Exibir o WebView
        chart_webview = ft.WebView(
            url=data_url,
            expand=True,
            bgcolor=ft.Colors.WHITE,
        )
        chart_container.content = chart_webview
        page.update()

    # Layout da página
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

    # Iniciar carregamento assíncrono
    page.run_task(load_chart)

    return content
