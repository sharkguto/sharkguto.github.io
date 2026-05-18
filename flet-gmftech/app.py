#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# about.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from theme import COLORS, get_theme, get_button_style, get_text_style, get_shadow, get_responsive_font_size, get_responsive_spacing
from utils.flet_runtime import call_page_method
from utils.responsive import ResponsiveConfig

# Variáveis globais para header e footer
header = None
footer = None
main_content = None

def main(page: ft.Page):
    global header, footer, main_content
    
    # Configurações iniciais da página
    page.title = "GMF-tech - Flet, Python e IA para negócios"
    page.bgcolor = COLORS["background"]
    page.scroll = "auto"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = get_theme()

    # Pré-carregar dados de cotação
    from pages.coins import preload_data
    page.run_task(preload_data)

    def show_snack_bar(snack_bar: ft.SnackBar):
        page.snack_bar = snack_bar
        snack_bar.open = True
        if hasattr(page, "show_dialog"):
            try:
                page.show_dialog(snack_bar)
                page.update()
                return
            except Exception:
                pass
        page.update()

    # Função para fechar o diálogo
    def close_dialog(e):
        dialog = getattr(page, "login_dialog", None)
        if dialog:
            dialog.open = False
            if hasattr(page, "pop_dialog"):
                try:
                    page.pop_dialog()
                except Exception:
                    pass
            elif dialog in page.overlay:
                page.overlay.remove(dialog)
        handle_dialog_dismiss(e)
        page.update()

    # Acoes simuladas do diagnostico comercial.
    def login_with_google(e):
        snack_bar = ft.SnackBar(
            content=ft.Text("Diagnóstico via Google iniciado...", style=get_text_style()),
            bgcolor=COLORS["success"],
            behavior=ft.SnackBarBehavior.FLOATING,
        )
        close_dialog(e)
        show_snack_bar(snack_bar)

    def login_with_apple(e):
        snack_bar = ft.SnackBar(
            content=ft.Text("Diagnóstico via Apple iniciado...", style=get_text_style()),
            bgcolor=COLORS["success"],
            behavior=ft.SnackBarBehavior.FLOATING,
        )
        close_dialog(e)
        show_snack_bar(snack_bar)

    def login_with_x(e):
        snack_bar = ft.SnackBar(
            content=ft.Text("Diagnóstico via X iniciado...", style=get_text_style()),
            bgcolor=COLORS["success"],
            behavior=ft.SnackBarBehavior.FLOATING,
        )
        close_dialog(e)
        show_snack_bar(snack_bar)

    # Funções para navegação entre páginas
    def go_to_home(e):
        call_page_method(page, "push_route", "/")

    def go_to_services(e):
        call_page_method(page, "push_route", "/services")

    def go_to_about(e):
        call_page_method(page, "push_route", "/about")

    def go_to_contact(e):
        call_page_method(page, "push_route", "/contact")

    def go_to_coins(e):
        call_page_method(page, "push_route", "/coins")

    def handle_login_click(e):
        page.login_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Agendar diagnóstico técnico", style=get_text_style(20, weight="bold")),
            content=ft.Column(
                [
                    ft.Text(
                        "Escolha um canal para iniciar uma conversa sobre Flet, Python, IA e automação.",
                        style=get_text_style(16, COLORS["text_secondary"]),
                    ),
                    ft.Button(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color=ft.Colors.WHITE),
                                ft.Text("Continuar com Google", color=ft.Colors.WHITE),
                            ],
                            alignment="center",
                        ),
                        bgcolor=COLORS["error"],
                        style=get_button_style(),
                        on_click=login_with_google,
                    ),
                    ft.Button(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.APPLE, color=ft.Colors.WHITE),
                                ft.Text("Continuar com Apple", color=ft.Colors.WHITE),
                            ],
                            alignment="center",
                        ),
                        bgcolor=COLORS["text_primary"],
                        style=get_button_style(),
                        on_click=login_with_apple,
                    ),
                    ft.Button(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.ALTERNATE_EMAIL, color=ft.Colors.WHITE),
                                ft.Text("Continuar com X", color=ft.Colors.WHITE),
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
            on_dismiss=lambda e: handle_dialog_dismiss(e),
        )
        if hasattr(page, "show_dialog"):
            page.show_dialog(page.login_dialog)
        else:
            page.overlay.append(page.login_dialog)
            page.login_dialog.open = True
            page.update()

    def handle_dialog_dismiss(e):
        return None

    def close_drawer(e):
        if hasattr(page, "close_drawer"):
            call_page_method(page, "close_drawer")
        else:
            page.drawer.open = False
            page.update()

    def navigate_and_close_drawer(route):
        def handler(e):
            if page.drawer:
                close_drawer(e)
            call_page_method(page, "push_route", route)
        return handler

    def login_and_close_drawer(e):
        if page.drawer:
            close_drawer(e)
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
                        ft.Image(src="/favicon.png", width=52, height=52, fit=ft.BoxFit.CONTAIN),
                        ft.Text(
                            "GMF-tech",
                            size=header_font_size,
                            weight="bold",
                            color=COLORS["primary"],
                        ),
                        ft.Text(
                            "Flet, Python e IA aplicada",
                            size=item_font_size - 2,
                            color=COLORS["text_secondary"],
                        ),
                    ],
                    horizontal_alignment="center",
                    spacing=5,
                ),
                padding=ft.Padding.symmetric(vertical=20, horizontal=16),
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
                leading=ft.Icon(ft.Icons.ROCKET_LAUNCH, color=COLORS["primary"], size=icon_size),
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
                leading=ft.Icon(ft.Icons.QUERY_STATS, color=COLORS["primary"], size=icon_size),
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

        # Adicionar CTA comercial se não estiver na página de cotação
        if page.route != "/coins":
            drawer_items.extend([
                ft.Divider(height=1, color=COLORS["text_secondary"]),
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.TASK_ALT, color=COLORS["secondary"], size=icon_size),
                    title=ft.Text("Diagnóstico", size=item_font_size, weight="bold"),
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
        # Calculate responsive logo font size
        logo_font_size = get_responsive_font_size(32, width)
        
        # Calculate responsive toolbar height (8% of viewport height)
        max_height = page.height * 0.08 if page.height else 60
        
        # Calculate responsive button spacing
        button_spacing = get_responsive_spacing(15, width)
        
        # Calculate responsive button padding
        button_padding_h = get_responsive_spacing(20, width)
        button_padding_v = get_responsive_spacing(10, width)
        
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
                    ft.Button(
                        "Diagnóstico",
                        bgcolor=COLORS["secondary"],
                        color=ft.Colors.WHITE,
                        on_click=handle_login_click,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=6),
                            padding=ft.Padding.symmetric(horizontal=button_padding_h, vertical=button_padding_v),
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
                    if hasattr(page, "show_drawer"):
                        call_page_method(page, "show_drawer")
                    else:
                        page.drawer.open = True
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
                content=ft.Row(
                    [
                        ft.Image(src="/favicon.png", width=34, height=34, fit=ft.BoxFit.CONTAIN),
                        ft.Text(
                            "GMF-tech",
                            size=logo_font_size,
                            weight="bold",
                            color=ft.Colors.WHITE,
                        ),
                    ],
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=ft.Padding.only(left=20),
            ),
            leading_width=240,
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
                        "GMF-tech - Flet, Python e IA aplicada",
                        size=title_font_size,
                        color=ft.Colors.WHITE,
                        weight="bold",
                        font_family="Roboto",
                        text_align="center",
                    ),
                    ft.Text(
                        "contato@gmf-tech.com | consultoria em Flet, automação e IA",
                        size=contact_font_size,
                        color=ft.Colors.GREY_300,
                        text_align="center",
                    ),
                    ft.Text(
                        "© 2026 GMF-tech. Todos os direitos reservados.",
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
                                tooltip="Comunidade",
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
                                tooltip="Portfólio",
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
            padding=ft.Padding.symmetric(
                vertical=padding_vertical,
                horizontal=padding_horizontal
            ),
            border_radius=ft.BorderRadius.only(top_left=8, top_right=8),
            alignment=ft.Alignment.CENTER,
            shadow=get_shadow(),
        )

    # Criar o header e drawer
    is_mobile = (page.width or 1024) <= 600
    page.appbar = create_header(is_mobile)
    if is_mobile:
        page.drawer = create_mobile_drawer()
    footer = create_footer()

    # Listener para redimensionamento da janela
    def on_resize(e):
        global footer
        is_mobile = (page.width or 1024) <= 600
        page.appbar = create_header(is_mobile)
        if is_mobile:
            page.drawer = create_mobile_drawer()
        else:
            page.drawer = None
        footer = create_footer()
        page.update()

    page.on_resize = on_resize

    def route_change(route_event=None):
        global main_content
        page.controls.clear()

        active_route = getattr(route_event, "route", None) or page.route or "/"
        if active_route == "":
            active_route = "/"
        page.route = active_route

        # Atualiza o header e drawer quando a rota muda
        is_mobile = (page.width or 1024) <= 600
        page.appbar = create_header(is_mobile)
        if is_mobile:
            page.drawer = create_mobile_drawer()
        else:
            page.drawer = None

        main_content = None
        if active_route == "/":
            from pages.home import home_content
            main_content = home_content(page)
        elif active_route == "/services":
            from pages.services import services_content
            main_content = services_content(page)
        elif active_route == "/about":
            from pages.about import about_content
            main_content = about_content(page)
        elif active_route == "/contact":
            from pages.contact import contact_content
            main_content = contact_content(page)
        elif active_route == "/coins":
            from pages.coins import currency_chart_content
            main_content = currency_chart_content(page)
        elif active_route == "/portfolio":
            from pages.portfolio import portfolio_content
            main_content = portfolio_content(page)

        if main_content:
            page.controls.append(
                ft.Column(
                    [
                        main_content,
                        footer,
                    ],
                    expand=True,
                    spacing=0,
                )
            )
        page.update()

    page.on_route_change = route_change
    route_change()

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
