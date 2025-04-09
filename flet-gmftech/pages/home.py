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
                                size=32 if page.width > 600 else 24,
                                weight="bold",
                                color=COLORS["text_primary"],
                                text_align="center",
                            ),
                            ft.Text(
                                "Sua parceira em soluções de TI",
                                size=24 if page.width > 600 else 18,
                                color=COLORS["text_secondary"],
                                text_align="center",
                            ),
                            ft.Container(
                                content=ft.ElevatedButton(
                                    text="Entre em Contato",
                                    style=get_button_style(),
                                    on_click=lambda e: page.go("/contact"),
                                ),
                                padding=ft.padding.only(top=20 if page.width > 600 else 15),
                            ),
                        ],
                        horizontal_alignment="center",
                        alignment="center",
                        expand=True,
                    ),
                    padding=ft.padding.symmetric(
                        horizontal=40 if page.width > 600 else 20,
                        vertical=40 if page.width > 600 else 20,
                    ),
                    bgcolor=COLORS["surface"],
                    border_radius=ft.border_radius.all(15),
                    shadow=get_shadow(),
                    expand=True,
                ),
            ],
            expand=True,
            alignment="center",
        ),
        expand=True,
    )
