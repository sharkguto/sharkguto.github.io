import flet as ft
from theme import COLORS, get_text_style, get_button_style


def home_content(page: ft.Page):
    return ft.Column(
        [
            ft.Text(
                "Bem-vindo à GMF-tech",
                style=get_text_style(32, weight="bold"),
                text_align="center",
            ),
            ft.Text(
                "Sua parceira em soluções de TI",
                style=get_text_style(24, COLORS["text_secondary"]),
                text_align="center",
            ),
            ft.ElevatedButton(
                "Entre em Contato",
                on_click=lambda e: page.go("/contact"),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                    padding=ft.padding.symmetric(horizontal=30, vertical=15),
                    overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
                ),
                bgcolor=COLORS["secondary"],
                color=ft.Colors.WHITE,
            ),
        ],
        horizontal_alignment="center",
        alignment="center",
        spacing=20,
    )
