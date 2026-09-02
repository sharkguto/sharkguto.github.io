#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flet as ft

from theme import COLORS, get_responsive_font_size, get_responsive_padding, get_responsive_spacing, get_shadow
from utils.responsive import Breakpoint, ResponsiveConfig


def portfolio_content(page: ft.Page):
    width = page.width if page.width else 1024
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    is_mobile = breakpoint == Breakpoint.MOBILE

    projects = [
        {
            "title": "Velejar Fácil",
            "description": "Plataforma web em desenvolvimento para gestão de embarcações, reservas e jornadas de atendimento. A solução utiliza React, Node.js, PostgreSQL, WebSockets e infraestrutura Cloudflare.",
            "image": "/velejar_facil.png",
            "technologies": ["React", "Node.js", "Cloudflare", "PostgreSQL", "WebSockets"],
            "metric": "Produto",
            "accent": COLORS["accent"],
            "url": "https://www.velejarfacil.com.br/",
        },
        {
            "title": "Monitoramento de Cotações",
            "description": "Aplicação demonstrativa para consulta de câmbio e ações, com histórico, volume e gráficos interativos. O projeto valida integração de APIs, processamento em Python e visualização no navegador.",
            "image": "/chart-project.jpg",
            "technologies": ["Python", "PyECharts", "Flet", "ScyllaDB", "Docker"],
            "metric": "Dados",
            "accent": COLORS["coral"],
        },
        {
            "title": "Website GMF-tech",
            "description": "Site institucional da GMF-tech desenvolvido em Flet e WebAssembly, com build estático, testes automatizados e validação em navegador.",
            "image": "/website-project.jpg",
            "technologies": ["Flet", "WebAssembly", "Pyodide", "Nginx", "Playwright"],
            "metric": "Web",
            "accent": COLORS["accent_alt"],
        },
    ]

    title_size = get_responsive_font_size(42, width)
    subtitle_size = get_responsive_font_size(18, width)
    card_title_size = get_responsive_font_size(24, width)
    description_size = get_responsive_font_size(15, width)
    tech_tag_size = get_responsive_font_size(13, width)
    tag_padding = get_responsive_padding(8, width)
    horizontal_padding = get_responsive_padding(48, width)
    card_padding = get_responsive_padding(24, width)
    spacing = get_responsive_spacing(18, width)

    if is_mobile:
        image_width = max((page.width or 400) - 80, 260)
        image_height = 200
    elif breakpoint == Breakpoint.TABLET:
        image_width = 330
        image_height = 220
    else:
        image_width = 390
        image_height = 250

    def create_tag(tech):
        return ft.Container(
            content=ft.Text(tech, size=tech_tag_size, color=COLORS["primary"], weight="w500"),
            bgcolor=COLORS["surface_alt"],
            padding=ft.Padding.symmetric(horizontal=tag_padding + 2, vertical=tag_padding),
            border_radius=ft.BorderRadius.all(4),
            border=ft.Border.all(1, COLORS["muted"]),
        )

    def create_project_card(project):
        project_url = project.get("url")
        return ft.Container(
            content=ft.Column(
                [
                    ft.Stack(
                        [
                            ft.Image(
                                src=project["image"],
                                fit=ft.BoxFit.COVER,
                                width=image_width,
                                height=image_height,
                                border_radius=ft.BorderRadius.all(8),
                            ),
                            ft.Container(
                                content=ft.Text(project["metric"], size=get_responsive_font_size(12, width), weight="bold", color=ft.Colors.WHITE),
                                bgcolor=project["accent"],
                                padding=ft.Padding.symmetric(horizontal=10, vertical=6),
                                border_radius=ft.BorderRadius.all(4),
                                right=12,
                                top=12,
                            ),
                        ]
                    ),
                    ft.Row(
                        [
                            ft.Text(
                                project["title"],
                                size=card_title_size,
                                weight="bold",
                                color=COLORS["text_primary"],
                                expand=True,
                            ),
                            *(
                                [
                                    ft.Icon(
                                        ft.Icons.OPEN_IN_NEW,
                                        size=get_responsive_font_size(20, width),
                                        color=COLORS["secondary"],
                                    )
                                ]
                                if project_url
                                else []
                            ),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Text(project["description"], size=description_size, color=COLORS["text_secondary"]),
                    ft.Row(
                        [create_tag(tech) for tech in project["technologies"]],
                        wrap=True,
                        spacing=8,
                        run_spacing=8,
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                spacing=spacing,
            ),
            bgcolor=COLORS["surface"],
            padding=ft.Padding.all(card_padding),
            border_radius=ft.BorderRadius.all(8),
            border=ft.Border.all(1, COLORS["muted"]),
            shadow=get_shadow(),
            url=project_url,
            ink=bool(project_url),
            tooltip=f"Abrir {project['title']}" if project_url else None,
        )

    hero = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Portfólio", size=get_responsive_font_size(15, width), color=COLORS["accent"], weight="bold"),
                            ft.Text("Projetos selecionados de software e produtos digitais", size=title_size, weight="bold", color=ft.Colors.WHITE),
                            ft.Text(
                                "Uma seleção de trabalhos que demonstra capacidade de atuar em produto, desenvolvimento web, integração de dados e engenharia de plataforma.",
                                size=subtitle_size,
                                color=ft.Colors.WHITE_70,
                            ),
                        ],
                        spacing=spacing,
                    ),
                    col={"sm": 12, "md": 8, "lg": 8},
                ),
                ft.Container(
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Image(src="/favicon.png", width=64, height=64, fit=ft.BoxFit.CONTAIN),
                                ft.Text("Competências aplicadas", size=get_responsive_font_size(22, width), weight="bold", color=ft.Colors.WHITE),
                                ft.Text("Arquitetura, interfaces, integrações, dados, qualidade e implantação.", size=get_responsive_font_size(14, width), color=ft.Colors.WHITE_70, text_align="center"),
                            ],
                            horizontal_alignment="center",
                            spacing=10,
                        ),
                        padding=ft.Padding.all(24),
                        bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE),
                        border=ft.Border.all(1, ft.Colors.with_opacity(0.18, ft.Colors.WHITE)),
                        border_radius=ft.BorderRadius.all(8),
                    ),
                    col={"sm": 12, "md": 4, "lg": 4},
                    alignment=ft.Alignment.CENTER,
                ),
            ],
            spacing=24,
            run_spacing=24,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=COLORS["primary"],
        padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(52, width)),
        width=width,
    )

    projects_section = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=create_project_card(project),
                    col={"sm": 12, "md": 6, "lg": 4},
                    padding=8,
                )
                for project in projects
            ],
            spacing=8,
            run_spacing=16,
        ),
        padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(42, width)),
        bgcolor=COLORS["background"],
        width=width,
    )

    proof_section = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Engenharia orientada ao contexto de cada negócio", size=get_responsive_font_size(30, width), weight="bold", color=COLORS["text_primary"]),
                            ft.Text("Cada projeto combina requisitos, tecnologia e operação de acordo com os objetivos, as restrições e o estágio do produto.", size=subtitle_size, color=COLORS["text_secondary"]),
                        ],
                        spacing=12,
                    ),
                    col={"sm": 12, "md": 6, "lg": 6},
                ),
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Column([ft.Text("Escopo", size=get_responsive_font_size(24, width), weight="bold", color=COLORS["coral"]), ft.Text("requisitos e critérios de aceite", size=description_size, color=COLORS["text_secondary"])], spacing=2),
                            ft.Column([ft.Text("Entrega", size=get_responsive_font_size(24, width), weight="bold", color=COLORS["secondary"]), ft.Text("produto, software e integrações", size=description_size, color=COLORS["text_secondary"])], spacing=2),
                            ft.Column([ft.Text("Operação", size=get_responsive_font_size(24, width), weight="bold", color=COLORS["accent_alt"]), ft.Text("cloud, segurança e evolução", size=description_size, color=COLORS["text_secondary"])], spacing=2),
                        ],
                        wrap=True,
                        spacing=get_responsive_spacing(28, width),
                    ),
                    col={"sm": 12, "md": 6, "lg": 6},
                    alignment=ft.Alignment.CENTER,
                ),
            ],
            spacing=24,
            run_spacing=24,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(38, width)),
        bgcolor=COLORS["surface_alt"],
        width=width,
    )

    return ft.Container(
        content=ft.Column(
            [hero, projects_section, proof_section],
            spacing=0,
        ),
        bgcolor=COLORS["background"],
        width=width,
    )
