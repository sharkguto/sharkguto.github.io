#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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


def send_email(name, email, message):
    print(name, email, message)
    return True, "Diagnostico recebido com sucesso"


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
        hint_text="Como posso te chamar?",
        border_color=COLORS["muted"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
        width=field_width,
    )
    email_field = ft.TextField(
        label="Email",
        hint_text="seu.email@empresa.com",
        border_color=COLORS["muted"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
        width=field_width,
    )
    message_field = ft.TextField(
        label="Mensagem",
        hint_text="Conte o que voce quer construir, automatizar ou melhorar com IA.",
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
                    content=ft.Text("Por favor, preencha todos os campos."),
                    bgcolor=COLORS["error"],
                )
            )
            return

        success, feedback = send_email(name_field.value, email_field.value, message_field.value)
        if not success:
            show_snack_bar(ft.SnackBar(content=ft.Text(feedback), bgcolor=COLORS["error"]))
            return

        show_snack_bar(
            ft.SnackBar(
                content=ft.Text("Diagnostico recebido com sucesso!"),
                bgcolor=COLORS["success"],
            )
        )
        name_field.value = ""
        email_field.value = ""
        message_field.value = ""
        page.update()

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
        "Enviar diagnostico",
        icon=ft.Icons.TASK_ALT,
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
                                ft.Text("Vamos mapear sua proxima entrega", size=section_title_size, weight="bold", color=COLORS["text_primary"]),
                                ft.Text("Flet, Python, dados, automacao e IA aplicada ao seu processo.", size=body_size, color=COLORS["text_secondary"]),
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
                            ft.Text("Contato", size=get_responsive_font_size(15, width), color=COLORS["accent"], weight="bold"),
                            ft.Text("Agende um diagnostico para Flet, IA e automacao", size=title_font_size, weight="bold", color=ft.Colors.WHITE),
                            ft.Text(
                                "Traga uma ideia, um processo manual ou um sistema que precisa evoluir. A GMF-tech transforma isso em plano tecnico e primeira entrega navegavel.",
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
                            prompt_card(ft.Icons.DEVICES, "Projeto Flet", "Apps web, desktop, mobile, dashboards e sistemas internos.", COLORS["secondary"]),
                            prompt_card(ft.Icons.SMART_TOY, "Consultoria de IA", "Copilots, agentes, classificacao, extracao e atendimento inteligente.", COLORS["coral"]),
                            prompt_card(ft.Icons.HUB, "Automacao", "Integre APIs, documentos, planilhas, CRM, backoffice e rotinas repetitivas.", COLORS["accent_alt"]),
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
                            ft.Text("O que pode entrar no diagnostico", size=section_title_size, weight="bold", color=COLORS["text_primary"]),
                            ft.Text("Modernizacao de sistemas, MVPs em Flet, bots internos, automacoes com IA, dashboards, pipelines de dados, cloud e deploy em GitHub Pages.", size=body_size, color=COLORS["text_secondary"]),
                            ft.Text("Resposta simulada nesta versao: o formulario valida os campos e prepara o fluxo para integracao futura.", size=get_responsive_font_size(14, width), color=COLORS["text_secondary"]),
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
