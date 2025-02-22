#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# services.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft


def services_content(page):
    primary_color = ft.Colors.INDIGO_700

    # Função para criar um card
    def create_card(icon, title, description):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(
                            icon,
                            size=40 if page.width > 600 else 30,
                            color=primary_color,
                        ),
                        ft.Text(
                            title, weight="bold", size=20 if page.width > 600 else 16
                        ),
                        ft.Text(
                            description,
                            size=14 if page.width > 600 else 12,
                            color=ft.Colors.GREY_700,
                        ),
                    ],
                    alignment="center",
                    spacing=10,
                ),
                padding=20,
            ),
            elevation=5,
            # Largura dinâmica: 80% da tela dividido pelo número de cards por linha
            width=page.width * 0.8 / 3
            if page.width > 900
            else page.width * 0.8 / 2
            if page.width > 600
            else page.width * 0.8,
            margin=ft.margin.all(10),
        )

    # Lista de serviços
    services = [
        (
            ft.Icons.DEVELOPER_BOARD,
            "Desenvolvimento",
            "Equipes dedicadas para seus projetos",
        ),
        (ft.Icons.SUPPORT_AGENT, "Suporte TI", "Atendimento 24/7 para sua empresa"),
        (ft.Icons.CLOUD, "Cloud Services", "Soluções em nuvem escaláveis"),
    ]

    # Criar os cards
    cards = [create_card(icon, title, desc) for icon, title, desc in services]

    # Conteúdo da página de serviços
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Nossos Serviços",
                    size=36 if page.width > 600 else 24,
                    weight="bold",
                    text_align="center",
                ),
                ft.ResponsiveRow(
                    controls=cards,
                    alignment="center",
                    spacing=20 if page.width > 600 else 10,
                ),
            ],
            alignment="center",
            spacing=20 if page.width > 600 else 10,
        ),
        padding=ft.padding.symmetric(
            vertical=50 if page.width > 600 else 30, horizontal=20
        ),
        bgcolor=ft.Colors.WHITE,
        expand=True,  # Preenche o espaço disponível (80% da tela)
    )
