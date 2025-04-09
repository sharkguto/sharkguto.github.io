import flet as ft
from theme import COLORS, get_text_style, get_button_style, get_shadow


def home_content(page: ft.Page):
    return ft.Container(
        content=ft.Container(
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
                        content=ft.Row(
                            [
                                ft.ElevatedButton(
                                    "Ver Portfólio",
                                    style=ft.ButtonStyle(
                                        bgcolor=COLORS["secondary"],
                                        color=ft.colors.WHITE,
                                        padding=ft.padding.symmetric(
                                            horizontal=30 if page.width > 600 else 20,
                                            vertical=15 if page.width > 600 else 10,
                                        ),
                                    ),
                                    on_click=lambda e: page.go("/portfolio"),
                                ),
                                ft.ElevatedButton(
                                    "Nossos Serviços",
                                    style=ft.ButtonStyle(
                                        bgcolor=COLORS["primary"],
                                        color=ft.colors.WHITE,
                                        padding=ft.padding.symmetric(
                                            horizontal=30 if page.width > 600 else 20,
                                            vertical=15 if page.width > 600 else 10,
                                        ),
                                    ),
                                    on_click=lambda e: page.go("/services"),
                                ),
                                ft.ElevatedButton(
                                    "Entre em Contato",
                                    style=ft.ButtonStyle(
                                        bgcolor=COLORS["accent"],
                                        color=ft.colors.WHITE,
                                        padding=ft.padding.symmetric(
                                            horizontal=30 if page.width > 600 else 20,
                                            vertical=15 if page.width > 600 else 10,
                                        ),
                                    ),
                                    on_click=lambda e: page.go("/contact"),
                                ),
                            ],
                            alignment="center",
                            spacing=20 if page.width > 600 else 10,
                            wrap=True,
                        ),
                        margin=ft.margin.only(top=40 if page.width > 600 else 30),
                    ),
                ],
                horizontal_alignment="center",
                alignment="center",
                spacing=20,
            ),
            alignment=ft.alignment.center,
            expand=True,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 350),
        alignment=ft.alignment.center,
    )
