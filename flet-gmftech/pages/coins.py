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


def fetch_usd_brl_data():
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return []


# Conteúdo da página com o gráfico
def currency_chart_content(page):
    primary_color = ft.Colors.INDIGO_700
    secondary_color = ft.Colors.AMBER_600

    # Função para voltar à home
    def go_to_home(e):
        page.go("/")

    # Container inicial com mensagem de carregamento
    chart_container = ft.Container(
        content=ft.Text("Carregando gráfico...", color=ft.Colors.GREY_500),
        alignment=ft.alignment.center,
        expand=True,
    )

    # Função para carregar o gráfico (síncrona, pois usa requests)
    def load_chart(page):
        # Buscar os dados da API
        data = fetch_usd_brl_data()
        if not data:
            chart_container.content = ft.Text(
                "Erro ao carregar os dados da API", color=ft.Colors.RED_400
            )
            page.update()
            return

        # Preparar os dados para o gráfico
        # Converter timestamp Unix para data legível (DD/MM/YYYY)
        dates = [
            datetime.fromtimestamp(int(entry["timestamp"])).strftime("%d/%m/%Y")
            for entry in data[::-1]  # Ordem cronológica
        ]
        highs = [float(entry["high"]) for entry in data[::-1]]
        lows = [float(entry["low"]) for entry in data[::-1]]
        pct_changes = [float(entry["pctChange"]) for entry in data[::-1]]

        # Criar o gráfico com Pyecharts
        bar = (
            Bar(
                init_opts=opts.InitOpts(
                    width="100%", height="400px", theme=ThemeType.LIGHT
                )
            )
            .add_xaxis(dates)
            .add_yaxis("Máxima (BRL)", highs, color="#1e88e5")
            .add_yaxis("Mínima (BRL)", lows, color="#ef5350")
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
                tooltip_opts=opts.TooltipOpts(
                    trigger="axis", axis_pointer_type="cross"
                ),
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
                linestyle_opts=opts.LineStyleOpts(width=2),
                label_opts=opts.LabelOpts(is_show=False),
            )
        )

        # Combinar gráficos de barras e linha
        bar.overlap(line)

        # Renderizar o gráfico em HTML e codificar em base64
        html = bar.render_embed()
        encoded_html = base64.b64encode(html.encode("utf-8")).decode("utf-8")
        data_url = f"data:text/html;base64,{encoded_html}"

        # Criar o WebView para exibir o gráfico
        chart_webview = ft.WebView(
            url=data_url,
            expand=True,
            on_page_started=lambda _: print("Gráfico iniciado"),
            on_page_ended=lambda _: print("Gráfico carregado"),
            on_web_resource_error=lambda e: print(f"Erro no gráfico: {e.data}"),
        )

        # Ajustar a altura do WebView dinamicamente
        chart_webview.height = page.height * 0.6  # 60% da altura da tela

        # Atualizar o container com o gráfico
        chart_container.content = chart_webview
        page.update()

    # Layout da página
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

    # Chamar a função de carregamento do gráfico (síncrona)
    load_chart(page)

    return content
