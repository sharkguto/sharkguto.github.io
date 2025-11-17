#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# xpto.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :
import flet as ft
from theme import COLORS, get_text_style, get_button_style, get_shadow, get_responsive_font_size, get_responsive_padding, get_responsive_spacing
from utils.responsive import ResponsiveConfig, Breakpoint


def send_email(name, email, message):
    print(name, email, message)
    return True, "Enviado com sucesso"


def contact_content(page: ft.Page):
    # Detect breakpoint for responsive layout
    breakpoint = ResponsiveConfig.get_breakpoint(page.width)
    
    # Calculate responsive values
    title_font_size = get_responsive_font_size(32, page.width)
    container_padding = get_responsive_padding(30, page.width)
    field_spacing = get_responsive_spacing(15, page.width)
    section_spacing = get_responsive_spacing(20, page.width)
    
    # Form field width: 100% on mobile, 400px on desktop
    field_width = None if breakpoint == Breakpoint.MOBILE else 400
    
    name_field = ft.TextField(
        label="Nome",
        border_color=COLORS["primary"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
        width=field_width,
        text_align="center",
    )
    email_field = ft.TextField(
        label="Email",
        border_color=COLORS["primary"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
        width=field_width,
        text_align="center",
    )
    message_field = ft.TextField(
        label="Mensagem",
        multiline=True,
        min_lines=3,
        max_lines=4,
        border_color=COLORS["primary"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
        width=field_width,
        text_align="center",
    )

    def handle_submit(e):
        if not name_field.value or not email_field.value or not message_field.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Por favor, preencha todos os campos."),
                bgcolor=COLORS["error"],
            )
            page.snack_bar.open = True
            page.update()
            return

        # Aqui você pode adicionar a lógica para enviar o email
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Mensagem enviada com sucesso!"),
            bgcolor=COLORS["success"],
        )
        page.snack_bar.open = True
        name_field.value = ""
        email_field.value = ""
        message_field.value = ""
        page.update()

    return ft.Container(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Entre em Contato",
                        size=title_font_size,
                        weight="bold",
                        color=COLORS["text_primary"],
                        text_align="center",
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                name_field,
                                email_field,
                                message_field,
                                ft.Container(
                                    content=ft.ElevatedButton(
                                        "Enviar Mensagem",
                                        style=get_button_style(),
                                        on_click=handle_submit,
                                    ),
                                    alignment=ft.alignment.center,
                                ),
                            ],
                            horizontal_alignment="center",
                            alignment="center",
                            spacing=field_spacing,
                        ),
                        padding=container_padding,
                        bgcolor=COLORS["surface"],
                        border_radius=ft.border_radius.all(15),
                        shadow=get_shadow(),
                        width=500 if breakpoint != Breakpoint.MOBILE else None,
                        alignment=ft.alignment.center,
                    ),
                ],
                horizontal_alignment="center",
                alignment="center",
                spacing=section_spacing,
            ),
            alignment=ft.alignment.center,
            expand=True,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 350),
        alignment=ft.alignment.center,
    )
