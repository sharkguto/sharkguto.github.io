#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# services.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft


def services_content(page):
    primary_color = ft.Colors.INDIGO_700

    return ft.Column(
        [
            ft.Container(
                expand=True,  # Preenche o espaço disponível no layout pai
                content=ft.Column(
                    [
                        ft.Text(
                            "Nossos Serviços",
                            size=36 if page.window.width > 600 else 24,
                            weight="bold",
                            text_align="center",
                        ),
                        ft.Row(
                            [
                                ft.Card(
                                    content=ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Icon(
                                                    ft.Icons.DEVELOPER_BOARD,
                                                    size=40
                                                    if page.window.width > 600
                                                    else 30,
                                                    color=primary_color,
                                                ),
                                                ft.Text(
                                                    "Desenvolvimento",
                                                    weight="bold",
                                                    size=20
                                                    if page.window.width > 600
                                                    else 16,
                                                ),
                                                ft.Text(
                                                    "Equipes dedicadas para seus projetos",
                                                    size=14
                                                    if page.window.width > 600
                                                    else 12,
                                                    color=ft.Colors.GREY_700,
                                                ),
                                            ],
                                            alignment="center",
                                            spacing=10,
                                        ),
                                        padding=20,
                                    ),
                                    elevation=5,
                                    width=300
                                    if page.window.width > 900
                                    else 250
                                    if page.window.width > 600
                                    else 200,
                                    margin=ft.margin.all(10),
                                ),
                                ft.Card(
                                    content=ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Icon(
                                                    ft.Icons.SUPPORT_AGENT,
                                                    size=40
                                                    if page.window.width > 600
                                                    else 30,
                                                    color=primary_color,
                                                ),
                                                ft.Text(
                                                    "Suporte TI",
                                                    weight="bold",
                                                    size=20
                                                    if page.window.width > 600
                                                    else 16,
                                                ),
                                                ft.Text(
                                                    "Atendimento 24/7 para sua empresa",
                                                    size=14
                                                    if page.window.width > 600
                                                    else 12,
                                                    color=ft.Colors.GREY_700,
                                                ),
                                            ],
                                            alignment="center",
                                            spacing=10,
                                        ),
                                        padding=20,
                                    ),
                                    elevation=5,
                                    width=300
                                    if page.window.width > 900
                                    else 250
                                    if page.window.width > 600
                                    else 200,
                                    margin=ft.margin.all(10),
                                ),
                                ft.Card(
                                    content=ft.Container(
                                        content=ft.Column(
                                            [
                                                ft.Icon(
                                                    ft.Icons.CLOUD,
                                                    size=40
                                                    if page.window.width > 600
                                                    else 30,
                                                    color=primary_color,
                                                ),
                                                ft.Text(
                                                    "Cloud Services",
                                                    weight="bold",
                                                    size=20
                                                    if page.window.width > 600
                                                    else 16,
                                                ),
                                                ft.Text(
                                                    "Soluções em nuvem escaláveis",
                                                    size=14
                                                    if page.window.width > 600
                                                    else 12,
                                                    color=ft.Colors.GREY_700,
                                                ),
                                            ],
                                            alignment="center",
                                            spacing=10,
                                        ),
                                        padding=20,
                                    ),
                                    elevation=5,
                                    width=300
                                    if page.window.width > 900
                                    else 250
                                    if page.window.width > 600
                                    else 200,
                                    margin=ft.margin.all(10),
                                ),
                            ],
                            alignment="center",
                            wrap=True,
                            spacing=20 if page.window.width > 600 else 10,
                        ),
                    ]
                ),
                padding=ft.padding.symmetric(
                    vertical=50 if page.window.width > 600 else 30, horizontal=20
                ),
                bgcolor=ft.Colors.WHITE,
            )
        ]
    )
