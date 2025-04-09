#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# about.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from theme import COLORS, get_theme, get_button_style, get_text_style, get_shadow

# Variáveis globais para header e footer
header = None
footer = None

def main(page: ft.Page):
    global header, footer
    
    # Configurações iniciais da página
    page.title = "GMF-tech - Outsourcing em TI"
    page.bgcolor = COLORS["background"]
    page.scroll = "auto"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.fonts = {
        "Roboto": "https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap"
    }
    page.theme = get_theme()

    # Função para fechar o diálogo
    def close_dialog(e):
        if page.overlay:
            page.close(page.login_dialog)
        page.update()

    # Funções de login simuladas
    def login_with_google(e):
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Login com Google iniciado...", style=get_text_style()),
            bgcolor=COLORS["success"],
            behavior=ft.SnackBarBehavior.FLOATING,
        )
        page.snack_bar.open = True
        close_dialog(e)
        page.update()

    def login_with_apple(e):
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Login com Apple iniciado...", style=get_text_style()),
            bgcolor=COLORS["success"],
            behavior=ft.SnackBarBehavior.FLOATING,
        )
        page.snack_bar.open = True
        close_dialog(e)
        page.update()

    def login_with_x(e):
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Login com X iniciado...", style=get_text_style()),
            bgcolor=COLORS["success"],
            behavior=ft.SnackBarBehavior.FLOATING,
        )
        page.snack_bar.open = True
        close_dialog(e)
        page.update()

    # Funções para navegação entre páginas
    def go_to_home(e):
        page.go("/")

    def go_to_services(e):
        page.go("/services")

    def go_to_about(e):
        page.go("/about")

    def go_to_contact(e):
        page.go("/contact")

    def go_to_coins(e):
        page.go("/coins")

    def handle_login_click(e):
        page.login_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Login na Plataforma de Cursos", style=get_text_style(20, weight="bold")),
            content=ft.Column(
                [
                    ft.Text("Escolha como deseja entrar:", style=get_text_style(16, COLORS["text_secondary"])),
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color=ft.Colors.WHITE),
                                ft.Text("Login com Google", color=ft.Colors.WHITE),
                            ],
                            alignment="center",
                        ),
                        bgcolor=COLORS["error"],
                        style=get_button_style(),
                        on_click=login_with_google,
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.APPLE, color=ft.Colors.WHITE),
                                ft.Text("Login com Apple", color=ft.Colors.WHITE),
                            ],
                            alignment="center",
                        ),
                        bgcolor=COLORS["text_primary"],
                        style=get_button_style(),
                        on_click=login_with_apple,
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.ALTERNATE_EMAIL, color=ft.Colors.WHITE),
                                ft.Text("Login com X", color=ft.Colors.WHITE),
                            ],
                            alignment="center",
                        ),
                        bgcolor=COLORS["accent"],
                        style=get_button_style(),
                        on_click=login_with_x,
                    ),
                ],
                tight=True,
                spacing=15,
            ),
            actions=[ft.TextButton("Cancelar", on_click=lambda e: close_dialog(e))],
            actions_alignment="end",
        )
        page.overlay.append(page.login_dialog)
        page.login_dialog.open = True
        page.update()

    def create_header(is_mobile):
        max_height = page.height * 0.08 if page.height else 60
        
        navigation_items = [
            ft.PopupMenuItem(text="Início", on_click=go_to_home),
            ft.PopupMenuItem(text="Serviços", on_click=go_to_services),
            ft.PopupMenuItem(text="Sobre", on_click=go_to_about),
            ft.PopupMenuItem(text="Contato", on_click=go_to_contact),
            ft.PopupMenuItem(text="Cotação", on_click=go_to_coins),
            ft.PopupMenuItem(text="Login", on_click=handle_login_click),
        ]

        if not is_mobile:
            navigation_controls = ft.Row(
                [
                    ft.TextButton(
                        "Início",
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
                        ),
                        on_click=go_to_home,
                    ),
                    ft.TextButton(
                        "Serviços",
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
                        ),
                        on_click=go_to_services,
                    ),
                    ft.TextButton(
                        "Sobre",
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
                        ),
                        on_click=go_to_about,
                    ),
                    ft.TextButton(
                        "Contato",
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
                        ),
                        on_click=go_to_contact,
                    ),
                    ft.TextButton(
                        "Cotação",
                        style=ft.ButtonStyle(
                            color=ft.Colors.WHITE,
                            overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
                        ),
                        on_click=go_to_coins,
                    ),
                    ft.ElevatedButton(
                        "Login",
                        bgcolor=COLORS["secondary"],
                        color=ft.Colors.WHITE,
                        on_click=handle_login_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=ft.padding.symmetric(horizontal=20, vertical=10),
                            overlay_color=ft.colors.with_opacity(0.1, ft.Colors.WHITE),
                        ),
                    ),
                ],
                alignment="end",
                spacing=15,
            )
        else:
            navigation_controls = ft.PopupMenuButton(
                icon=ft.Icons.MENU,
                items=navigation_items,
                icon_color=ft.Colors.WHITE,
            )

        return ft.Container(
            content=ft.Row(
                [
                    ft.Text(
                        "GMF-tech",
                        size=32 if page.width > 600 else 24,
                        weight="bold",
                        color=ft.Colors.WHITE,
                        font_family="Roboto",
                    ),
                    navigation_controls,
                ],
                alignment="spaceBetween",
                vertical_alignment="center",
            ),
            bgcolor=COLORS["primary"],
            padding=ft.padding.symmetric(horizontal=30),
            border_radius=ft.border_radius.only(bottom_left=15, bottom_right=15),
            height=max_height,
            shadow=get_shadow(),
        )

    def create_footer():
        max_height = page.height * 0.15 if page.height else 120

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "GMF-tech - Outsourcing em TI",
                        size=20 if page.width > 600 else 16,
                        color=ft.Colors.WHITE,
                        weight="bold",
                        font_family="Roboto",
                    ),
                    ft.Text(
                        "contato@gmf-tech.com | (11) 9999-9999",
                        size=16 if page.width > 600 else 14,
                        color=ft.Colors.GREY_300,
                    ),
                    ft.Text(
                        "© 2025 GMF-tech. Todos os direitos reservados.",
                        size=14 if page.width > 600 else 12,
                        color=ft.Colors.GREY_400,
                    ),
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.Icons.FACEBOOK,
                                icon_color=ft.Colors.WHITE,
                                icon_size=24,
                                tooltip="Facebook",
                            ),
                            ft.IconButton(
                                icon=ft.Icons.PUBLIC,
                                icon_color=ft.Colors.WHITE,
                                icon_size=24,
                                tooltip="LinkedIn",
                            ),
                            ft.IconButton(
                                icon=ft.Icons.PUBLIC,
                                icon_color=ft.Colors.WHITE,
                                icon_size=24,
                                tooltip="Twitter",
                            ),
                        ],
                        alignment="center",
                        spacing=20,
                    ),
                ],
                alignment="center",
                spacing=10,
            ),
            bgcolor=COLORS["primary"],
            padding=ft.padding.symmetric(vertical=20, horizontal=30),
            border_radius=ft.border_radius.only(top_left=15, top_right=15),
            alignment=ft.alignment.center,
            height=max_height,
            shadow=get_shadow(),
        )

    is_mobile = page.width <= 600

    # Inicializar header e footer
    header = create_header(is_mobile)
    footer = create_footer()

    # Listener para redimensionamento da janela
    def on_resize(e):
        footer.content = create_footer().content
        is_mobile = page.width <= 600
        header.content = create_header(is_mobile).content
        header.height = page.height * 0.08 if page.height else 60
        footer.height = page.height * 0.15 if page.height else 120

        page.controls[0].controls[1].height = (
            (page.height * 0.77)
            if page.height
            else (page.height - (header.height + footer.height))
        )
        page.update()

    page.on_resized = on_resize

    def route_change(route_event):
        page.controls.clear()

        main_content = None
        if route_event.route == "/":
            from pages.home import home_content
            main_content = home_content(page)
        elif route_event.route == "/services":
            from pages.services import services_content
            main_content = services_content(page)
        elif route_event.route == "/about":
            from pages.about import about_content
            main_content = about_content(page)
        elif route_event.route == "/contact":
            from pages.contact import contact_content
            main_content = contact_content(page)
        elif route_event.route == "/coins":
            from pages.coins import currency_chart_content
            main_content = currency_chart_content(page)

        fill_height = (
            (page.height * 0.77)
            if page.height
            else (page.height - (header.height + footer.height))
        )

        if main_content:
            page.controls.append(
                ft.Column(
                    [
                        header,
                        ft.Container(
                            content=main_content,
                            expand=True,
                            bgcolor=COLORS["surface"],
                            height=fill_height,
                            padding=ft.padding.symmetric(horizontal=30, vertical=20),
                            border_radius=ft.border_radius.all(15),
                            shadow=get_shadow(),
                        ),
                        footer,
                    ],
                    expand=True,
                    spacing=0,
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route if page.route else "/")

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
