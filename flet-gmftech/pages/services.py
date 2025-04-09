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
                    ft.Container(
                        content=ft.Icon(
                            icon,
                            size=40 if page.width > 600 else 32,
                            color=COLORS["primary"],
                        ),
                        margin=ft.margin.only(bottom=10),
                    ),
                    ft.Container(
                        content=ft.Text(
                            title,
                            size=20 if page.width > 600 else 18,
                            weight="bold",
                            color=COLORS["text_primary"],
                            text_align="center",
                        ),
                        margin=ft.margin.only(bottom=10),
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
                spacing=0,
            ),
            padding=ft.padding.all(25 if page.width > 600 else 20),
            bgcolor=COLORS["surface"],
            border_radius=ft.border_radius.all(15),
            shadow=get_shadow(),
            width=300 if page.width > 600 else None,
            height=200 if page.width > 600 else 180,
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

    technologies = [
        {
            "icon": ft.icons.CODE,
            "title": "Python",
            "description": "Desenvolvimento backend robusto e eficiente.",
        },
        {
            "icon": ft.icons.DEVICES,
            "title": "Flet",
            "description": "Apps multiplataforma com WebAssembly.",
        },
        {
            "icon": ft.icons.STORAGE,
            "title": "PostgreSQL",
            "description": "Banco de dados relacional de alta performance.",
        },
        {
            "icon": ft.icons.CLOUD_QUEUE,
            "title": "AWS",
            "description": "Infraestrutura em nuvem escalável e confiável.",
        },
        {
            "icon": ft.icons.INTEGRATION_INSTRUCTIONS,
            "title": "Azure DevOps",
            "description": "CI/CD e gestão ágil de projetos.",
        },
    ]

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
                ft.GridView(
                    [
                        create_card(
                            service["icon"],
                            service["title"],
                            service["description"],
                        )
                        for service in services
                    ],
                    runs_count=2 if page.width > 600 else 1,
                    max_extent=320 if page.width > 600 else 400,
                    spacing=20 if page.width > 600 else 15,
                    run_spacing=20 if page.width > 600 else 15,
                    child_aspect_ratio=1.5,
                    padding=ft.padding.symmetric(
                        horizontal=20 if page.width > 600 else 10,
                        vertical=10,
                    ),
                ),
                ft.Container(
                    content=ft.Text(
                        "Tecnologias",
                        size=32 if page.width > 600 else 24,
                        weight="bold",
                        color=COLORS["text_primary"],
                        text_align="center",
                    ),
                    margin=ft.margin.only(top=40),
                ),
                ft.GridView(
                    [
                        create_card(
                            tech["icon"],
                            tech["title"],
                            tech["description"],
                        )
                        for tech in technologies
                    ],
                    runs_count=3 if page.width > 900 else (2 if page.width > 600 else 1),
                    max_extent=320 if page.width > 600 else 400,
                    spacing=20 if page.width > 600 else 15,
                    run_spacing=20 if page.width > 600 else 15,
                    child_aspect_ratio=1.5,
                    padding=ft.padding.symmetric(
                        horizontal=20 if page.width > 600 else 10,
                        vertical=10,
                    ),
                ),
            ],
            scroll=None,  # Desabilita o scroll individual
            spacing=20 if page.width > 600 else 15,
        ),
        padding=ft.padding.symmetric(horizontal=20 if page.width > 600 else 10),
    )
