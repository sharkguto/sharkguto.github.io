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
    def send_message(e):
        if not name.value or not email.value or not message.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    "Por favor, preencha todos os campos",
                    style=get_text_style(16, ft.Colors.WHITE),
                ),
                bgcolor=COLORS["error"],
            )
            page.snack_bar.open = True
            page.update()
            return

        # Simulação de envio de mensagem
        page.snack_bar = ft.SnackBar(
            content=ft.Text(
                "Mensagem enviada com sucesso!",
                style=get_text_style(16, ft.Colors.WHITE),
            ),
            bgcolor=COLORS["success"],
        )
        page.snack_bar.open = True
        page.update()

        # Limpar campos
        name.value = ""
        email.value = ""
        message.value = ""
        page.update()

    name = ft.TextField(
        label="Nome",
        hint_text="Seu nome completo",
        border_radius=8,
        border_color=COLORS["primary"],
        label_style=get_text_style(16),
        text_style=get_text_style(16),
    )

    email = ft.TextField(
        label="Email",
        hint_text="seu@email.com",
        border_radius=8,
        border_color=COLORS["primary"],
        label_style=get_text_style(16),
        text_style=get_text_style(16),
    )

    message = ft.TextField(
        label="Mensagem",
        hint_text="Como podemos ajudar?",
        border_radius=8,
        border_color=COLORS["primary"],
        multiline=True,
        min_lines=5,
        max_lines=5,
        label_style=get_text_style(16),
        text_style=get_text_style(16),
    )

    return ft.Container(
        content=ft.ListView(
            [
                ft.Column(
                    [
                        ft.Text(
                            "Entre em Contato",
                            style=get_text_style(32 if page.width > 600 else 24, weight="bold"),
                            text_align="center",
                        ),
                        ft.Text(
                            "Preencha o formulário abaixo e entraremos em contato em breve",
                            style=get_text_style(16, COLORS["text_secondary"]),
                            text_align="center",
                        ),
                        ft.Container(
                            content=ft.Column(
                                [name, email, message],
                                spacing=20,
                            ),
                            padding=20,
                            bgcolor=COLORS["surface"],
                            border_radius=ft.border_radius.all(15),
                            shadow=get_shadow(),
                        ),
                        ft.ElevatedButton(
                            "Enviar Mensagem",
                            on_click=send_message,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8),
                                padding=ft.padding.symmetric(
                                    horizontal=30 if page.width > 600 else 20,
                                    vertical=15 if page.width > 600 else 10
                                ),
                                overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
                            ),
                            bgcolor=COLORS["primary"],
                            color=ft.Colors.WHITE,
                        ),
                    ],
                    horizontal_alignment="center",
                    alignment="center",
                    spacing=20 if page.width > 600 else 15,
                ),
            ],
            expand=True,
            spacing=20,
            padding=ft.padding.symmetric(
                horizontal=40 if page.width > 600 else 20,
                vertical=20
            ),
        ),
        expand=True,
    )
