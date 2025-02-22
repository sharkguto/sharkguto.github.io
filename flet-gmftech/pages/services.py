#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# services.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft


def services_content(page):
    primary_color = ft.Colors.INDIGO_700

    # Função para criar um card
    def create_card(icon, title, description):
        return ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(
                            icon,
                            size=40 if page.width > 600 else 30,
                            color=primary_color,
                        ),
                        ft.Text(
                            title, weight="bold", size=20 if page.width > 600 else 16
                        ),
                        ft.Text(
                            description,
                            size=14 if page.width > 600 else 12,
                            color=ft.Colors.GREY_700,
                        ),
                    ],
                    alignment="center",
                    spacing=10,
                ),
                padding=20,
            ),
            elevation=5,
            width=page.width * 0.8 / 3
            if page.width > 900
            else page.width * 0.8 / 2
            if page.width > 600
            else page.width * 0.8,
            margin=ft.margin.all(10),
        )

    # Lista de serviços
    services = [
        (
            "Desenvolvimento",
            ft.Icons.DEVELOPER_BOARD,
            "Equipes dedicadas para seus projetos",
        ),
        ("Suporte TI", ft.Icons.SUPPORT_AGENT, "Atendimento 24/7 para sua empresa"),
        ("Cloud AWS", ft.Icons.CLOUD, "Soluções escaláveis com Amazon Web Services"),
        ("DevOps", ft.Icons.SETTINGS, "Integração e entrega contínua para agilidade"),
        ("Ansible", ft.Icons.AUTO_FIX_HIGH, "Automação de infraestrutura simplificada"),
        ("Automação", ft.Icons.BUILD, "Processos otimizados com scripts inteligentes"),
        ("Python Backend", ft.Icons.CODE, "APIs robustas e escaláveis com Python"),
        ("Web com Flet", ft.Icons.WEB, "Aplicações web modernas e responsivas"),
        ("Mobile com Kivy", ft.Icons.PHONE_ANDROID, "Apps móveis multiplataforma"),
    ]

    # Criar os cards
    cards = [create_card(icon, title, desc) for title, icon, desc in services]

    # Conteúdo da página de serviços com rolagem
    return ft.Container(
        content=ft.ListView(
            controls=[
                ft.Column(
                    [
                        ft.Text(
                            "Nossos Serviços",
                            size=36 if page.width > 600 else 24,
                            weight="bold",
                            text_align="center",
                        ),
                        ft.ResponsiveRow(
                            controls=cards,
                            alignment="center",
                            spacing=20 if page.width > 600 else 10,
                        ),
                    ],
                    alignment="center",
                    spacing=20 if page.width > 600 else 10,
                )
            ],
            expand=True,  # Preenche o espaço disponível
        ),
        padding=ft.padding.symmetric(
            vertical=50 if page.width > 600 else 30, horizontal=20
        ),
        bgcolor=ft.Colors.WHITE,
        expand=True,
    )
