#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# theme.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft

# Paleta de cores moderna
COLORS = {
    "primary": "#1a237e",  # Indigo 900
    "secondary": "#ffa000",  # Amber 700
    "background": "#f5f5f5",  # Grey 100
    "surface": "#ffffff",  # White
    "text_primary": "#212121",  # Grey 900
    "text_secondary": "#757575",  # Grey 600
    "accent": "#2196f3",  # Blue 500
    "error": "#f44336",  # Red 500
    "success": "#4caf50",  # Green 500
}

# Configurações de tema
def get_theme():
    return ft.Theme(
        font_family="Roboto",
        color_scheme=ft.ColorScheme(
            primary=COLORS["primary"],
            secondary=COLORS["secondary"],
            surface=COLORS["surface"],
            background=COLORS["background"],
        ),
    )

# Estilo de botão padrão
def get_button_style():
    return ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=8),
        padding=ft.padding.symmetric(horizontal=30, vertical=15),
        overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
    )

# Estilo de texto padrão
def get_text_style(size=16, color=None, weight=None):
    return ft.TextStyle(
        font_family="Roboto",
        color=color or COLORS["text_primary"],
        size=size,
        weight=weight,
    )

# Sombra padrão
def get_shadow():
    return ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.with_opacity(0.1, ft.Colors.BLACK),
        offset=ft.Offset(0, 0),
    ) 