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
                                            "A GMF-tech combina engenharia Python, Flet, WebAssembly, cloud e IA aplicada para construir sistemas úteis, bonitos e fáceis de evoluir.",
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
                            ft.Container(content=value_card(ft.Icons.PSYCHOLOGY, "Consultoria sem enrolação", "Mapeio gargalos, priorizo ganhos rápidos e traduzo tecnologia em decisão de negócio.", COLORS["coral"]), col={"sm": 12, "md": 4, "lg": 4}),
                            ft.Container(content=value_card(ft.Icons.DEVICES, "Flet como especialidade", "Interfaces ricas em Python, prontas para web, desktop, mobile e deploy estático.", COLORS["secondary"]), col={"sm": 12, "md": 4, "lg": 4}),
                            ft.Container(content=value_card(ft.Icons.AUTO_AWESOME, "IA para operação real", "Copilots, agentes, triagem, extração, automação e integração com sistemas existentes.", COLORS["accent_alt"]), col={"sm": 12, "md": 4, "lg": 4}),
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
                                    ft.Container(content=value_card(ft.Icons.FACT_CHECK, "1. Diagnóstico", "Entendimento de processos, dados, riscos, ferramentas e oportunidades de automação.", COLORS["secondary"]), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=value_card(ft.Icons.ROUTE, "2. Protótipo", "Fluxo navegável em Flet, com integrações e dados suficientes para validar valor.", COLORS["coral"]), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=value_card(ft.Icons.SPEED, "3. Produção", "Deploy, monitoramento, testes, documentação e evolução incremental.", COLORS["accent_alt"]), col={"sm": 12, "md": 4, "lg": 4}),
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
