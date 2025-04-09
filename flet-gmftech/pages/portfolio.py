import flet as ft
from theme import COLORS, get_shadow

def portfolio_content(page: ft.Page):
    projects = [
        {
            "title": "Sistema de Monitoramento de Cotações",
            "description": """
Desenvolvemos uma solução robusta e em tempo real para monitoramento de cotações de moedas, 
utilizando tecnologias modernas como Python e ScyllaDB. O sistema processa milhares de 
transações por segundo, oferecendo:

• Visualização em tempo real das cotações
• Análise histórica com gráficos interativos
• Alta performance com latência < 100ms
• Escalabilidade horizontal automática
• Interface moderna e responsiva
""",
            "image": "/images/chart-project.jpg",
            "technologies": ["Python", "ScyllaDB", "Flet", "Docker", "Kubernetes"]
        },
        {
            "title": "Website Institucional GMF-tech",
            "description": """
Criação de uma presença digital moderna e profissional para a GMF-tech, com foco em:

• Design responsivo e adaptativo
• Performance otimizada (97+ no PageSpeed)
• Acessibilidade WCAG 2.1
• Interface moderna com animações suaves
• Integração com sistemas de analytics

O site foi desenvolvido utilizando as melhores práticas de desenvolvimento web e SEO, 
resultando em uma experiência excepcional para os usuários.
""",
            "image": "/images/website-project.jpg",
            "technologies": ["Python", "Flet", "Material Design", "Git", "CI/CD"]
        }
    ]

    def create_project_card(project):
        # Ajusta o tamanho da imagem baseado na largura da tela
        image_width = 400 if page.width > 600 else page.width - 80
        image_height = 250 if page.width > 600 else 200

        return ft.Container(
            content=ft.Column(
                [
                    ft.Container(
                        content=ft.Image(
                            src=project["image"],
                            fit=ft.ImageFit.COVER,
                            width=image_width,
                            height=image_height,
                            border_radius=ft.border_radius.all(8),
                        ),
                        margin=ft.margin.only(bottom=20),
                    ),
                    ft.Text(
                        project["title"],
                        size=24 if page.width > 600 else 20,
                        weight="bold",
                        color=COLORS["text_primary"],
                    ),
                    ft.Text(
                        project["description"],
                        size=16 if page.width > 600 else 14,
                        color=COLORS["text_secondary"],
                        text_align="justify",
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Container(
                                    content=ft.Text(
                                        tech,
                                        size=14 if page.width > 600 else 12,
                                        color=COLORS["primary"],
                                        weight="w500",
                                    ),
                                    bgcolor=COLORS["surface"],
                                    padding=ft.padding.all(8),
                                    border_radius=ft.border_radius.all(4),
                                    margin=ft.margin.only(right=8, bottom=8),
                                )
                                for tech in project["technologies"]
                            ],
                            wrap=True,
                            spacing=0,
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        margin=ft.margin.only(top=20),
                    ),
                ],
                spacing=15,
            ),
            bgcolor=ft.colors.WHITE,
            padding=30 if page.width > 600 else 20,
            border_radius=ft.border_radius.all(15),
            shadow=get_shadow(),
            margin=ft.margin.only(bottom=30),
        )

    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Nossos Projetos",
                    size=32 if page.width > 600 else 24,
                    weight="bold",
                    color=COLORS["text_primary"],
                    text_align="center",
                ),
                ft.Text(
                    "Conheça alguns dos nossos casos de sucesso",
                    size=16 if page.width > 600 else 14,
                    color=COLORS["text_secondary"],
                    text_align="center",
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            content=create_project_card(project),
                            col={"sm": 12, "md": 6},
                            padding=10,
                        )
                        for project in projects
                    ],
                    alignment="center",
                ),
            ],
            expand=True,
            alignment="start",
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 400),
        padding=ft.padding.symmetric(horizontal=40 if page.width > 600 else 20),
    ) 