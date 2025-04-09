#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# about.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from theme import COLORS, get_text_style, get_button_style, get_shadow


def about_content(page: ft.Page):
    def go_to_home(e):
        page.go("/")

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Sobre a GMF-tech",
                    style=get_text_style(32, weight="bold"),
                    text_align="center",
                ),
                ft.Text(
                    "Nossa história e missão",
                    style=get_text_style(16, COLORS["text_secondary"]),
                    text_align="center",
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "A GMF-tech é uma empresa especializada em soluções de TI, focada em fornecer serviços de alta qualidade para nossos clientes.",
                                style=get_text_style(16),
                                text_align="center",
                            ),
                            ft.Text(
                                "Nossa missão é ajudar empresas a alcançarem seu potencial máximo através da tecnologia, oferecendo soluções personalizadas e suporte excepcional.",
                                style=get_text_style(16),
                                text_align="center",
                            ),
                        ],
                        spacing=20,
                    ),
                    padding=20,
                    bgcolor=COLORS["surface"],
                    border_radius=ft.border_radius.all(15),
                    shadow=get_shadow(),
                ),
                ft.ElevatedButton(
                    "Voltar para Home",
                    bgcolor=COLORS["secondary"],
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        padding=ft.padding.symmetric(horizontal=30, vertical=15),
                        overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
                    ),
                    on_click=go_to_home,
                ),
            ],
            horizontal_alignment="center",
            alignment="center",
            spacing=20,
        ),
        padding=20,
        bgcolor=COLORS["surface"],
        expand=True,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(15),
    )
