import flet as ft
from theme import COLORS, get_responsive_font_size, get_responsive_padding, get_responsive_spacing
from utils.responsive import ResponsiveConfig


def home_content(page: ft.Page):
    # Get current breakpoint
    width = page.width if page.width else 1024
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    
    # Calculate responsive values
    title_size = get_responsive_font_size(48, width)
    subtitle_size = get_responsive_font_size(32, width)
    button_padding_h = get_responsive_padding(30, width)
    button_padding_v = get_responsive_padding(15, width)
    button_spacing = get_responsive_spacing(20, width)
    top_margin = get_responsive_spacing(40, width)
    column_spacing = get_responsive_spacing(20, width)
    
    return ft.Container(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Bem-vindo à GMF-tech",
                        size=title_size,
                        weight="bold",
                        color=COLORS["text_primary"],
                        text_align="center",
                    ),
                    ft.Text(
                        "Sua parceira em soluções de TI",
                        size=subtitle_size,
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
                                            horizontal=button_padding_h,
                                            vertical=button_padding_v,
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
                                            horizontal=button_padding_h,
                                            vertical=button_padding_v,
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
                                            horizontal=button_padding_h,
                                            vertical=button_padding_v,
                                        ),
                                    ),
                                    on_click=lambda e: page.go("/contact"),
                                ),
                            ],
                            alignment="center",
                            spacing=button_spacing,
                            wrap=True,
                        ),
                        margin=ft.margin.only(top=top_margin),
                    ),
                ],
                horizontal_alignment="center",
                alignment="center",
                spacing=column_spacing,
            ),
            alignment=ft.alignment.center,
            expand=True,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 350),
        alignment=ft.alignment.center,
    )
