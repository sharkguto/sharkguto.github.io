#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# xpto.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :
import flet as ft
from theme import COLORS, get_text_style, get_button_style, get_shadow


def send_email(name, email, message):
    print(name, email, message)
    return True, "Enviado com sucesso"


def contact_content(page: ft.Page):
    name_field = ft.TextField(
        label="Nome",
        border_color=COLORS["primary"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
    )
    email_field = ft.TextField(
        label="Email",
        border_color=COLORS["primary"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
    )
    message_field = ft.TextField(
        label="Mensagem",
        multiline=True,
        min_lines=3,
        max_lines=5,
        border_color=COLORS["primary"],
        focused_border_color=COLORS["secondary"],
        cursor_color=COLORS["secondary"],
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
        content=ft.Column(
            [
                ft.Text(
                    "Entre em Contato",
                    size=32 if page.width > 600 else 24,
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
                            ft.ElevatedButton(
                                "Enviar Mensagem",
                                style=get_button_style(),
                                on_click=handle_submit,
                            ),
                        ],
                        spacing=20,
                    ),
                    padding=20,
                    bgcolor=COLORS["surface"],
                    border_radius=ft.border_radius.all(15),
                    shadow=get_shadow(),
                    width=400 if page.width > 600 else None,
                ),
            ],
            expand=True,
            alignment="center",
            spacing=20,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 400),  # Altura mínima de 400px
        padding=ft.padding.symmetric(horizontal=40 if page.width > 600 else 20),
    )
