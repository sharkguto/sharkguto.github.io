#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# about.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from theme import COLORS, get_theme, get_button_style, get_text_style, get_shadow, get_responsive_font_size, get_responsive_spacing
from utils.responsive import ResponsiveConfig, Breakpoint

# Variáveis globais para header e footer
header = None
footer = None
main_content = None

def main(page: ft.Page):
    global header, footer, main_content
    
    # Configurações iniciais da página
    page.title = "GMF-tech - Outsourcing em TI"
    page.bgcolor = COLORS["background"]
    page.scroll = "auto"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = get_theme()

    # Pré-carregar dados de cotação
    from pages.coins import preload_data
    page.run_task(preload_data)

    # Função para fechar o diálogo
    def close_dialog(e):
        if page.overlay:
            page.close(page.login_dialog)
            restore_webview(e)
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
        global main_content
        # Esconder o WebView se estiver na página de cotação
        if page.route == "/coins" and main_content:
            try:
                webview = main_content.content.content.controls[0].controls[2].content
                if isinstance(webview, ft.WebView):
                    webview.visible = False
                    page.update()
            except:
                pass
        
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
            actions=[ft.TextButton("Cancelar", on_click=close_dialog)],
            actions_alignment="end",
            on_dismiss=lambda e: restore_webview(e),
        )
        page.overlay.append(page.login_dialog)
        page.login_dialog.open = True
        page.update()

    def restore_webview(e):
        global main_content
        if page.route == "/coins" and main_content:
            try:
                webview = main_content.content.content.controls[0].controls[2].content
                if isinstance(webview, ft.WebView):
                    webview.visible = True
                    page.update()
            except:
                pass

    def close_drawer(e):
        page.close(page.drawer)
        page.update()

    def navigate_and_close_drawer(route):
        def handler(e):
            if page.drawer:
                page.close(page.drawer)
            page.go(route)
        return handler

    def login_and_close_drawer(e):
        if page.drawer:
            page.close(page.drawer)
        handle_login_click(e)

    def create_mobile_drawer():
        # Get responsive values
        width = page.width if page.width else 1024
        
        # Calculate responsive sizes
        header_font_size = get_responsive_font_size(24, width)
        item_font_size = get_responsive_font_size(16, width)
        icon_size = get_responsive_font_size(24, width)
        
        drawer_items = [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Icon(ft.Icons.BUSINESS, size=48, color=COLORS["primary"]),
                        ft.Text(
                            "GMF-tech",
                            size=header_font_size,
                            weight="bold",
                            color=COLORS["primary"],
                        ),
                        ft.Text(
                            "Outsourcing em TI",
                            size=item_font_size - 2,
                            color=COLORS["text_secondary"],
                        ),
                    ],
                    horizontal_alignment="center",
                    spacing=5,
                ),
                padding=ft.padding.symmetric(vertical=20, horizontal=16),
                bgcolor=COLORS["surface"],
            ),
            ft.Divider(height=1, color=COLORS["text_secondary"]),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.HOME, color=COLORS["primary"], size=icon_size),
                title=ft.Text("Início", size=item_font_size),
                on_click=navigate_and_close_drawer("/"),
                selected=page.route == "/",
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.WORK, color=COLORS["primary"], size=icon_size),
                title=ft.Text("Serviços", size=item_font_size),
                on_click=navigate_and_close_drawer("/services"),
                selected=page.route == "/services",
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.INFO, color=COLORS["primary"], size=icon_size),
                title=ft.Text("Sobre", size=item_font_size),
                on_click=navigate_and_close_drawer("/about"),
                selected=page.route == "/about",
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.CONTACT_MAIL, color=COLORS["primary"], size=icon_size),
                title=ft.Text("Contato", size=item_font_size),
                on_click=navigate_and_close_drawer("/contact"),
                selected=page.route == "/contact",
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.ATTACH_MONEY, color=COLORS["primary"], size=icon_size),
                title=ft.Text("Cotação", size=item_font_size),
                on_click=navigate_and_close_drawer("/coins"),
                selected=page.route == "/coins",
            ),
            ft.ListTile(
                leading=ft.Icon(ft.Icons.FOLDER, color=COLORS["primary"], size=icon_size),
                title=ft.Text("Portfólio", size=item_font_size),
                on_click=navigate_and_close_drawer("/portfolio"),
                selected=page.route == "/portfolio",
            ),
        ]

        # Adicionar opção de login se não estiver na página de cotação
        if page.route != "/coins":
            drawer_items.extend([
                ft.Divider(height=1, color=COLORS["text_secondary"]),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.LOGIN, color=COLORS["secondary"], size=icon_size),
                    title=ft.Text("Login", size=item_font_size, weight="bold"),
                    on_click=login_and_close_drawer,
                ),
            ])

        return ft.NavigationDrawer(
            controls=drawer_items,
            bgcolor=ft.Colors.WHITE,
        )

    def create_header(is_mobile):
        # Get responsive values based on screen width
        width = page.width if page.width else 1024
        breakpoint = ResponsiveConfig.get_breakpoint(width)
        
        # Calculate responsive logo font size
        logo_font_size = get_responsive_font_size(32, width)
        
        # Calculate responsive toolbar height (8% of viewport height)
        max_height = page.height * 0.08 if page.height else 60
        
        # Calculate responsive button spacing
        button_spacing = get_responsive_spacing(15, width)
        
        # Calculate responsive button padding
        button_padding_h = get_responsive_spacing(20, width)
        button_padding_v = get_responsive_spacing(10, width)
        
        navigation_items = [
            ft.PopupMenuItem(text="Início", on_click=go_to_home),
            ft.PopupMenuItem(text="Serviços", on_click=go_to_services),
            ft.PopupMenuItem(text="Sobre", on_click=go_to_about),
            ft.PopupMenuItem(text="Contato", on_click=go_to_contact),
            ft.PopupMenuItem(text="Cotação", on_click=go_to_coins),
        ]

        if page.route != "/coins":
            navigation_items.append(ft.PopupMenuItem(text="Login", on_click=handle_login_click))

        if not is_mobile:
            nav_buttons = [
                ft.TextButton(
                    "Início",
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                    ),
                    on_click=go_to_home,
                ),
                ft.TextButton(
                    "Serviços",
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                    ),
                    on_click=go_to_services,
                ),
                ft.TextButton(
                    "Sobre",
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                    ),
                    on_click=go_to_about,
                ),
                ft.TextButton(
                    "Contato",
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                    ),
                    on_click=go_to_contact,
                ),
                ft.TextButton(
                    "Cotação",
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                    ),
                    on_click=go_to_coins,
                ),
            ]

            if page.route != "/coins":
                nav_buttons.append(
                    ft.ElevatedButton(
                        "Login",
                        bgcolor=COLORS["secondary"],
                        color=ft.Colors.WHITE,
                        on_click=handle_login_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=ft.padding.symmetric(horizontal=button_padding_h, vertical=button_padding_v),
                            overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                        ),
                    )
                )

            navigation_controls = ft.Row(
                nav_buttons,
                alignment="end",
                spacing=button_spacing,
            )
        else:
            # Mobile: usar ícone de menu que abre o drawer
            def open_drawer(e):
                if page.drawer:
                    page.open(page.drawer)
                    page.update()
            
            navigation_controls = ft.IconButton(
                icon=ft.Icons.MENU,
                icon_color=ft.Colors.WHITE,
                icon_size=28,
                on_click=open_drawer,
                tooltip="Menu",
            )

        return ft.AppBar(
            leading=ft.Container(
                content=ft.Text(
                    "GMF-tech",
                    size=logo_font_size,
                    weight="bold",
                    color=ft.Colors.WHITE,
                ),
                padding=ft.padding.only(left=20),
            ),
            leading_width=200,
            title=ft.Text(""),
            center_title=False,
            bgcolor=COLORS["primary"],
            actions=[navigation_controls],
            toolbar_height=max_height,
        )

    def create_footer():
        # Get responsive values based on screen width
        width = page.width if page.width else 1024
        breakpoint = ResponsiveConfig.get_breakpoint(width)
        
        # Calculate responsive font sizes
        title_font_size = get_responsive_font_size(18, width)
        contact_font_size = get_responsive_font_size(14, width)
        copyright_font_size = get_responsive_font_size(12, width)
        
        # Calculate responsive icon size
        icon_size = get_responsive_font_size(20, width)
        
        # Calculate responsive spacing
        column_spacing = get_responsive_spacing(8, width)
        icon_spacing = get_responsive_spacing(15, width)
        
        # Calculate responsive padding
        padding_vertical = get_responsive_spacing(15, width)
        padding_horizontal = get_responsive_spacing(20, width)
        
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "GMF-tech - Outsourcing em TI",
                        size=title_font_size,
                        color=ft.Colors.WHITE,
                        weight="bold",
                        font_family="Roboto",
                        text_align="center",
                    ),
                    ft.Text(
                        "contato@gmf-tech.com | (11) 9999-9999",
                        size=contact_font_size,
                        color=ft.Colors.GREY_300,
                        text_align="center",
                    ),
                    ft.Text(
                        "© 2025 GMF-tech. Todos os direitos reservados.",
                        size=copyright_font_size,
                        color=ft.Colors.GREY_400,
                        text_align="center",
                    ),
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.Icons.FACEBOOK,
                                icon_color=ft.Colors.WHITE,
                                icon_size=icon_size,
                                tooltip="Facebook",
                            ),
                            ft.IconButton(
                                icon=ft.Icons.PUBLIC,
                                icon_color=ft.Colors.WHITE,
                                icon_size=icon_size,
                                tooltip="LinkedIn",
                            ),
                            ft.IconButton(
                                icon=ft.Icons.PUBLIC,
                                icon_color=ft.Colors.WHITE,
                                icon_size=icon_size,
                                tooltip="Twitter",
                            ),
                        ],
                        alignment="center",
                        spacing=icon_spacing,
                    ),
                ],
                alignment="center",
                spacing=column_spacing,
                horizontal_alignment="center",
            ),
            bgcolor=COLORS["primary"],
            padding=ft.padding.symmetric(
                vertical=padding_vertical,
                horizontal=padding_horizontal
            ),
            border_radius=ft.border_radius.only(top_left=15, top_right=15),
            alignment=ft.alignment.center,
            shadow=get_shadow(),
        )

    # Criar o header e drawer
    is_mobile = page.width <= 600
    page.appbar = create_header(is_mobile)
    if is_mobile:
        page.drawer = create_mobile_drawer()
    footer = create_footer()

    # Listener para redimensionamento da janela
    def on_resize(e):
        global footer
        is_mobile = page.width <= 600
        page.appbar = create_header(is_mobile)
        if is_mobile:
            page.drawer = create_mobile_drawer()
        else:
            page.drawer = None
        footer = create_footer()
        page.update()

    page.on_resized = on_resize

    def route_change(route_event):
        global main_content
        page.controls.clear()

        # Atualiza o header e drawer quando a rota muda
        is_mobile = page.width <= 600
        page.appbar = create_header(is_mobile)
        if is_mobile:
            page.drawer = create_mobile_drawer()
        else:
            page.drawer = None

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
        elif route_event.route == "/portfolio":
            from pages.portfolio import portfolio_content
            main_content = portfolio_content(page)

        if main_content:
            page.controls.append(
                ft.Column(
                    [
                        ft.Container(
                            content=main_content,
                            expand=True,
                            bgcolor=COLORS["surface"],
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
