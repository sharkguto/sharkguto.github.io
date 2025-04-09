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
        is_mobile = page.width <= 600
        card_padding = 15 if is_mobile else 20
        content_width = page.width - (2 * card_padding) - 40  # Considerando margens e padding do container pai
        
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Icon(
                            icon,
                            size=32 if is_mobile else 40,
                            color=COLORS["primary"],
                        ),
                        margin=ft.margin.only(bottom=8 if is_mobile else 10),
                    ),
                    ft.Container(
                        content=ft.Text(
                            title,
                            size=16 if is_mobile else 20,
                            weight="bold",
                            color=COLORS["text_primary"],
                            text_align="center",
                        ),
                        margin=ft.margin.only(bottom=8 if is_mobile else 10),
                    ),
                    ft.Container(
                        content=ft.Text(
                            description,
                            size=14 if is_mobile else 16,
                            color=COLORS["text_secondary"],
                            text_align="center",
                            width=content_width if is_mobile else 280,
                        ),
                        margin=ft.margin.only(bottom=5),
                    ),
                ],
                horizontal_alignment="center",
                alignment="center",
                spacing=5,
            ),
            padding=ft.padding.all(card_padding),
            bgcolor=COLORS["surface"],
            border_radius=ft.border_radius.all(15),
            shadow=get_shadow(),
            width=None,  # Permitir que a largura seja controlada pelo GridView
            height=None,  # Altura automática
            margin=ft.margin.all(5),
        )

    # Lista de serviços
    services = [
        {
            "icon": ft.icons.ASSIGNMENT,
            "title": "Levantamento de Requisitos",
            "description": "Análise detalhada e documentação das necessidades do seu projeto.",
        },
        {
            "icon": ft.icons.ARCHITECTURE,
            "title": "Arquitetura de Software",
            "description": "Design e planejamento de soluções escaláveis e robustas.",
        },
        {
            "icon": ft.icons.DEVELOPER_BOARD,
            "title": "IoT com Arduino",
            "description": "Desenvolvimento de soluções IoT com hardware Arduino.",
        },
        {
            "icon": ft.icons.PRECISION_MANUFACTURING,
            "title": "Prototipagem Eletrônica",
            "description": "Simulação e prototipagem com SimulIDE para validação de projetos.",
        },
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
            "icon": ft.icons.DATA_OBJECT,
            "title": "ScyllaDB",
            "description": "Banco NoSQL de alta performance e baixa latência.",
        },
        {
            "icon": ft.icons.MEMORY,
            "title": "Redis",
            "description": "Cache distribuído e banco de dados em memória.",
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
                    size=24 if page.width > 600 else 20,
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
                    max_extent=320 if page.width > 600 else page.width,
                    spacing=8,
                    run_spacing=8,
                    child_aspect_ratio=None,
                    padding=ft.padding.symmetric(
                        horizontal=10,
                        vertical=8,
                    ),
                ),
                ft.Container(
                    content=ft.Text(
                        "Tecnologias",
                        size=24 if page.width > 600 else 20,
                        weight="bold",
                        color=COLORS["text_primary"],
                        text_align="center",
                    ),
                    margin=ft.margin.only(top=30),
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
                    max_extent=320 if page.width > 600 else page.width,
                    spacing=8,
                    run_spacing=8,
                    child_aspect_ratio=None,
                    padding=ft.padding.symmetric(
                        horizontal=10,
                        vertical=8,
                    ),
                ),
            ],
            scroll=None,
            spacing=15,
        ),
        padding=ft.padding.symmetric(horizontal=10),
    )
