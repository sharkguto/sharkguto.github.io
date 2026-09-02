#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# about.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :

import flet as ft
from theme import COLORS, get_theme, get_responsive_font_size, get_responsive_spacing
from utils.flet_runtime import call_page_method

# Variáveis globais para header e footer
header = None
footer = None
main_content = None

def main(page: ft.Page):
    global header, footer, main_content
    
    # Configurações iniciais da página
    page.title = "GMF-tech | Fábrica de software"
    page.bgcolor = COLORS["background"]
    page.scroll = None
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme = get_theme()

    # Pré-carregar dados de cotação
    from pages.coins import preload_data
    page.run_task(preload_data)

    # Funções para navegação entre páginas
    def go_to_home(e):
        call_page_method(page, "push_route", "/")

    def go_to_services(e):
        call_page_method(page, "push_route", "/services")

    def go_to_about(e):
        call_page_method(page, "push_route", "/about")

    def go_to_contact(e):
        call_page_method(page, "push_route", "/contact")

    def go_to_portfolio(e):
        call_page_method(page, "push_route", "/portfolio")

    def go_to_coins(e):
        call_page_method(page, "push_route", "/coins")

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
                            "Engenharia de software sob medida",
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
                    leading=ft.Icon(ft.Icons.CONTACT_MAIL, color=COLORS["secondary"], size=icon_size),
                    title=ft.Text("Fale com a GMF-tech", size=item_font_size, weight="bold"),
                    on_click=navigate_and_close_drawer("/contact"),
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
                ft.TextButton(
                    "Portfólio",
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                    ),
                    on_click=go_to_portfolio,
                ),
            ]

            if page.route != "/coins":
                nav_buttons.append(
                    ft.Button(
                        "Fale com a GMF-tech",
                        bgcolor=COLORS["secondary"],
                        color=ft.Colors.WHITE,
                        on_click=go_to_contact,
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
        width = page.width if page.width else 1024
        is_mobile = width <= 600

        brand = ft.Row(
            [
                ft.Image(src="/favicon.png", width=22, height=22, fit=ft.BoxFit.CONTAIN),
                ft.Text("GMF-tech", size=15, color=ft.Colors.WHITE, weight="bold"),
                *(
                    [
                        ft.Container(width=1, height=18, bgcolor=ft.Colors.GREY_700),
                        ft.Text(
                            "Fábrica de software sob medida",
                            size=13,
                            color=ft.Colors.GREY_300,
                        ),
                    ]
                    if not is_mobile
                    else []
                ),
            ],
            spacing=7,
            tight=True,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        contact = ft.Container(
            content=ft.Row(
                [
                    ft.Icon(ft.Icons.MAIL_OUTLINE, size=15, color=COLORS["accent"]),
                    ft.Text("contato@gmf-tech.com", size=12, color=ft.Colors.GREY_200),
                ],
                spacing=5,
                tight=True,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.Padding.symmetric(horizontal=6, vertical=4),
            border_radius=ft.BorderRadius.all(4),
            url="mailto:contato@gmf-tech.com",
            ink=True,
            tooltip="Enviar e-mail para a GMF-tech",
        )

        copyright_text = ft.Text(
            "© 2026 GMF-tech",
            size=11,
            color=ft.Colors.GREY_400,
            text_align="center" if is_mobile else "right",
        )

        if is_mobile:
            footer_content = ft.Column(
                [
                    ft.Row(
                        [brand, contact],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    copyright_text,
                ],
                spacing=2,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        else:
            footer_content = ft.Row(
                [brand, contact, copyright_text],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            )

        return ft.Container(
            content=footer_content,
            bgcolor=COLORS["primary"],
            padding=ft.Padding.symmetric(
                vertical=6 if is_mobile else 8,
                horizontal=14 if is_mobile else 24,
            ),
            alignment=ft.Alignment.CENTER,
            border=ft.Border.only(top=ft.BorderSide(1, COLORS["secondary"])),
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
        if page.controls:
            page_layout = page.controls[0]
            if isinstance(page_layout, ft.Column) and len(page_layout.controls) == 2:
                page_layout.controls[1] = footer
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
                        ft.Column(
                            [main_content],
                            expand=True,
                            spacing=0,
                            scroll=ft.ScrollMode.AUTO,
                            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                        ),
                        footer,
                    ],
                    expand=True,
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                )
            )
        page.update()

    page.on_route_change = route_change
    route_change()

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER)
