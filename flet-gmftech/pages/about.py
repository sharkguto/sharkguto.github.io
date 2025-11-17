#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# about.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from theme import COLORS, get_text_style, get_button_style, get_shadow, get_responsive_font_size, get_responsive_padding, get_responsive_spacing
from utils.responsive import ResponsiveConfig, Breakpoint


def about_content(page: ft.Page):
    def go_to_home(e):
        page.go("/")

    # Detect current breakpoint
    width = page.width if page.width else 1024
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    
    # Calculate responsive values
    title_size = get_responsive_font_size(32, width)
    section_title_size = get_responsive_font_size(24, width)
    body_text_size = get_responsive_font_size(16, width)
    container_padding = get_responsive_padding(30, width)
    section_spacing = get_responsive_spacing(20, width)
    inner_spacing = get_responsive_spacing(15, width)
    
    # Calculate container max-width based on breakpoint
    if breakpoint == Breakpoint.MOBILE:
        container_max_width = None  # Full width on mobile
    elif breakpoint == Breakpoint.TABLET:
        container_max_width = 700
    else:  # DESKTOP
        container_max_width = 800

    return ft.Container(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Sobre Nós",
                        size=title_size,
                        weight="bold",
                        color=COLORS["text_primary"],
                        text_align="center",
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Nossa História",
                                    size=section_title_size,
                                    weight="bold",
                                    color=COLORS["text_primary"],
                                    text_align="center",
                                ),
                                ft.Text(
                                    "A GMF-tech nasceu da paixão por tecnologia e da vontade de transformar negócios através de soluções inovadoras.",
                                    size=body_text_size,
                                    color=COLORS["text_secondary"],
                                    text_align="center",
                                ),
                                ft.Text(
                                    "Nossa Missão",
                                    size=section_title_size,
                                    weight="bold",
                                    color=COLORS["text_primary"],
                                    text_align="center",
                                ),
                                ft.Text(
                                    "Fornecer soluções tecnológicas de alta qualidade que impulsionem o sucesso de nossos clientes.",
                                    size=body_text_size,
                                    color=COLORS["text_secondary"],
                                    text_align="center",
                                ),
                                ft.Text(
                                    "Nossos Valores",
                                    size=section_title_size,
                                    weight="bold",
                                    color=COLORS["text_primary"],
                                    text_align="center",
                                ),
                                ft.Text(
                                    "• Inovação\n• Qualidade\n• Compromisso\n• Transparência\n• Excelência",
                                    size=body_text_size,
                                    color=COLORS["text_secondary"],
                                    text_align="center",
                                ),
                            ],
                            horizontal_alignment="center",
                            alignment="center",
                            spacing=inner_spacing,
                        ),
                        padding=container_padding,
                        bgcolor=COLORS["surface"],
                        border_radius=ft.border_radius.all(15),
                        shadow=get_shadow(),
                        width=container_max_width,
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
        height=max(page.height - 160 if page.height else 400, 350),  # Altura mínima menor para mobile
        alignment=ft.alignment.center,
    )
