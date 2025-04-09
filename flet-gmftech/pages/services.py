#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# services.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from theme import COLORS, get_text_style, get_button_style, get_shadow


def services_content(page: ft.Page):
    # Função para criar um card
    def create_card(icon, title, description):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(
                        icon,
                        size=40 if page.width > 600 else 30,
                        color=COLORS["primary"],
                    ),
                    ft.Text(
                        title,
                        size=20 if page.width > 600 else 16,
                        weight="bold",
                        color=COLORS["text_primary"],
                        text_align="center",
                    ),
                    ft.Text(
                        description,
                        size=16 if page.width > 600 else 14,
                        color=COLORS["text_secondary"],
                        text_align="center",
                    ),
                ],
                horizontal_alignment="center",
                alignment="center",
                spacing=10 if page.width > 600 else 8,
            ),
            padding=ft.padding.all(20 if page.width > 600 else 15),
            bgcolor=COLORS["surface"],
            border_radius=ft.border_radius.all(15),
            shadow=get_shadow(),
            expand=True,
        )

    # Lista de serviços
    services = [
        {
            "icon": ft.icons.COMPUTER,
            "title": "Desenvolvimento Web",
            "description": "Criamos sites e aplicações web modernas e responsivas.",
        },
        {
            "icon": ft.icons.PHONE_ANDROID,
            "title": "Desenvolvimento Mobile",
            "description": "Desenvolvemos aplicativos nativos e híbridos para iOS e Android.",
        },
        {
            "icon": ft.icons.CLOUD,
            "title": "Cloud Computing",
            "description": "Soluções em nuvem para escalabilidade e performance.",
        },
        {
            "icon": ft.icons.SECURITY,
            "title": "Segurança",
            "description": "Proteção e segurança para seus dados e aplicações.",
        },
    ]

    # Criar os cards
    cards = [create_card(service["icon"], service["title"], service["description"]) for service in services]

    # Conteúdo da página de serviços com rolagem
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Nossos Serviços",
                    size=32 if page.width > 600 else 24,
                    weight="bold",
                    color=COLORS["text_primary"],
                    text_align="center",
                ),
                ft.Container(
                    content=ft.GridView(
                        [
                            card
                            for card in cards
                        ],
                        runs_count=2 if page.width > 600 else 1,
                        max_extent=300,
                        spacing=20 if page.width > 600 else 15,
                        run_spacing=20 if page.width > 600 else 15,
                        expand=True,
                    ),
                    padding=ft.padding.symmetric(
                        horizontal=40 if page.width > 600 else 20,
                        vertical=20 if page.width > 600 else 15,
                    ),
                    expand=True,
                ),
            ],
            expand=True,
            alignment="center",
            spacing=20 if page.width > 600 else 15,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 400),  # Altura mínima de 400px
        padding=ft.padding.symmetric(horizontal=40 if page.width > 600 else 20),
    )
