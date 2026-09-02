#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flet as ft

from theme import COLORS, get_responsive_font_size, get_responsive_padding, get_responsive_spacing, get_shadow


def about_content(page: ft.Page):
    width = page.width if page.width else 1024
    title_size = get_responsive_font_size(38, width)
    section_title_size = get_responsive_font_size(24, width)
    body_text_size = get_responsive_font_size(16, width)
    padding = get_responsive_padding(44, width)
    spacing = get_responsive_spacing(20, width)

    def value_card(icon, title, text, color):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(icon, size=get_responsive_font_size(32, width), color=color),
                    ft.Text(title, size=section_title_size, weight="bold", color=COLORS["text_primary"]),
                    ft.Text(text, size=body_text_size, color=COLORS["text_secondary"]),
                ],
                spacing=10,
            ),
            padding=ft.Padding.all(get_responsive_padding(24, width)),
            bgcolor=COLORS["surface"],
            border_radius=ft.BorderRadius.all(8),
            border=ft.Border.all(1, COLORS["muted"]),
            shadow=get_shadow(),
        )

    return ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.Text("Sobre a GMF-tech", size=get_responsive_font_size(15, width), color=COLORS["accent"], weight="bold"),
                                        ft.Text("Fábrica de software para empresas que precisam transformar processos em sistemas confiáveis.", size=title_size, weight="bold", color=ft.Colors.WHITE),
                                        ft.Text(
                                            "A GMF-tech planeja, desenvolve e mantém soluções sob medida, reunindo produto, arquitetura, desenvolvimento, dados e infraestrutura.",
                                            size=body_text_size,
                                            color=ft.Colors.WHITE_70,
                                        ),
                                    ],
                                    spacing=spacing,
                                ),
                                col={"sm": 12, "md": 7, "lg": 7},
                            ),
                            ft.Container(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Image(src="/favicon.png", width=82, height=82, fit=ft.BoxFit.CONTAIN),
                                            ft.Text("Identidade GMF-tech", size=section_title_size, weight="bold", color=ft.Colors.WHITE),
                                            ft.Text("Engenharia de software com direção técnica, transparência e responsabilidade sobre a entrega.", size=body_text_size, color=ft.Colors.WHITE_70, text_align="center"),
                                        ],
                                        horizontal_alignment="center",
                                        spacing=12,
                                    ),
                                    bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE),
                                    padding=ft.Padding.all(28),
                                    border=ft.Border.all(1, ft.Colors.with_opacity(0.18, ft.Colors.WHITE)),
                                    border_radius=ft.BorderRadius.all(8),
                                ),
                                col={"sm": 12, "md": 5, "lg": 5},
                                alignment=ft.Alignment.CENTER,
                            ),
                        ],
                        spacing=24,
                        run_spacing=24,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    bgcolor=COLORS["primary"],
                    padding=ft.Padding.symmetric(horizontal=padding, vertical=get_responsive_padding(54, width)),
                    width=width,
                ),
                ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Container(content=value_card(ft.Icons.FACT_CHECK, "Consultoria e discovery", "Levantamento de objetivos, processos, requisitos e riscos para estruturar o escopo do projeto.", COLORS["coral"]), col={"sm": 12, "md": 4, "lg": 4}),
                            ft.Container(content=value_card(ft.Icons.DEVICES, "Desenvolvimento sob medida", "Aplicações web e mobile, sistemas internos, APIs e integrações alinhados à operação da empresa.", COLORS["secondary"]), col={"sm": 12, "md": 4, "lg": 4}),
                            ft.Container(content=value_card(ft.Icons.CLOUD_DONE, "Entrega e operação", "Testes, documentação, infraestrutura, implantação e acompanhamento da evolução do sistema.", COLORS["accent_alt"]), col={"sm": 12, "md": 4, "lg": 4}),
                        ],
                        spacing=16,
                        run_spacing=16,
                    ),
                    padding=ft.Padding.symmetric(horizontal=padding, vertical=get_responsive_padding(36, width)),
                    width=width,
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Como conduzimos cada projeto", size=title_size, weight="bold", color=COLORS["text_primary"], text_align="center"),
                            ft.ResponsiveRow(
                                [
                                    ft.Container(content=value_card(ft.Icons.FACT_CHECK, "1. Descoberta e escopo", "Objetivos, requisitos, dependências, riscos e critérios de aceite são consolidados para orientar a execução.", COLORS["secondary"]), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=value_card(ft.Icons.ROUTE, "2. Engenharia e validação", "Arquitetura, protótipos, implementação e testes evoluem em entregas priorizadas e verificáveis.", COLORS["coral"]), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=value_card(ft.Icons.SPEED, "3. Implantação e evolução", "Deploy, documentação, monitoramento e backlog de melhorias sustentam a operação após a entrega.", COLORS["accent_alt"]), col={"sm": 12, "md": 4, "lg": 4}),
                                ],
                                spacing=16,
                                run_spacing=16,
                            ),
                        ],
                        spacing=get_responsive_spacing(28, width),
                    ),
                    bgcolor=COLORS["surface_alt"],
                    padding=ft.Padding.symmetric(horizontal=padding, vertical=get_responsive_padding(42, width)),
                    width=width,
                ),
            ],
            spacing=0,
        ),
        bgcolor=COLORS["background"],
        width=width,
    )
