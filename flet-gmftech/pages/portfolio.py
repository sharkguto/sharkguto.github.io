import flet as ft
from theme import COLORS, get_shadow

def portfolio_content(page: ft.Page):
    def create_project_card(title, description, image_url, tech_stack):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Image(
                            src=image_url,
                            fit=ft.ImageFit.COVER,
                            width=None,
                            height=200,
                        ),
                        border_radius=ft.border_radius.only(
                            top_left=15, top_right=15
                        ),
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        expand=True,
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    title,
                                    size=24 if page.width > 600 else 20,
                                    weight="bold",
                                    color=COLORS["text_primary"],
                                ),
                                ft.Text(
                                    description,
                                    size=16 if page.width > 600 else 14,
                                    color=COLORS["text_secondary"],
                                ),
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.Text(
                                                    tech,
                                                    size=14,
                                                    color=ft.colors.WHITE,
                                                ),
                                                bgcolor=COLORS["primary"],
                                                padding=ft.padding.all(8),
                                                border_radius=ft.border_radius.all(15),
                                            )
                                            for tech in tech_stack
                                        ],
                                        wrap=True,
                                        spacing=10,
                                    ),
                                    margin=ft.margin.only(top=10),
                                ),
                            ],
                            spacing=10,
                        ),
                        padding=ft.padding.all(20),
                    ),
                ],
                spacing=0,
            ),
            bgcolor=COLORS["surface"],
            border_radius=ft.border_radius.all(15),
            shadow=get_shadow(),
            expand=True,
        )

    projects = [
        {
            "title": "Sistema de Gestão Empresarial",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
            "image_url": "/images/project1.png",  # Placeholder
            "tech_stack": ["Python", "PostgreSQL", "Redis", "AWS", "Docker"],
        },
        {
            "title": "App de Monitoramento IoT",
            "description": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse.",
            "image_url": "/images/project2.png",  # Placeholder
            "tech_stack": ["Python", "Flet", "Azure", "ScyllaDB"],
        },
    ]

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Portfólio",
                    size=32 if page.width > 600 else 24,
                    weight="bold",
                    color=COLORS["text_primary"],
                    text_align="center",
                ),
                ft.Text(
                    "Conheça alguns dos nossos projetos",
                    size=20 if page.width > 600 else 16,
                    color=COLORS["text_secondary"],
                    text_align="center",
                ),
                ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Container(
                                content=create_project_card(**project),
                                col=12 if page.width <= 600 else 6,
                                padding=10,
                            )
                            for project in projects
                        ],
                    ),
                    margin=ft.margin.only(top=30),
                ),
            ],
            scroll=None,
            horizontal_alignment="center",
            spacing=10,
        ),
        padding=ft.padding.symmetric(
            horizontal=20 if page.width > 600 else 10,
            vertical=20 if page.width > 600 else 15,
        ),
    ) 