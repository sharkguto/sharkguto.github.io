#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# theme.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from utils.responsive import ResponsiveConfig

# Paleta de cores moderna
COLORS = {
    "primary": "#1a237e",  # Azul escuro
    "secondary": "#0d47a1",  # Azul médio
    "accent": "#1e88e5",  # Azul claro
    "error": "#d32f2f",  # Vermelho
    "warning": "#ffa000",  # Laranja
    "success": "#388e3c",  # Verde
    "background": "#f5f5f5",  # Cinza muito claro
    "surface": "#ffffff",  # Branco
    "text_primary": "#212121",  # Cinza muito escuro
    "text_secondary": "#757575",  # Cinza médio
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
        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
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
        color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
        offset=ft.Offset(0, 0),
    )

# Responsive helper functions
def get_responsive_font_size(base_size: int, width: int) -> int:
    """
    Calculate responsive font size based on screen width.
    
    Args:
        base_size: Base font size in pixels
        width: Screen width in pixels
        
    Returns:
        Scaled font size as integer
    """
    if width is None or width <= 0:
        width = 1024  # Default to desktop width
    
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    return ResponsiveConfig.get_font_size(base_size, breakpoint)


def get_responsive_padding(base_padding: int, width: int) -> int:
    """
    Calculate responsive padding based on screen width.
    
    Args:
        base_padding: Base padding in pixels
        width: Screen width in pixels
        
    Returns:
        Scaled padding as integer
    """
    if width is None or width <= 0:
        width = 1024  # Default to desktop width
    
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    return ResponsiveConfig.get_spacing(base_padding, breakpoint)


def get_responsive_spacing(base_spacing: int, width: int) -> int:
    """
    Calculate responsive spacing based on screen width.
    
    Args:
        base_spacing: Base spacing in pixels
        width: Screen width in pixels
        
    Returns:
        Scaled spacing as integer
    """
    if width is None or width <= 0:
        width = 1024  # Default to desktop width
    
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    return ResponsiveConfig.get_spacing(base_spacing, breakpoint) 