import flet as ft
from theme import COLORS, get_shadow, get_responsive_font_size, get_responsive_padding, get_responsive_spacing
from utils.responsive import ResponsiveConfig

def portfolio_content(page: ft.Page):
    projects = [
        {
            "title": "Velejar Fácil",
            "description": """
Plataforma inovadora para controle de embarcações, conectando donos de marinas e usuários finais. Permite o gerenciamento de barcos, reservas e passeios de fim de semana, funcionando como um "Uber de barcos". Principais recursos:

• Gestão de frota para marinas
• Reserva e aluguel de embarcações por usuários
• Pagamentos integrados e avaliações
• Interface intuitiva para web e mobile
• Segurança e rastreamento em tempo real
""",
            "image": "/images/velejar_facil.jpg",
            "technologies": ["Python", "Flet", "APIs", "Cloud", "Banco de Dados"]
        },
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
        # Detect breakpoint for responsive behavior
        breakpoint = ResponsiveConfig.get_breakpoint(page.width or 1024)
        
        # Calculate responsive image dimensions
        # Desktop: 400px, Tablet: 350px, Mobile: (viewport_width - 80px)
        if breakpoint.value == "mobile":
            image_width = (page.width or 400) - 80
            image_height = 200
        elif breakpoint.value == "tablet":
            image_width = 350
            image_height = 220
        else:  # desktop
            image_width = 400
            image_height = 250
        
        # Calculate responsive values
        card_padding = get_responsive_padding(30, page.width or 1024)
        title_size = get_responsive_font_size(24, page.width or 1024)
        description_size = get_responsive_font_size(16, page.width or 1024)
        tech_tag_size = get_responsive_font_size(14, page.width or 1024)
        tech_tag_padding = get_responsive_padding(8, page.width or 1024)
        spacing_between_elements = get_responsive_spacing(15, page.width or 1024)
        margin_bottom = get_responsive_spacing(20, page.width or 1024)
        tech_margin_top = get_responsive_spacing(20, page.width or 1024)
        tech_tag_spacing = get_responsive_spacing(8, page.width or 1024)

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
                        margin=ft.margin.only(bottom=margin_bottom),
                    ),
                    ft.Text(
                        project["title"],
                        size=title_size,
                        weight="bold",
                        color=COLORS["text_primary"],
                    ),
                    ft.Text(
                        project["description"],
                        size=description_size,
                        color=COLORS["text_secondary"],
                        text_align="justify",
                    ),
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Container(
                                    content=ft.Text(
                                        tech,
                                        size=tech_tag_size,
                                        color=COLORS["primary"],
                                        weight="w500",
                                    ),
                                    bgcolor=COLORS["surface"],
                                    padding=ft.padding.all(tech_tag_padding),
                                    border_radius=ft.border_radius.all(4),
                                    margin=ft.margin.only(right=tech_tag_spacing, bottom=tech_tag_spacing),
                                )
                                for tech in project["technologies"]
                            ],
                            wrap=True,
                            spacing=0,
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        margin=ft.margin.only(top=tech_margin_top),
                    ),
                ],
                spacing=spacing_between_elements,
            ),
            bgcolor=ft.Colors.WHITE,
            padding=card_padding,
            border_radius=ft.border_radius.all(15),
            shadow=get_shadow(),
            margin=ft.margin.only(bottom=30),
        )

    # Detect breakpoint for main container
    breakpoint = ResponsiveConfig.get_breakpoint(page.width or 1024)
    
    # Calculate responsive values for main container
    title_size = get_responsive_font_size(32, page.width or 1024)
    subtitle_size = get_responsive_font_size(16, page.width or 1024)
    container_padding = get_responsive_padding(40, page.width or 1024)
    section_spacing = get_responsive_spacing(20, page.width or 1024)
    
    # Configure ResponsiveRow columns based on breakpoint
    # Mobile: 1 column (12/12), Tablet & Desktop: 2 columns (6/12 each)
    col_config = {"sm": 12, "md": 6, "lg": 6}
    
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    "Nossos Projetos",
                    size=title_size,
                    weight="bold",
                    color=COLORS["text_primary"],
                    text_align="center",
                ),
                ft.Text(
                    "Conheça alguns dos nossos casos de sucesso",
                    size=subtitle_size,
                    color=COLORS["text_secondary"],
                    text_align="center",
                ),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            content=create_project_card(project),
                            col=col_config,
                            padding=10,
                        )
                        for project in projects
                    ],
                    alignment="center",
                ),
            ],
            expand=True,
            alignment="start",
            spacing=section_spacing,
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else 400, 400),
        padding=ft.padding.symmetric(horizontal=container_padding),
    ) 