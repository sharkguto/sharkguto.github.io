#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flet as ft

from theme import COLORS, get_responsive_font_size, get_responsive_padding, get_responsive_spacing, get_shadow
from utils.responsive import Breakpoint, ResponsiveConfig


def services_content(page: ft.Page):
    width = page.width if page.width else 1024
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    is_mobile = breakpoint == Breakpoint.MOBILE
    selected_service = {"index": 0}
    service_cards = []
    service_actions = []
    service_wrappers = []
    service_grid = ft.ResponsiveRow()
    stack_panel = ft.Container()
    stack_panel_wrapper = ft.Container()

    cards_per_row = {
        Breakpoint.MOBILE: 1,
        Breakpoint.TABLET: 2,
        Breakpoint.DESKTOP: 3,
    }[breakpoint]

    def create_card(icon, title, description, highlight=COLORS["secondary"], index=None):
        card_padding = get_responsive_padding(22, width)
        icon_size = get_responsive_font_size(34, width)
        title_size = get_responsive_font_size(19, width)
        description_size = get_responsive_font_size(15, width)
        selected = index == selected_service["index"]
        action_icon = ft.Icon(
            ft.Icons.KEYBOARD_ARROW_DOWN if selected else ft.Icons.ARROW_FORWARD,
            size=get_responsive_font_size(16, width),
            color=highlight,
        )
        action_text = ft.Text(
            "Selecionado" if selected else "Ver detalhes",
            size=get_responsive_font_size(13, width),
            color=highlight,
            weight="bold",
        )

        card = ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Icon(icon, size=icon_size, color=highlight),
                        bgcolor=ft.Colors.with_opacity(0.09, highlight),
                        padding=ft.Padding.all(10),
                        border_radius=ft.BorderRadius.all(8),
                    ),
                    ft.Text(title, size=title_size, weight="bold", color=COLORS["text_primary"]),
                    ft.Text(description, size=description_size, color=COLORS["text_secondary"]),
                    ft.Row(
                        [
                            action_icon,
                            action_text,
                        ],
                        spacing=6,
                    ) if index is not None else ft.Container(height=0),
                ],
                spacing=12,
            ),
            padding=ft.Padding.all(card_padding),
            bgcolor=ft.Colors.with_opacity(0.06, highlight) if selected else COLORS["surface"],
            border_radius=ft.BorderRadius.all(8),
            border=ft.Border.all(2 if selected else 1, highlight if selected else COLORS["muted"]),
            shadow=get_shadow(),
            margin=ft.Margin.all(4),
            ink=index is not None,
        )
        if index is not None:
            card.on_click = select_service(index)
            service_cards.append(card)
            service_actions.append((action_icon, action_text))
        return card

    def create_stack_chip(label, color=COLORS["secondary"]):
        return ft.Container(
            content=ft.Text(label, size=get_responsive_font_size(13, width), color=COLORS["text_primary"], weight="w500"),
            bgcolor=ft.Colors.with_opacity(0.12, color),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.28, color)),
            border_radius=ft.BorderRadius.all(4),
            padding=ft.Padding.symmetric(horizontal=get_responsive_padding(10, width), vertical=get_responsive_padding(7, width)),
        )

    def build_stack_panel():
        service = services[selected_service["index"]]
        service_header = ft.Row(
            [
                ft.Container(
                    content=ft.Icon(service["icon"], color=service["highlight"], size=get_responsive_font_size(30, width)),
                    bgcolor=ft.Colors.with_opacity(0.1, service["highlight"]),
                    padding=ft.Padding.all(10),
                    border_radius=ft.BorderRadius.all(8),
                ),
                ft.Column(
                    [
                        ft.Text("Detalhes do serviço", size=get_responsive_font_size(13, width), weight="bold", color=service["highlight"]),
                        ft.Text(service["title"], size=get_responsive_font_size(25, width), weight="bold", color=COLORS["text_primary"]),
                        ft.Text(service["stack_note"], size=get_responsive_font_size(15, width), color=COLORS["text_secondary"]),
                    ],
                    spacing=4,
                    expand=True,
                ),
            ],
            spacing=14,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

        technologies = ft.Column(
            [
                ft.Text("Tecnologias e práticas", size=get_responsive_font_size(16, width), weight="bold", color=COLORS["text_primary"]),
                ft.Row(
                    [create_stack_chip(stack, service["highlight"]) for stack in service["stacks"]],
                    wrap=True,
                    spacing=8,
                    run_spacing=8,
                ),
            ],
            spacing=10,
        )

        scopes = ft.Column(
            [
                ft.Text("Escopos atendidos", size=get_responsive_font_size(17, width), weight="bold", color=COLORS["text_primary"]),
                *[
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.CHECK_CIRCLE, color=service["highlight"], size=get_responsive_font_size(18, width)),
                            ft.Text(item, size=get_responsive_font_size(14, width), color=COLORS["text_secondary"], expand=True),
                        ],
                        spacing=8,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    )
                    for item in service["use_cases"]
                ],
            ],
            spacing=8,
        )

        return ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [service_header, technologies],
                        spacing=get_responsive_spacing(16, width),
                    ),
                    col={"sm": 12, "md": 7, "lg": 7},
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Container(
                                content=scopes,
                                padding=ft.Padding.only(left=0 if is_mobile else get_responsive_padding(20, width)),
                            ),
                        ],
                    ),
                    border=ft.Border.only(
                        left=ft.BorderSide(0 if is_mobile else 1, COLORS["muted"]),
                    ),
                    col={"sm": 12, "md": 5, "lg": 5},
                ),
            ],
            spacing=get_responsive_spacing(18, width),
            run_spacing=get_responsive_spacing(18, width),
            vertical_alignment=ft.CrossAxisAlignment.START,
        )

    def update_selection_styles():
        for index, card in enumerate(service_cards):
            service = services[index]
            selected = index == selected_service["index"]
            card.bgcolor = ft.Colors.with_opacity(0.06, service["highlight"]) if selected else COLORS["surface"]
            card.border = ft.Border.all(2 if selected else 1, service["highlight"] if selected else COLORS["muted"])
            action_icon, action_text = service_actions[index]
            action_icon.icon = ft.Icons.KEYBOARD_ARROW_DOWN if selected else ft.Icons.ARROW_FORWARD
            action_text.value = "Selecionado" if selected else "Ver detalhes"

    def place_stack_panel():
        row_end = min(
            ((selected_service["index"] // cards_per_row) + 1) * cards_per_row,
            len(service_wrappers),
        )
        service_grid.controls = [
            *service_wrappers[:row_end],
            stack_panel_wrapper,
            *service_wrappers[row_end:],
        ]

    async def center_stack_panel():
        content_scroller = getattr(page, "_content_scroller", None)
        if content_scroller is None:
            return

        await content_scroller.scroll_to(
            scroll_key="service-detail",
            duration=260,
            curve=ft.AnimationCurve.EASE_OUT,
        )
        await content_scroller.scroll_to(
            delta=-96 if is_mobile else -170,
            duration=160,
            curve=ft.AnimationCurve.EASE_OUT,
        )

    def select_service(index):
        def handler(e):
            selected_service["index"] = index
            update_selection_styles()
            stack_panel.content = build_stack_panel()
            stack_panel.border = ft.Border.all(1, services[index]["highlight"])
            place_stack_panel()
            page.update()
            page.run_task(center_stack_panel)

        return handler

    services = [
        {
            "icon": ft.Icons.ARCHITECTURE,
            "title": "Arquitetura de Software",
            "description": "Definição de componentes, integrações, dados, segurança e operação para sistemas novos ou existentes.",
            "highlight": COLORS["primary"],
            "stacks": ["Python", "FastAPI", "PostgreSQL", "Docker", "Azure DevOps", "OCI", "Redis", "Observabilidade", "Testes"],
            "stack_note": "A GMF-tech estrutura a solução técnica a partir dos requisitos de negócio, dos sistemas envolvidos e das condições de operação.",
            "use_cases": ["Arquitetura de APIs e sistemas internos", "Modelagem de dados e integrações", "Modernização de aplicações em produção"],
        },
        {
            "icon": ft.Icons.ASSIGNMENT,
            "title": "Levantamento de Requisitos",
            "description": "Levantamento de objetivos, processos, regras de negócio, dependências e critérios de aceite.",
            "highlight": COLORS["secondary"],
            "stacks": ["Discovery", "User Stories", "Backlog", "Roadmap", "Mapeamento de processos", "Critérios de aceite", "Prototipação", "Documentação"],
            "stack_note": "O trabalho transforma necessidades dispersas em escopo priorizado, requisitos verificáveis e plano de execução.",
            "use_cases": ["Mapeamento de processos e sistemas", "Backlog técnico para produtos digitais", "Especificação para contratação e desenvolvimento"],
        },
        {
            "icon": ft.Icons.DEVELOPER_BOARD,
            "title": "IoT com Arduino",
            "description": "Prototipagem e desenvolvimento de soluções conectadas para captura, transmissão e análise de dados.",
            "highlight": COLORS["coral"],
            "stacks": ["Arduino", "Sensores", "Python", "APIs", "Flet", "Dashboards", "MQTT", "Dados", "Automação"],
            "stack_note": "O escopo integra dispositivos, protocolos, APIs e interfaces de acompanhamento em uma solução única.",
            "use_cases": ["Coleta de dados com sensores", "Telemetria e monitoramento", "Integração entre equipamentos e sistemas corporativos"],
        },
        {
            "icon": ft.Icons.PRECISION_MANUFACTURING,
            "title": "Prototipagem Eletrônica",
            "description": "Simulação e construção de provas de conceito para validar requisitos técnicos antes da produção.",
            "highlight": COLORS["accent_alt"],
            "stacks": ["Arduino", "SimulIDE", "Protoboard", "Sensores", "Python", "Flet", "Validação", "Documentação"],
            "stack_note": "A prototipagem reduz incertezas de hardware, integração e operação antes do investimento em escala.",
            "use_cases": ["Provas de conceito eletrônicas", "Validação de sensores e atuadores", "Protótipos para decisão de produto"],
        },
        {
            "icon": ft.Icons.LAPTOP_MAC,
            "title": "Desenvolvimento Web",
            "description": "Produtos digitais, portais, sistemas internos e sites institucionais responsivos.",
            "highlight": COLORS["accent"],
            "stacks": ["React", "Node.js", "Python 3.14", "Flet 0.86.5", "FastAPI", "PostgreSQL", "Cloudflare", "Docker", "Playwright"],
            "stack_note": "A arquitetura e a stack são definidas conforme requisitos de produto, integrações, segurança, prazo e operação.",
            "use_cases": ["Portais e sistemas web", "Sites institucionais e plataformas digitais", "Dashboards e aplicações orientadas a dados"],
        },
        {
            "icon": ft.Icons.PHONE_ANDROID,
            "title": "Desenvolvimento Mobile",
            "description": "Aplicativos multiplataforma para equipes internas, clientes e operações em campo.",
            "highlight": COLORS["secondary"],
            "stacks": ["Flet", "Python", "APIs", "Design responsivo", "Banco de dados", "Cloud", "CI/CD", "Testes"],
            "stack_note": "O desenvolvimento considera experiência de uso, integração com APIs, segurança e distribuição desde o planejamento.",
            "use_cases": ["Aplicativos internos de operação", "Aplicativos conectados a APIs", "Extensões mobile de produtos existentes"],
        },
        {
            "icon": ft.Icons.CLOUD,
            "title": "Cloud Computing",
            "description": "Infraestrutura, automação de entrega e observabilidade para aplicações em produção.",
            "highlight": COLORS["primary"],
            "stacks": ["AWS", "OCI", "Azure DevOps", "Docker", "Nginx", "CI/CD", "Observabilidade", "Backups", "Monitoramento"],
            "stack_note": "Ambientes e pipelines são documentados para reduzir intervenções manuais e dar previsibilidade à operação.",
            "use_cases": ["Infraestrutura para APIs e sistemas", "Automação de build, testes e implantação", "Monitoramento, logs e rotinas de backup"],
        },
        {
            "icon": ft.Icons.SECURITY,
            "title": "Segurança",
            "description": "Revisão de aplicações, integrações e processos de entrega com foco em riscos técnicos.",
            "highlight": COLORS["success"],
            "stacks": ["Hardening", "Revisão de código", "Testes", "Backups", "Logs", "CI/CD", "Docker", "Gestão de acessos"],
            "stack_note": "Os controles são incorporados ao desenvolvimento, à infraestrutura e às rotinas de operação.",
            "use_cases": ["Revisão de aplicações e APIs", "Padronização de implantação", "Controles de acesso, logs e recuperação"],
        },
        {
            "icon": ft.Icons.SMART_TOY,
            "title": "Automação e Inteligência Artificial",
            "description": "Automação de processos e recursos de IA integrados a sistemas e bases de conhecimento existentes.",
            "highlight": COLORS["coral"],
            "stacks": ["LLMs", "Agentes", "RAG", "Python", "APIs", "HTTPX", "PostgreSQL", "Redis", "Governança"],
            "stack_note": "A adoção é condicionada a um caso de uso definido, dados disponíveis, controles de acesso e critérios de avaliação.",
            "use_cases": ["Assistentes internos", "Extração e classificação de documentos", "Automação de backoffice e atendimento"],
        },
    ]

    technologies = [
        ("Python", "APIs, processamento de dados, integrações e automação.", ft.Icons.CODE, COLORS["secondary"]),
        ("Flet", "Apps multiplataforma com Python para web, desktop e mobile.", ft.Icons.DEVICES, COLORS["coral"]),
        ("React", "Interfaces web componentizadas para produtos e plataformas digitais.", ft.Icons.WEB, COLORS["accent"]),
        ("Node.js", "Serviços web, APIs e comunicação em tempo real.", ft.Icons.HUB, COLORS["success"]),
        ("PostgreSQL", "Banco de dados relacional de alta performance.", ft.Icons.STORAGE, COLORS["primary"]),
        ("ScyllaDB", "Banco NoSQL de alta performance e baixa latência.", ft.Icons.DATA_OBJECT, COLORS["secondary"]),
        ("Redis", "Cache distribuído, filas leves e banco em memória.", ft.Icons.MEMORY, COLORS["success"]),
        ("AWS", "Infraestrutura em nuvem escalável e confiável.", ft.Icons.CLOUD_QUEUE, COLORS["coral"]),
        ("Cloudflare", "Entrega, proteção e serviços de borda para aplicações web.", ft.Icons.CLOUD_DONE, COLORS["secondary"]),
        ("Azure DevOps", "CI/CD, backlog e gestão ágil de projetos.", ft.Icons.INTEGRATION_INSTRUCTIONS, COLORS["accent_alt"]),
        ("Apache ECharts", "Visualização de dados interativa via PyECharts.", ft.Icons.INSERT_CHART, COLORS["accent"]),
        ("IA e LLMs", "Assistentes, busca semântica e processamento de documentos.", ft.Icons.SMART_TOY, COLORS["coral"]),
    ]

    title_size = get_responsive_font_size(36, width)
    subtitle_size = get_responsive_font_size(17, width)
    grid_spacing = get_responsive_padding(12, width)
    horizontal_padding = get_responsive_padding(28 if is_mobile else 44, width)
    service_col = {"sm": 12, "md": 6, "lg": 4}
    tech_col = {"sm": 12, "md": 6, "lg": 4}

    stack_panel = ft.Container(
        content=build_stack_panel(),
        padding=ft.Padding.all(get_responsive_padding(26, width)),
        bgcolor=COLORS["surface"],
        border=ft.Border.all(1, services[0]["highlight"]),
        border_radius=ft.BorderRadius.all(8),
        shadow=get_shadow(),
    )
    stack_panel_wrapper = ft.Container(
        content=stack_panel,
        key="service-detail",
        col={"sm": 12, "md": 12, "lg": 12},
        padding=ft.Padding.symmetric(vertical=grid_spacing, horizontal=4),
        data="service-detail",
    )
    service_wrappers = [
        ft.Container(
            content=create_card(
                service["icon"],
                service["title"],
                service["description"],
                service["highlight"],
                index,
            ),
            col=service_col,
        )
        for index, service in enumerate(services)
    ]
    service_grid = ft.ResponsiveRow(
        spacing=grid_spacing,
        run_spacing=grid_spacing,
    )
    place_stack_panel()

    return ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Serviços de engenharia de software", size=title_size, weight="bold", color=ft.Colors.WHITE, text_align="center"),
                            ft.Text(
                                "A GMF-tech atua da definição do escopo à implantação, reunindo produto, desenvolvimento, integrações, dados e infraestrutura.",
                                size=subtitle_size,
                                color=ft.Colors.WHITE_70,
                                text_align="center",
                            ),
                        ],
                        horizontal_alignment="center",
                        spacing=12,
                    ),
                    bgcolor=COLORS["primary"],
                    padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(42, width)),
                    width=width,
                ),
                ft.Container(
                    content=service_grid,
                    padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(20, width)),
                    width=width,
                ),
                ft.Container(
                    content=ft.Text("Tecnologias e plataformas", size=title_size, weight="bold", color=COLORS["text_primary"], text_align="center"),
                    alignment=ft.Alignment.CENTER,
                    padding=ft.Padding.only(top=get_responsive_padding(20, width)),
                    width=width,
                ),
                ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=create_card(icon, title, description, highlight),
                                col=tech_col,
                            )
                            for title, description, icon, highlight in technologies
                        ],
                        spacing=grid_spacing,
                        run_spacing=grid_spacing,
                    ),
                    padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(20, width)),
                    width=width,
                ),
            ],
            spacing=0,
        ),
        bgcolor=COLORS["background"],
        width=width,
    )
