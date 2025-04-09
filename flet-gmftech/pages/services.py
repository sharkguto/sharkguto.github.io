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
                    ft.Icon(icon, color=COLORS["primary"], size=40),
                    ft.Text(title, style=get_text_style(20, weight="bold")),
                    ft.Text(description, style=get_text_style(16, COLORS["text_secondary"])),
                ],
                horizontal_alignment="center",
                alignment="center",
                spacing=10,
            ),
            padding=20,
            bgcolor=COLORS["surface"],
            border_radius=ft.border_radius.all(15),
            shadow=get_shadow(),
            expand=True,
        )

    # Lista de serviços
    services = [
        {
            "icon": ft.Icons.CODE,
            "title": "Desenvolvimento de Software",
            "description": "Soluções personalizadas para seu negócio",
        },
        {
            "icon": ft.Icons.CLOUD,
            "title": "Cloud Computing",
            "description": "Infraestrutura escalável e segura",
        },
        {
            "icon": ft.Icons.SECURITY,
            "title": "Segurança da Informação",
            "description": "Proteção para seus dados e sistemas",
        },
        {
            "icon": ft.Icons.SUPPORT_AGENT,
            "title": "Suporte Técnico",
            "description": "Assistência especializada 24/7",
        },
    ]

    # Criar os cards
    cards = [create_card(service["icon"], service["title"], service["description"]) for service in services]

    # Conteúdo da página de serviços com rolagem
    return ft.Container(
        content=ft.ListView(
            [
                ft.Text(
                    "Nossos Serviços",
                    style=get_text_style(32, weight="bold"),
                    text_align="center",
                ),
                ft.GridView(
                    [
                        card
                        for card in cards
                    ],
                    runs_count=2 if page.width > 600 else 1,
                    max_extent=300,
                    spacing=20,
                    run_spacing=20,
                    padding=20,
                ),
            ],
            spacing=20,
            padding=20,
        ),
        bgcolor=COLORS["surface"],
        border_radius=ft.border_radius.all(15),
        shadow=get_shadow(),
    )
