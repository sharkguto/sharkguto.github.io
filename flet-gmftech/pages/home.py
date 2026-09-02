import flet as ft

from theme import COLORS, get_responsive_font_size, get_responsive_padding, get_responsive_spacing, get_shadow
from utils.flet_runtime import call_page_method
from utils.responsive import Breakpoint, ResponsiveConfig


def home_content(page: ft.Page):
    width = page.width if page.width else 1024
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    is_mobile = breakpoint == Breakpoint.MOBILE

    title_size = get_responsive_font_size(40 if is_mobile else 48, width)
    subtitle_size = get_responsive_font_size(20 if is_mobile else 22, width)
    section_title_size = get_responsive_font_size(34 if is_mobile else 38, width)
    body_size = get_responsive_font_size(16, width)
    button_padding_h = get_responsive_padding(28, width)
    button_padding_v = get_responsive_padding(14, width)
    section_padding = get_responsive_padding(32 if is_mobile else 52, width)
    section_spacing = get_responsive_spacing(34, width)

    def nav_button(text, bgcolor, route, icon=None):
        return ft.Button(
            text,
            icon=icon,
            style=ft.ButtonStyle(
                bgcolor=bgcolor,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(radius=6),
                padding=ft.Padding.symmetric(
                    horizontal=button_padding_h,
                    vertical=button_padding_v,
                ),
            ),
            on_click=lambda e: call_page_method(page, "push_route", route),
        )

    def stat_card(value, label, accent=COLORS["accent"]):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(value, size=get_responsive_font_size(24, width), weight="bold", color=accent),
                    ft.Text(label, size=get_responsive_font_size(13, width), color=ft.Colors.WHITE_70),
                ],
                spacing=4,
            ),
            padding=ft.Padding.all(get_responsive_padding(16, width)),
            bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.16, ft.Colors.WHITE)),
            border_radius=ft.BorderRadius.all(8),
        )

    def service_card(icon, title, text, accent):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Icon(icon, size=get_responsive_font_size(34, width), color=accent),
                    ft.Text(title, size=get_responsive_font_size(19, width), weight="bold", color=COLORS["text_primary"]),
                    ft.Text(text, size=body_size, color=COLORS["text_secondary"]),
                ],
                spacing=12,
            ),
            padding=ft.Padding.all(get_responsive_padding(22, width)),
            bgcolor=COLORS["surface"],
            border_radius=ft.BorderRadius.all(8),
            border=ft.Border.all(1, COLORS["muted"]),
            shadow=get_shadow(),
        )

    hero_visual = ft.Container(
        content=ft.Stack(
            [
                ft.Image(
                    src="/velejar_facil.png",
                    fit=ft.BoxFit.COVER,
                    width=480 if not is_mobile else max(width - 48, 280),
                    height=360 if not is_mobile else 220,
                    border_radius=ft.BorderRadius.all(8),
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.HUB, color=COLORS["accent_alt"], size=20),
                                    ft.Text("Arquitetura conectada ao negócio", color=ft.Colors.WHITE, weight="bold"),
                                ],
                                spacing=8,
                            ),
                            ft.Text(
                                "Aplicações, APIs e integrações projetadas para sustentar a operação e a evolução do produto.",
                                color=ft.Colors.WHITE_70,
                                size=get_responsive_font_size(13, width),
                            ),
                        ],
                        spacing=6,
                    ),
                    bgcolor=ft.Colors.with_opacity(0.86, COLORS["primary"]),
                    padding=ft.Padding.all(18),
                    width=300 if not is_mobile else max(width - 80, 240),
                    border_radius=ft.BorderRadius.all(8),
                    right=16,
                    bottom=16,
                ),
            ],
        ),
        border_radius=ft.BorderRadius.all(8),
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        shadow=get_shadow(),
    )

    hero = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=ft.Text(
                                    "Fábrica de software especializada",
                                    size=get_responsive_font_size(13, width),
                                    color=COLORS["accent"],
                                    weight="bold",
                                ),
                                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                                border=ft.Border.all(1, ft.Colors.with_opacity(0.35, COLORS["accent"])),
                                border_radius=ft.BorderRadius.all(6),
                            ),
                            ft.Text(
                                "Arquitetura de soluções e sistemas sob medida",
                                size=title_size,
                                weight="bold",
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "A GMF-tech desenvolve e implanta soluções com Python 3, FastAPI, React e Flet para web, WebAssembly e mobile.",
                                size=subtitle_size,
                                color=ft.Colors.WHITE_70,
                            ),
                            ft.Row(
                                [
                                    nav_button("Falar sobre um projeto", COLORS["coral"], "/contact", ft.Icons.CHAT),
                                    nav_button("Conhecer serviços", COLORS["secondary"], "/services", ft.Icons.ROCKET_LAUNCH),
                                    nav_button("Ver projetos", COLORS["accent"], "/portfolio", ft.Icons.TRAVEL_EXPLORE),
                                ],
                                wrap=True,
                                spacing=get_responsive_spacing(12, width),
                            ),
                            ft.ResponsiveRow(
                                [
                                    ft.Container(content=stat_card("Arquitetura", "Soluções escaláveis e integradas"), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=stat_card("Backend Python", "APIs e serviços com FastAPI", COLORS["accent_alt"]), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=stat_card("Web e mobile", "React, Flet e WebAssembly"), col={"sm": 12, "md": 4, "lg": 4}),
                                ],
                                spacing=10,
                                run_spacing=10,
                                visible=not is_mobile,
                            ),
                        ],
                        spacing=get_responsive_spacing(22, width),
                    ),
                    col={"sm": 12, "md": 7, "lg": 7},
                ),
                ft.Container(
                    content=hero_visual,
                    col={"sm": 12, "md": 5, "lg": 5},
                    alignment=ft.Alignment.CENTER,
                    visible=not is_mobile,
                ),
            ],
            spacing=24,
            run_spacing=24,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=COLORS["primary"],
        padding=ft.Padding.symmetric(horizontal=section_padding, vertical=get_responsive_padding(36, width)),
        width=width,
    )

    services = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Especialização técnica para soluções completas",
                    size=section_title_size,
                    weight="bold",
                    color=COLORS["text_primary"],
                    text_align="center",
                ),
                ft.Text(
                    "Arquitetura, desenvolvimento e implantação conduzidos com tecnologias adequadas a cada contexto.",
                    size=subtitle_size,
                    color=COLORS["text_secondary"],
                    text_align="center",
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(content=service_card(ft.Icons.ARCHITECTURE, "Arquitetura de Soluções", "Modelagem de sistemas, componentes, integrações, dados, segurança e requisitos não funcionais.", COLORS["primary"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.API, "Backend Python e FastAPI", "APIs, serviços e integrações com contratos bem definidos, testes e observabilidade.", COLORS["secondary"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.WEB, "Frontend React", "Interfaces web componentizadas, responsivas e integradas às regras do produto.", COLORS["coral"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.DEVICES, "Aplicações com Flet", "Soluções em Python para web, WebAssembly e dispositivos móveis.", COLORS["secondary"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.HUB, "Dados e Integrações", "Bancos de dados, WebSockets e integrações entre sistemas e serviços externos.", COLORS["accent_alt"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.CLOUD, "Cloud, DevOps e Segurança", "Ambientes, pipelines, monitoramento e controles para operação em produção.", COLORS["accent"]), col={"sm": 12, "md": 6, "lg": 4}),
                    ],
                    spacing=16,
                    run_spacing=16,
                ),
            ],
            horizontal_alignment="center",
            spacing=section_spacing,
        ),
        bgcolor=COLORS["background"],
        padding=ft.Padding.symmetric(horizontal=section_padding, vertical=get_responsive_padding(54, width)),
        width=width,
    )

    method = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Processo de entrega", size=get_responsive_font_size(16, width), color=COLORS["accent"], weight="bold"),
                            ft.Text("Engenharia aplicada do projeto à operação.", size=section_title_size, weight="bold", color=ft.Colors.WHITE),
                            ft.Text(
                                "A GMF-tech conduz as decisões de arquitetura e desenvolvimento, define responsabilidades e acompanha cada etapa até a entrada em operação.",
                                size=body_size,
                                color=ft.Colors.WHITE_70,
                            ),
                        ],
                        spacing=14,
                    ),
                    col={"sm": 12, "md": 5, "lg": 5},
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(leading=ft.Icon(ft.Icons.FACT_CHECK, color=COLORS["accent_alt"]), title=ft.Text("1. Entender objetivos, requisitos e restrições do negócio", color=ft.Colors.WHITE)),
                            ft.ListTile(leading=ft.Icon(ft.Icons.ROUTE, color=COLORS["accent_alt"]), title=ft.Text("2. Definir arquitetura, contratos e plano de implementação", color=ft.Colors.WHITE)),
                            ft.ListTile(leading=ft.Icon(ft.Icons.SPEED, color=COLORS["accent_alt"]), title=ft.Text("3. Desenvolver, testar, implantar e sustentar a solução", color=ft.Colors.WHITE)),
                        ],
                        spacing=6,
                    ),
                    col={"sm": 12, "md": 7, "lg": 7},
                ),
            ],
            spacing=24,
            run_spacing=24,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=COLORS["dark_surface"],
        padding=ft.Padding.symmetric(horizontal=section_padding, vertical=get_responsive_padding(50, width)),
        width=width,
    )

    return ft.Container(
        content=ft.Column(
            [hero, services, method],
            spacing=0,
        ),
        bgcolor=COLORS["background"],
        width=width,
    )
