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
                    "Sobre Nós",
                    size=32 if page.width > 600 else 24,
                    weight="bold",
                    color=COLORS["text_primary"],
                    text_align="center",
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Nossa História",
                                size=24 if page.width > 600 else 20,
                                weight="bold",
                                color=COLORS["text_primary"],
                            ),
                            ft.Text(
                                "A GMF-tech nasceu da paixão por tecnologia e da vontade de transformar negócios através de soluções inovadoras.",
                                size=16,
                                color=COLORS["text_secondary"],
                            ),
                            ft.Text(
                                "Nossa Missão",
                                size=24 if page.width > 600 else 20,
                                weight="bold",
                                color=COLORS["text_primary"],
                            ),
                            ft.Text(
                                "Fornecer soluções tecnológicas de alta qualidade que impulsionem o sucesso de nossos clientes.",
                                size=16,
                                color=COLORS["text_secondary"],
                            ),
                            ft.Text(
                                "Nossos Valores",
                                size=24 if page.width > 600 else 20,
                                weight="bold",
                                color=COLORS["text_primary"],
                            ),
                            ft.Text(
                                "• Inovação\n• Qualidade\n• Compromisso\n• Transparência\n• Excelência",
                                size=16,
                                color=COLORS["text_secondary"],
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
            expand=True,
            alignment="center",
            spacing=20,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 400),  # Altura mínima de 400px
        padding=ft.padding.symmetric(horizontal=40 if page.width > 600 else 20),
    )
