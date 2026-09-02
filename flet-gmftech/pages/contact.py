#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.parse import quote

import flet as ft

from theme import (
    COLORS,
    get_button_style,
    get_responsive_font_size,
    get_responsive_padding,
    get_responsive_spacing,
    get_shadow,
)
from utils.responsive import Breakpoint, ResponsiveConfig


def build_mailto_url(name: str, email: str, message: str) -> str:
    subject = quote("Contato pelo site GMF-tech")
    body = quote(
        f"Nome: {name}\n"
        f"Email: {email}\n\n"
        f"Contexto do projeto:\n{message}"
    )
    return f"mailto:contato@gmf-tech.com?subject={subject}&body={body}"


def contact_content(page: ft.Page):
    width = page.width if page.width else 1024
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    is_mobile = breakpoint == Breakpoint.MOBILE

    title_font_size = get_responsive_font_size(42, width)
    section_title_size = get_responsive_font_size(28, width)
    body_size = get_responsive_font_size(16, width)
    container_padding = get_responsive_padding(36, width)
    field_spacing = get_responsive_spacing(15, width)
    section_spacing = get_responsive_spacing(24, width)
    horizontal_padding = get_responsive_padding(48, width)
    field_width = None if is_mobile else 440

    name_field = ft.TextField(
        label="Nome",
        hint_text="Nome e sobrenome",
        border_color=COLORS["muted"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
        width=field_width,
    )
    email_field = ft.TextField(
        label="E-mail",
        hint_text="seu.email@empresa.com",
        border_color=COLORS["muted"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
        width=field_width,
    )
    message_field = ft.TextField(
        label="Contexto do projeto",
        hint_text="Descreva o objetivo, o contexto atual, os sistemas envolvidos e o prazo esperado.",
        multiline=True,
        min_lines=5,
        max_lines=6,
        border_color=COLORS["muted"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
        width=field_width,
    )

    def show_snack_bar(snack_bar: ft.SnackBar):
        page.snack_bar = snack_bar
        snack_bar.open = True
        if hasattr(page, "show_dialog"):
            try:
                page.show_dialog(snack_bar)
                page.update()
                return
            except Exception:
                pass
        page.update()

    def handle_submit(e):
        if not name_field.value or not email_field.value or not message_field.value:
            show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Preencha todos os campos para continuar."),
                    bgcolor=COLORS["error"],
                )
            )
            return

        page.launch_url(build_mailto_url(name_field.value, email_field.value, message_field.value))
        show_snack_bar(
            ft.SnackBar(
                content=ft.Text("Seu aplicativo de e-mail foi aberto para concluir o contato."),
                bgcolor=COLORS["success"],
            )
        )

    def prompt_card(icon, title, text, color):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(icon, color=color, size=get_responsive_font_size(24, width)),
                        bgcolor=ft.Colors.with_opacity(0.1, color),
                        padding=ft.Padding.all(10),
                        border_radius=ft.BorderRadius.all(8),
                    ),
                    ft.Column(
                        [
                            ft.Text(title, size=get_responsive_font_size(17, width), weight="bold", color=COLORS["text_primary"]),
                            ft.Text(text, size=get_responsive_font_size(14, width), color=COLORS["text_secondary"]),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=ft.Padding.all(get_responsive_padding(16, width)),
            bgcolor=COLORS["surface"],
            border=ft.Border.all(1, COLORS["muted"]),
            border_radius=ft.BorderRadius.all(8),
        )

    submit_button = ft.Button(
        "Continuar por e-mail",
        icon=ft.Icons.EMAIL,
        style=get_button_style(),
        bgcolor=COLORS["coral"],
        color=ft.Colors.WHITE,
        on_click=handle_submit,
    )

    form_card = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Image(src="/favicon.png", width=44, height=44, fit=ft.BoxFit.CONTAIN),
                        ft.Column(
                            [
                                ft.Text("Informações iniciais do projeto", size=section_title_size, weight="bold", color=COLORS["text_primary"]),
                                ft.Text("Compartilhe o contexto necessário para uma primeira análise.", size=body_size, color=COLORS["text_secondary"]),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                    ],
                    spacing=14,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                name_field,
                email_field,
                message_field,
                ft.Container(content=submit_button, alignment=ft.Alignment.CENTER_LEFT),
            ],
            spacing=field_spacing,
        ),
        padding=ft.Padding.all(container_padding),
        bgcolor=COLORS["surface"],
        border_radius=ft.BorderRadius.all(8),
        border=ft.Border.all(1, COLORS["muted"]),
        shadow=get_shadow(),
        width=None if is_mobile else 560,
    )

    hero = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Contato comercial", size=get_responsive_font_size(15, width), color=COLORS["accent"], weight="bold"),
                            ft.Text("Converse com a GMF-tech sobre seu próximo projeto", size=title_font_size, weight="bold", color=ft.Colors.WHITE),
                            ft.Text(
                                "Apresente o objetivo de negócio, o cenário atual e o resultado esperado. A equipe organiza as informações para avaliar escopo, abordagem e próximos passos.",
                                size=get_responsive_font_size(18, width),
                                color=ft.Colors.WHITE_70,
                            ),
                        ],
                        spacing=section_spacing,
                    ),
                    col={"sm": 12, "md": 6, "lg": 6},
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            prompt_card(ft.Icons.DEVICES, "Novo produto digital", "Aplicações web e mobile, portais de cliente e sistemas internos.", COLORS["secondary"]),
                            prompt_card(ft.Icons.HUB, "Modernização e integração", "Sistemas legados, APIs, dados e processos entre plataformas.", COLORS["coral"]),
                            prompt_card(ft.Icons.SETTINGS_SUGGEST, "Dados e automação", "Dashboards, pipelines, rotinas operacionais e IA quando houver justificativa.", COLORS["accent_alt"]),
                        ],
                        spacing=12,
                    ),
                    col={"sm": 12, "md": 6, "lg": 6},
                ),
            ],
            spacing=28,
            run_spacing=28,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=COLORS["primary"],
        padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(52, width)),
        width=width,
    )

    form_section = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Informações que ajudam na análise", size=section_title_size, weight="bold", color=COLORS["text_primary"]),
                            ft.Text("Objetivo de negócio, usuários envolvidos, sistemas atuais, integrações necessárias, restrições, prazo e critérios de sucesso.", size=body_size, color=COLORS["text_secondary"]),
                        ],
                        spacing=14,
                    ),
                    col={"sm": 12, "md": 5, "lg": 5},
                ),
                ft.Container(
                    content=form_card,
                    col={"sm": 12, "md": 7, "lg": 7},
                    alignment=ft.Alignment.CENTER,
                ),
            ],
            spacing=28,
            run_spacing=28,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(46, width)),
        bgcolor=COLORS["background"],
        width=width,
    )

    return ft.Container(
        content=ft.Column(
            [hero, form_section],
            spacing=0,
        ),
        bgcolor=COLORS["background"],
        width=width,
    )
