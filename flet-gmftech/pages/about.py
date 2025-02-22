#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# about.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft


def about_content(page):
    primary_color = ft.Colors.INDIGO_700  # Usado para texto ou detalhes, não fundo
    secondary_color = ft.Colors.AMBER_600

    def go_to_home(e):
        page.go("/")

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Página Sobre",
                    size=48 if page.window.width > 600 else 30,
                    weight="bold",
                    color=primary_color,  # Texto em azul escuro
                    text_align="center",
                ),
                ft.Text(
                    "Saiba mais sobre a GMF-tech",
                    size=20 if page.window.width > 600 else 16,
                    color=ft.Colors.GREY_700,  # Cinza escuro para contraste no fundo branco
                    text_align="center",
                ),
                ft.Container(
                    content=ft.Text(
                        "Somos uma empresa especializada em soluções de TI sob medida, "
                        "focada em outsourcing e aceleração de negócios através da tecnologia.",
                        size=16 if page.window.width > 600 else 14,
                        color=ft.Colors.BLACK,
                        text_align="center",
                    ),
                    padding=20,
                ),
                ft.ElevatedButton(
                    "Voltar para Home",
                    bgcolor=secondary_color,
                    color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                    on_click=go_to_home,
                ),
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20 if page.window.width > 600 else 10,
            expand=True,  # Preenche o Container internamente
        ),
        padding=ft.padding.symmetric(
            vertical=60 if page.window.width > 600 else 30, horizontal=20
        ),
        bgcolor=ft.Colors.WHITE,  # Fundo branco conforme solicitado
        expand=True,  # Preenche o espaço disponível no layout pai
        alignment=ft.alignment.center,
    )
