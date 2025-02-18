#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# app.py.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft


def main(page: ft.Page):
    page.title = "Tech Outsourcing Solutions"
    page.scroll = "adaptive"
    page.padding = 0

    # Cabeçalho com nome da empresa, tagline e botão de contato
    header = ft.Container(
        width=page.width,
        padding=20,
        bgcolor=ft.colors.BLUE,
        alignment=ft.alignment.center,
        content=ft.Column(
            [
                ft.Text(
                    "Tech Outsourcing Solutions",
                    size=40,
                    weight="bold",
                    color=ft.colors.WHITE,
                ),
                ft.Text(
                    "Soluções de TI que impulsionam o seu negócio",
                    size=20,
                    color=ft.colors.WHITE,
                ),
                ft.ElevatedButton(
                    "Entre em Contato",
                    bgcolor=ft.colors.WHITE,
                    color=ft.colors.BLACK,
                    on_click=lambda e: page.go("/contato"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # Seção "Sobre Nós"
    about = ft.Container(
        padding=20,
        margin=ft.margin.only(top=20),
        border_radius=10,
        bgcolor=ft.colors.WHITE,
        content=ft.Column(
            [
                ft.Text("Sobre Nós", size=30, weight="bold"),
                ft.Text(
                    "Somos uma empresa especializada em outsourcing de TI, "
                    "oferecendo soluções personalizadas para otimizar a performance "
                    "e a eficiência do seu negócio.",
                    size=16,
                ),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # Seção "Serviços"
    service_card = lambda title, description: ft.Container(
        width=250,
        padding=10,
        border_radius=10,
        bgcolor=ft.colors.LIGHT_BLUE_100,
        content=ft.Column(
            [
                ft.Text(title, weight="bold", size=18),
                ft.Text(description, size=14),
            ],
            spacing=5,
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    )

    services = ft.Container(
        padding=20,
        margin=ft.margin.only(top=20),
        content=ft.Column(
            [
                ft.Text("Nossos Serviços", size=30, weight="bold"),
                ft.Row(
                    [
                        service_card(
                            "Desenvolvimento de Software",
                            "Criação de soluções customizadas para seu negócio.",
                        ),
                        service_card(
                            "Suporte Técnico",
                            "Assistência especializada para manter sua operação ativa.",
                        ),
                        service_card(
                            "Consultoria em TI",
                            "Estratégias para otimizar e modernizar processos.",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    wrap=True,
                ),
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # Seção "Contato"
    contact = ft.Container(
        padding=20,
        margin=ft.margin.only(top=20, bottom=20),
        border_radius=10,
        bgcolor=ft.colors.GREY_100,
        content=ft.Column(
            [
                ft.Text("Entre em Contato", size=30, weight="bold"),
                ft.TextField(label="Seu nome", width=300),
                ft.TextField(label="Seu e-mail", width=300),
                ft.TextField(label="Mensagem", multiline=True, width=300, height=100),
                ft.ElevatedButton(
                    "Enviar",
                    on_click=lambda e: print("Mensagem enviada!"),
                ),
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # Organização das seções em uma única coluna (conteúdo principal)
    content = ft.Column(
        [
            header,
            about,
            services,
            contact,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(content)
    page.update()


ft.app(target=main)
