import flet as ft
from theme import COLORS, get_text_style, get_button_style, get_shadow


def home_content(page: ft.Page):
    return ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                "Bem-vindo à GMF-tech",
                                size=48 if page.width > 600 else 32,
                                weight="bold",
                                color=COLORS["text_primary"],
                                text_align="center",
                            ),
                            ft.Text(
                                "Sua parceira em soluções de TI",
                                size=32 if page.width > 600 else 24,
                                color=COLORS["text_secondary"],
                                text_align="center",
                            ),
                            ft.Container(
                                content=ft.ElevatedButton(
                                    "Entre em Contato",
                                    style=get_button_style(),
                                    on_click=lambda e: page.go("/contact"),
                                ),
                                padding=ft.padding.only(top=40 if page.width > 600 else 30),
                            ),
                        ],
                        horizontal_alignment="center",
                        alignment="center",
                        spacing=20,
                    ),
                    expand=True,
                    alignment=ft.alignment.center,
                ),
            ],
            expand=True,
            alignment="center",
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 400),  # Altura mínima de 400px
        padding=ft.padding.symmetric(horizontal=40 if page.width > 600 else 20),
    )
