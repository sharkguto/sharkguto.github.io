#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flet as ft

from theme import COLORS, get_responsive_font_size, get_responsive_padding, get_responsive_spacing, get_shadow
from utils.responsive import Breakpoint, ResponsiveConfig


def about_content(page: ft.Page):
    width = page.width if page.width else 1024
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    is_mobile = breakpoint == Breakpoint.MOBILE

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
                                        ft.Text("Um estúdio técnico para empresas que querem sair do slide e colocar software em produção.", size=title_size, weight="bold", color=ft.Colors.WHITE),
                                        ft.Text(
                                            "A GMF-tech combina desenvolvimento Python, DevOps, APIs, dados, cloud e IA aplicada para construir sistemas úteis, seguros e fáceis de evoluir.",
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
                                            ft.Text("Caravela digital", size=section_title_size, weight="bold", color=ft.Colors.WHITE),
                                            ft.Text("Direção, velocidade e tecnologia navegando para resultado mensurável.", size=body_text_size, color=ft.Colors.WHITE_70, text_align="center"),
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
                            ft.Container(content=value_card(ft.Icons.PSYCHOLOGY, "Consultoria sem enrolação", "Mapeio gargalos, priorizo ganhos rápidos e uso IA quando ela reduz trabalho manual de verdade.", COLORS["coral"]), col={"sm": 12, "md": 4, "lg": 4}),
                            ft.Container(content=value_card(ft.Icons.DEVICES, "Desenvolvimento Python", "APIs, automações, sistemas internos e apps em Flet (Flutter com Python) para web, celular e desktop.", COLORS["secondary"]), col={"sm": 12, "md": 4, "lg": 4}),
                            ft.Container(content=value_card(ft.Icons.AUTO_AWESOME, "DevOps para produção", "Docker, pipelines, Azure DevOps, deploys repetíveis e ambientes organizados para reduzir risco operacional.", COLORS["accent_alt"]), col={"sm": 12, "md": 4, "lg": 4}),
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
                            ft.Text("Como eu trabalho", size=title_size, weight="bold", color=COLORS["text_primary"], text_align="center"),
                            ft.ResponsiveRow(
                                [
                                    ft.Container(content=value_card(ft.Icons.FACT_CHECK, "1. Diagnóstico", "Levantamento de processos, dados, integrações, infraestrutura, dores do time, riscos técnicos e oportunidades reais de IA. A ideia é separar sintoma de causa e transformar necessidade de negócio em um plano executável.", COLORS["secondary"]), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=value_card(ft.Icons.ROUTE, "2. Protótipo", "Validação rápida com Python, FastAPI, PostgreSQL, apps em Flet (Flutter com Python), automações com IA e integrações reais quando fizer sentido. O protótipo prova fluxo, regra de negócio e valor antes de virar projeto grande.", COLORS["coral"]), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=value_card(ft.Icons.SPEED, "3. Produção", "Entrega com Docker, Azure DevOps, testes, documentação, deploy automatizado, monitoramento básico e automações com IA bem integradas. Depois disso, evolução incremental com previsibilidade e menos retrabalho.", COLORS["accent_alt"]), col={"sm": 12, "md": 4, "lg": 4}),
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
