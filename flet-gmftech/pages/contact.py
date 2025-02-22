#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# xpto.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :
import flet as ft


def send_email(name, email, message):
    print(name, email, message)
    return True, "Enviado com sucesso"


def contact_content(page):
    primary_color = ft.Colors.INDIGO_700
    secondary_color = ft.Colors.AMBER_600

    # Campos do formulário
    name_field = ft.TextField(
        label="Nome",
        width=300,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        border_radius=8,
    )
    email_field = ft.TextField(
        label="E-mail",
        width=300,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        border_radius=8,
    )
    message_field = ft.TextField(
        label="Mensagem",
        width=300,
        multiline=True,
        min_lines=4,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        border_radius=8,
    )
    status_text = ft.Text("", color=ft.Colors.WHITE)

    def go_to_home(e):
        page.go("/")

    def submit_form(e):
        if not name_field.value or not email_field.value or not message_field.value:
            status_text.value = "Por favor, preencha todos os campos!"
            status_text.color = ft.Colors.RED_400
        else:
            success, message = send_email(
                name_field.value, email_field.value, message_field.value
            )
            status_text.value = message
            status_text.color = ft.Colors.GREEN_400 if success else ft.Colors.RED_400
            if success:
                name_field.value = ""
                email_field.value = ""
                message_field.value = ""
        page.update()

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Página de Contato",
                    size=48 if page.window.width > 600 else 30,
                    weight="bold",
                    color=ft.Colors.WHITE,
                    text_align="center",
                ),
                ft.Text(
                    "Entre em contato com a GMF-tech",
                    size=20 if page.window.width > 600 else 16,
                    color=ft.Colors.GREY_300,
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
                                bgcolor=secondary_color,
                                color=ft.Colors.WHITE,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=8)
                                ),
                                on_click=submit_form,
                            ),
                            status_text,
                        ],
                        spacing=15,
                        alignment="center",
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
            expand=True,
        ),
        padding=ft.padding.symmetric(
            vertical=60 if page.window.width > 600 else 30, horizontal=20
        ),
        bgcolor=primary_color,
        expand=True,
        alignment=ft.alignment.center,
    )
