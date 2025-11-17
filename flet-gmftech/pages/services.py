#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# services.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from theme import COLORS, get_text_style, get_button_style, get_shadow, get_responsive_font_size, get_responsive_padding
from utils.responsive import ResponsiveConfig


def services_content(page: ft.Page):
    # Detect breakpoint for responsive layout
    breakpoint = ResponsiveConfig.get_breakpoint(page.width)
    
    # Função para criar um card
    def create_card(icon, title, description):
        # Use responsive padding instead of hardcoded values
        card_padding = get_responsive_padding(20, page.width)
        
        # Use responsive font sizes
        icon_size = get_responsive_font_size(40, page.width)
        title_size = get_responsive_font_size(20, page.width)
        description_size = get_responsive_font_size(16, page.width)
        
        # Use responsive spacing
        bottom_spacing = get_responsive_padding(10, page.width)
        
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Icon(
                            icon,
                            size=icon_size,
                            color=COLORS["primary"],
                        ),
                        margin=ft.margin.only(bottom=bottom_spacing),
                    ),
                    ft.Container(
                        content=ft.Text(
                            title,
                            size=title_size,
                            weight="bold",
                            color=COLORS["text_primary"],
                            text_align="center",
                        ),
                        margin=ft.margin.only(bottom=bottom_spacing),
                    ),
                    ft.Container(
                        content=ft.Text(
                            description,
                            size=description_size,
                            color=COLORS["text_secondary"],
                            text_align="center",
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
            "icon": ft.Icons.ASSIGNMENT,
            "title": "Levantamento de Requisitos",
            "description": "Análise detalhada e documentação das necessidades do seu projeto.",
        },
        {
            "icon": ft.Icons.ARCHITECTURE,
            "title": "Arquitetura de Software",
            "description": "Design e planejamento de soluções escaláveis e robustas.",
        },
        {
            "icon": ft.Icons.DEVELOPER_BOARD,
            "title": "IoT com Arduino",
            "description": "Desenvolvimento de soluções IoT com hardware Arduino.",
        },
        {
            "icon": ft.Icons.PRECISION_MANUFACTURING,
            "title": "Prototipagem Eletrônica",
            "description": "Simulação e prototipagem com SimulIDE para validação de projetos.",
        },
        {
            "icon": ft.Icons.COMPUTER,
            "title": "Desenvolvimento Web",
            "description": "Criamos sites e aplicações web modernas e responsivas.",
        },
        {
            "icon": ft.Icons.PHONE_ANDROID,
            "title": "Desenvolvimento Mobile",
            "description": "Desenvolvemos aplicativos nativos e híbridos para iOS e Android.",
        },
        {
            "icon": ft.Icons.CLOUD,
            "title": "Cloud Computing",
            "description": "Soluções em nuvem para escalabilidade e performance.",
        },
        {
            "icon": ft.Icons.SECURITY,
            "title": "Segurança",
            "description": "Proteção e segurança para seus dados e aplicações.",
        },
    ]

    technologies = [
        {
            "icon": ft.Icons.CODE,
            "title": "Python",
            "description": "Desenvolvimento backend robusto e eficiente.",
        },
        {
            "icon": ft.Icons.DEVICES,
            "title": "Flet",
            "description": "Apps multiplataforma com WebAssembly.",
        },
        {
            "icon": ft.Icons.STORAGE,
            "title": "PostgreSQL",
            "description": "Banco de dados relacional de alta performance.",
        },
        {
            "icon": ft.Icons.DATA_OBJECT,
            "title": "ScyllaDB",
            "description": "Banco NoSQL de alta performance e baixa latência.",
        },
        {
            "icon": ft.Icons.MEMORY,
            "title": "Redis",
            "description": "Cache distribuído e banco de dados em memória.",
        },
        {
            "icon": ft.Icons.CLOUD_QUEUE,
            "title": "AWS",
            "description": "Infraestrutura em nuvem escalável e confiável.",
        },
        {
            "icon": ft.Icons.INTEGRATION_INSTRUCTIONS,
            "title": "Azure DevOps",
            "description": "CI/CD e gestão ágil de projetos.",
        },
        {
            "icon": ft.Icons.INSERT_CHART,
            "title": "Apache ECharts",
            "description": "Biblioteca de visualização de dados interativa e responsiva.",
        },
    ]

    # Use responsive grid columns based on breakpoint
    services_grid_columns = ResponsiveConfig.get_grid_columns(breakpoint)
    # For services, use 1 column on mobile, 2 on tablet/desktop
    services_runs_count = 1 if page.width < 768 else 2
    
    # For technologies, use full responsive grid (1, 2, 3)
    tech_grid_columns = ResponsiveConfig.get_grid_columns(breakpoint)
    
    # Use responsive title size
    title_size = get_responsive_font_size(24, page.width)
    
    # Use responsive spacing
    grid_spacing = get_responsive_padding(8, page.width)
    section_spacing = get_responsive_padding(30, page.width)
    
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Nossos Serviços",
                    size=title_size,
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
                    runs_count=services_runs_count,
                    max_extent=400,
                    spacing=grid_spacing,
                    run_spacing=grid_spacing,
                    child_aspect_ratio=None,
                    padding=ft.padding.symmetric(
                        horizontal=10,
                        vertical=8,
                    ),
                ),
                ft.Container(
                    content=ft.Text(
                        "Tecnologias",
                        size=title_size,
                        weight="bold",
                        color=COLORS["text_primary"],
                        text_align="center",
                    ),
                    margin=ft.margin.only(top=section_spacing),
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
                    runs_count=tech_grid_columns,
                    max_extent=400,
                    spacing=grid_spacing,
                    run_spacing=grid_spacing,
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
