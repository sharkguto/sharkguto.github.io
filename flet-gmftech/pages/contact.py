#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# xpto.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :
import flet as ft


def contact_content(page):
    return ft.Column(
        [
            ft.Container(
                content=ft.Text(
                    "Página Contato",
                    size=30 if page.window.width > 600 else 20,
                    weight="bold",
                    color=ft.Colors.WHITE,
                    text_align="center",
                ),
                padding=20,
                bgcolor=ft.Colors.WHITE,
            ),
            ft.Container(
                content=ft.Text(
                    "Entre em contato com a GMF-tech...",
                    size=20 if page.window.width > 600 else 16,
                    color=ft.Colors.GREY_300,
                ),
                padding=20,
                bgcolor=ft.Colors.WHITE,
            ),
        ]
    )
