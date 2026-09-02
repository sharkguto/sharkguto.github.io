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
                                    ft.Text("Sistemas integrados à operação", color=ft.Colors.WHITE, weight="bold"),
                                ],
                                spacing=8,
                            ),
                            ft.Text(
                                "Aplicações, APIs, dados e automações conectados aos processos da empresa.",
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
                                    "Fábrica de software",
                                    size=get_responsive_font_size(13, width),
                                    color=COLORS["accent"],
                                    weight="bold",
                                ),
                                padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                                border=ft.Border.all(1, ft.Colors.with_opacity(0.35, COLORS["accent"])),
                                border_radius=ft.BorderRadius.all(6),
                            ),
                            ft.Text(
                                "Software sob medida para operações e produtos digitais",
                                size=title_size,
                                weight="bold",
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "A GMF-tech especifica, desenvolve e implanta aplicações web, mobile e sistemas internos, com arquitetura, integrações e infraestrutura adequadas ao negócio.",
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
                                    ft.Container(content=stat_card("Sob medida", "Escopo, desenvolvimento e evolução"), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=stat_card("Full stack", "Frontend, backend e dados", COLORS["accent_alt"]), col={"sm": 12, "md": 4, "lg": 4}),
                                    ft.Container(content=stat_card("Entrega", "Cloud, CI/CD e observabilidade"), col={"sm": 12, "md": 4, "lg": 4}),
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
                    "Engenharia de software de ponta a ponta",
                    size=section_title_size,
                    weight="bold",
                    color=COLORS["text_primary"],
                    text_align="center",
                ),
                ft.Text(
                    "Atuação desde a definição do escopo até a implantação, documentação e evolução do sistema.",
                    size=subtitle_size,
                    color=COLORS["text_secondary"],
                    text_align="center",
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(content=service_card(ft.Icons.ASSIGNMENT, "Discovery e Requisitos", "Objetivos, fluxos, regras de negócio, backlog e critérios de aceite.", COLORS["secondary"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.ARCHITECTURE, "Arquitetura de Software", "Definição de componentes, dados, integrações, segurança e operação.", COLORS["primary"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.DEVELOPER_BOARD, "IoT e Sistemas Conectados", "Prototipagem eletrônica, telemetria e integração entre dispositivos e software.", COLORS["coral"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.DEVICES, "Aplicações Web e Mobile", "Produtos digitais, portais, sistemas internos e interfaces responsivas.", COLORS["secondary"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.CLOUD, "Cloud, DevOps e Segurança", "Ambientes, pipelines, monitoramento e controles para operação em produção.", COLORS["accent"]), col={"sm": 12, "md": 6, "lg": 4}),
                        ft.Container(content=service_card(ft.Icons.SETTINGS_SUGGEST, "Dados, Automação e IA", "Integração de dados e automação de processos com critérios de segurança e governança.", COLORS["accent_alt"]), col={"sm": 12, "md": 6, "lg": 4}),
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
                            ft.Text("Projetos conduzidos com escopo, critérios técnicos e previsibilidade.", size=section_title_size, weight="bold", color=ft.Colors.WHITE),
                            ft.Text(
                                "A GMF-tech organiza as decisões de produto e engenharia, define responsabilidades e acompanha cada etapa até a entrada em operação.",
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
                            ft.ListTile(leading=ft.Icon(ft.Icons.FACT_CHECK, color=COLORS["accent_alt"]), title=ft.Text("1. Definir objetivos, escopo, riscos e critérios de aceite", color=ft.Colors.WHITE)),
                            ft.ListTile(leading=ft.Icon(ft.Icons.ROUTE, color=COLORS["accent_alt"]), title=ft.Text("2. Projetar a arquitetura e validar os fluxos prioritários", color=ft.Colors.WHITE)),
                            ft.ListTile(leading=ft.Icon(ft.Icons.SPEED, color=COLORS["accent_alt"]), title=ft.Text("3. Implantar, documentar e planejar a evolução", color=ft.Colors.WHITE)),
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
