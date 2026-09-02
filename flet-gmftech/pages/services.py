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
    service_previews = []
    stack_panel = ft.Container()

    def create_card(icon, title, description, highlight=COLORS["secondary"], index=None):
        card_padding = get_responsive_padding(22, width)
        icon_size = get_responsive_font_size(34, width)
        title_size = get_responsive_font_size(19, width)
        description_size = get_responsive_font_size(15, width)
        selected = index == selected_service["index"]
        preview = ft.Container(height=0)
        if index is not None:
            preview = ft.Container(
                content=ft.Row(
                    [create_stack_chip(stack, highlight) for stack in services[index]["stacks"][:4]],
                    wrap=True,
                    spacing=6,
                    run_spacing=6,
                ),
                visible=selected,
            )
            service_previews.append(preview)

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
                            ft.Icon(ft.Icons.TOUCH_APP, size=get_responsive_font_size(16, width), color=highlight),
                            ft.Text("Ver stacks", size=get_responsive_font_size(13, width), color=highlight, weight="bold"),
                        ],
                        spacing=6,
                    ) if index is not None else ft.Container(height=0),
                    preview,
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
        return ft.Column(
            [
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Icon(service["icon"], color=service["highlight"], size=get_responsive_font_size(30, width)),
                            bgcolor=ft.Colors.with_opacity(0.1, service["highlight"]),
                            padding=ft.Padding.all(10),
                            border_radius=ft.BorderRadius.all(8),
                        ),
                        ft.Column(
                            [
                                ft.Text("Stacks para " + service["title"], size=get_responsive_font_size(25, width), weight="bold", color=COLORS["text_primary"]),
                                ft.Text(service["stack_note"], size=get_responsive_font_size(15, width), color=COLORS["text_secondary"]),
                            ],
                            spacing=4,
                            expand=True,
                        ),
                    ],
                    spacing=14,
                    vertical_alignment=ft.CrossAxisAlignment.START,
                ),
                ft.Row(
                    [create_stack_chip(stack, service["highlight"]) for stack in service["stacks"]],
                    wrap=True,
                    spacing=8,
                    run_spacing=8,
                ),
                ft.Divider(color=COLORS["muted"], height=1),
                ft.Column(
                    [
                        ft.Text("Aplicações típicas", size=get_responsive_font_size(17, width), weight="bold", color=COLORS["text_primary"]),
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
                ),
            ],
            spacing=get_responsive_spacing(18, width),
        )

    def update_selection_styles():
        for index, card in enumerate(service_cards):
            service = services[index]
            selected = index == selected_service["index"]
            card.bgcolor = ft.Colors.with_opacity(0.06, service["highlight"]) if selected else COLORS["surface"]
            card.border = ft.Border.all(2 if selected else 1, service["highlight"] if selected else COLORS["muted"])
            service_previews[index].visible = selected

    def select_service(index):
        def handler(e):
            selected_service["index"] = index
            update_selection_styles()
            stack_panel.content = build_stack_panel()
            page.update()

        return handler

    services = [
        {
            "icon": ft.Icons.ARCHITECTURE,
            "title": "Arquitetura de Sistemas",
            "description": "Especialidade em desenhar sistemas Python escaláveis, integrados e preparados para produção desde o início.",
            "highlight": COLORS["primary"],
            "stacks": ["Python", "FastAPI", "PostgreSQL", "Docker", "Azure DevOps", "OCI", "Redis", "Observabilidade", "Testes"],
            "stack_note": "Minha especialidade é ligar negócio, dados, APIs, integrações, infraestrutura e entrega em uma arquitetura clara e sustentável.",
            "use_cases": ["Arquitetura de APIs e sistemas internos", "Modelagem de dados, integrações e fluxos críticos", "Modernização de sistemas com deploy, testes e operação"],
        },
        {
            "icon": ft.Icons.ASSIGNMENT,
            "title": "Levantamento de Requisitos",
            "description": "Análise detalhada, documentação e priorização das necessidades do seu projeto.",
            "highlight": COLORS["secondary"],
            "stacks": ["Discovery", "User Stories", "Backlog", "Roadmap", "Protótipos Flet", "Critérios de aceite", "Documentação", "Automação com IA"],
            "stack_note": "Organizo o problema, documento os fluxos e uso IA para acelerar análise, priorização e documentação.",
            "use_cases": ["Mapeamento de processos e sistemas", "Backlog técnico para MVPs e produtos", "Documentação assistida por IA"],
        },
        {
            "icon": ft.Icons.DEVELOPER_BOARD,
            "title": "IoT com Arduino",
            "description": "Desenvolvimento de soluções IoT com hardware Arduino e sistemas conectados.",
            "highlight": COLORS["coral"],
            "stacks": ["Arduino", "Sensores", "Python", "APIs", "Flet", "Dashboards", "MQTT", "Dados", "Automação"],
            "stack_note": "Da bancada ao painel: protótipos conectados, coleta de dados e interfaces para acompanhar tudo.",
            "use_cases": ["Coleta de dados com sensores", "Painéis de monitoramento", "Integração entre hardware e sistemas"],
        },
        {
            "icon": ft.Icons.PRECISION_MANUFACTURING,
            "title": "Prototipagem Eletrônica",
            "description": "Simulação e prototipagem para validação rápida de ideias e projetos.",
            "highlight": COLORS["accent_alt"],
            "stacks": ["Arduino", "SimulIDE", "Protoboard", "Sensores", "Python", "Flet", "Validação", "Documentação"],
            "stack_note": "Valido ideias antes de escalar investimento, conectando protótipo, software e dados.",
            "use_cases": ["Prova de conceito eletrônica", "Validação de sensores e atuadores", "Demonstrações técnicas para produto"],
        },
        {
            "icon": ft.Icons.LAPTOP_MAC,
            "title": "Desenvolvimento Web",
            "description": "Sites, aplicações web e dashboards modernos, responsivos e prontos para deploy.",
            "highlight": COLORS["accent"],
            "stacks": ["Python 3.14", "Flet 0.86.5", "WebAssembly", "Pyodide 314.0.3", "GitHub Pages", "Docker", "Nginx", "Playwright"],
            "stack_note": "A web continua sendo Flet-first: Python no navegador, bundle estático e validação real antes de publicar.",
            "use_cases": ["Sites institucionais em Flet", "Portais e backoffices", "Dashboards com PyECharts/Apache ECharts"],
        },
        {
            "icon": ft.Icons.PHONE_ANDROID,
            "title": "Desenvolvimento Mobile",
            "description": "Aplicativos nativos e híbridos para iOS e Android, com foco em produto e operação.",
            "highlight": COLORS["secondary"],
            "stacks": ["Flet", "Python", "APIs", "Design responsivo", "Banco de dados", "Cloud", "CI/CD", "Testes"],
            "stack_note": "Uso Flet e Python para acelerar apps multiplataforma sem perder clareza de arquitetura.",
            "use_cases": ["Apps internos de operação", "Aplicativos conectados a APIs", "Interfaces mobile para produtos existentes"],
        },
        {
            "icon": ft.Icons.CLOUD,
            "title": "Cloud Computing",
            "description": "Soluções em nuvem para escalabilidade, performance, disponibilidade e deploy confiável.",
            "highlight": COLORS["primary"],
            "stacks": ["AWS", "OCI", "Azure DevOps", "Docker", "Nginx", "CI/CD", "Observabilidade", "Backups", "Monitoramento"],
            "stack_note": "Organizo ambientes reproduzíveis, pipelines confiáveis e infraestrutura pronta para evoluir sem improviso.",
            "use_cases": ["Infraestrutura para APIs e sistemas", "Automação de build, testes e deploy", "Ambientes de produção com monitoramento e rotina de backup"],
        },
        {
            "icon": ft.Icons.SECURITY,
            "title": "Segurança",
            "description": "Proteção, revisão técnica e boas práticas para seus dados, aplicações e integrações.",
            "highlight": COLORS["success"],
            "stacks": ["Hardening", "Revisão de código", "Testes", "Backups", "Logs", "CI/CD", "Docker", "Governança de IA"],
            "stack_note": "Segurança aplicada ao ciclo real: código, dados, deploy, automações e uso responsável de IA.",
            "use_cases": ["Revisão de aplicações e APIs", "Padronização de deploy seguro", "Controles para automações com IA"],
        },
        {
            "icon": ft.Icons.SMART_TOY,
            "title": "Consultoria e Automação com IA",
            "description": "Copilots, agentes, análise de documentos e automações inteligentes para reduzir tarefas manuais.",
            "highlight": COLORS["coral"],
            "stacks": ["LLMs", "Agentes", "RAG", "Python", "APIs", "HTTPX", "PostgreSQL", "Redis", "Governança"],
            "stack_note": "IA entra como camada prática sobre os serviços que você já presta: análise, automação, atendimento e decisão.",
            "use_cases": ["Copilots internos", "Extração e classificação de documentos", "Automação de backoffice, CRM e atendimento"],
        },
    ]

    technologies = [
        ("Python", "Desenvolvimento backend robusto, automações, APIs e IA aplicada.", ft.Icons.CODE, COLORS["secondary"]),
        ("Flet", "Apps multiplataforma com Python para web, desktop e mobile.", ft.Icons.DEVICES, COLORS["coral"]),
        ("PostgreSQL", "Banco de dados relacional de alta performance.", ft.Icons.STORAGE, COLORS["primary"]),
        ("ScyllaDB", "Banco NoSQL de alta performance e baixa latência.", ft.Icons.DATA_OBJECT, COLORS["secondary"]),
        ("Redis", "Cache distribuído, filas leves e banco em memória.", ft.Icons.MEMORY, COLORS["success"]),
        ("AWS", "Infraestrutura em nuvem escalável e confiável.", ft.Icons.CLOUD_QUEUE, COLORS["coral"]),
        ("Azure DevOps", "CI/CD, backlog e gestão ágil de projetos.", ft.Icons.INTEGRATION_INSTRUCTIONS, COLORS["accent_alt"]),
        ("Apache ECharts", "Visualização de dados interativa via PyECharts.", ft.Icons.INSERT_CHART, COLORS["accent"]),
        ("IA e LLMs", "Copilots, agentes, RAG e automações inteligentes.", ft.Icons.SMART_TOY, COLORS["coral"]),
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
        border=ft.Border.all(1, COLORS["muted"]),
        border_radius=ft.BorderRadius.all(8),
        shadow=get_shadow(),
    )

    return ft.Container(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("Nossos Serviços", size=title_size, weight="bold", color=ft.Colors.WHITE, text_align="center"),
                            ft.Text(
                                "Tudo que a GMF-tech já entrega em software, web, mobile, IoT, cloud e segurança, agora também com consultoria e automação com IA.",
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
                    content=ft.ResponsiveRow(
                        [
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
                        ],
                        spacing=grid_spacing,
                        run_spacing=grid_spacing,
                    ),
                    padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(28, width)),
                    width=width,
                ),
                ft.Container(
                    content=stack_panel,
                    padding=ft.Padding.symmetric(horizontal=horizontal_padding, vertical=get_responsive_padding(10, width)),
                    width=width,
                ),
                ft.Container(
                    content=ft.Text("Stack principal", size=title_size, weight="bold", color=COLORS["text_primary"], text_align="center"),
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
