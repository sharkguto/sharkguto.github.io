#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# theme.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from utils.responsive import ResponsiveConfig


# Paleta de cores da GMF-tech: azul profundo, verde oceano e acentos quentes.
COLORS = {
    "primary": "#071B2C",
    "secondary": "#0E7C7B",
    "accent": "#2DD4BF",
    "accent_alt": "#F6C85F",
    "coral": "#FF6B4A",
    "error": "#D64545",
    "warning": "#F6C85F",
    "success": "#1A936F",
    "background": "#F4F8FA",
    "surface": "#FFFFFF",
    "surface_alt": "#EAF3F5",
    "text_primary": "#10212F",
    "text_secondary": "#53656F",
    "muted": "#D8E6EA",
    "dark_surface": "#0B2536",
}

# Configurações de tema
def get_theme():
    color_scheme = ft.ColorScheme(
        primary=COLORS["primary"],
        secondary=COLORS["secondary"],
        surface=COLORS["surface"],
    )

    return ft.Theme(
        font_family="Roboto",
        color_scheme=color_scheme,
        scaffold_bgcolor=COLORS["background"],
        use_material3=True,
    )

# Estilo de botão padrão
def get_button_style():
    return ft.ButtonStyle(
        shape=ft.RoundedRectangleBorder(radius=6),
        padding=ft.Padding.symmetric(horizontal=28, vertical=14),
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
        blur_radius=24,
        color=ft.Colors.with_opacity(0.14, ft.Colors.BLACK),
        offset=ft.Offset(0, 10),
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
