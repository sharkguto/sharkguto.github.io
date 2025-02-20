import flet as ft


def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "GMF-tech - Outsourcing em TI"
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.scroll = "auto"
    page.padding = 0

    # Paleta de cores
    primary_color = ft.Colors.INDIGO_700
    secondary_color = ft.Colors.AMBER_600

    # Função para fechar o diálogo
    def close_dialog():
        page.dialog.open = False
        page.update()

    # Funções de login simuladas
    def login_with_google(e):
        page.snack_bar = ft.SnackBar(ft.Text("Login com Google iniciado..."), open=True)
        close_dialog()
        page.update()

    def login_with_apple(e):
        page.snack_bar = ft.SnackBar(ft.Text("Login com Apple iniciado..."), open=True)
        close_dialog()
        page.update()

    def login_with_x(e):
        page.snack_bar = ft.SnackBar(ft.Text("Login com X iniciado..."), open=True)
        close_dialog()
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

    # Função para abrir o diálogo de login
    def handle_login_click(e):
        login_dialog = ft.AlertDialog(
            title=ft.Text("Login na Plataforma de Cursos", size=20, weight="bold"),
            content=ft.Column(
                [
                    ft.Text(
                        "Escolha como deseja entrar:", size=16, color=ft.Colors.GREY_700
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.ACCOUNT_CIRCLE, color=ft.Colors.WHITE),
                                ft.Text("Login com Google", color=ft.Colors.WHITE),
                            ]
                        ),
                        bgcolor=ft.Colors.RED_600,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=ft.padding.symmetric(vertical=10),
                        ),
                        on_click=login_with_google,
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.APPLE, color=ft.Colors.WHITE),
                                ft.Text("Login com Apple", color=ft.Colors.WHITE),
                            ]
                        ),
                        bgcolor=ft.Colors.BLACK,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=ft.padding.symmetric(vertical=10),
                        ),
                        on_click=login_with_apple,
                    ),
                    ft.ElevatedButton(
                        content=ft.Row(
                            [
                                ft.Icon(
                                    ft.Icons.ALTERNATE_EMAIL, color=ft.Colors.WHITE
                                ),
                                ft.Text("Login com X", color=ft.Colors.WHITE),
                            ]
                        ),
                        bgcolor=ft.Colors.BLUE_GREY_800,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=8),
                            padding=ft.padding.symmetric(vertical=10),
                        ),
                        on_click=login_with_x,
                    ),
                ],
                tight=True,
                spacing=10,
            ),
            actions=[ft.TextButton("Cancelar", on_click=lambda e: close_dialog())],
            actions_alignment="end",
        )

        page.dialog = login_dialog
        login_dialog.open = True
        page.update()

    # Header fixo (mantido em todas as páginas)
    header = ft.Container(
        content=ft.Row(
            [
                ft.Text("GMF-tech", size=30, weight="bold", color=ft.Colors.WHITE),
                ft.Row(
                    [
                        ft.TextButton(
                            "Início",
                            style=ft.ButtonStyle(color=ft.Colors.WHITE),
                            on_click=go_to_home,
                        ),
                        ft.TextButton(
                            "Serviços",
                            style=ft.ButtonStyle(color=ft.Colors.WHITE),
                            on_click=go_to_services,
                        ),
                        ft.TextButton(
                            "Sobre",
                            style=ft.ButtonStyle(color=ft.Colors.WHITE),
                            on_click=go_to_about,
                        ),
                        ft.TextButton(
                            "Contato",
                            style=ft.ButtonStyle(color=ft.Colors.WHITE),
                            on_click=go_to_contact,
                        ),
                        ft.ElevatedButton(
                            "Login",
                            bgcolor=secondary_color,
                            color=ft.Colors.WHITE,
                            on_click=handle_login_click,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=8),
                                padding=ft.padding.symmetric(horizontal=15, vertical=8),
                            ),
                        ),
                    ],
                    alignment="end",
                    spacing=10,
                ),
            ],
            alignment="spaceBetween",
        ),
        bgcolor=primary_color,
        padding=ft.padding.symmetric(horizontal=20),
        border_radius=ft.border_radius.only(top_left=0, top_right=0),
    )

    # Footer fixo (mantido em todas as páginas)
    footer = ft.Container(
        content=ft.Column(
            [
                ft.Text("GMF-tech - Outsourcing em TI", color=ft.Colors.WHITE),
                ft.Text(
                    "contato@gmf-tech.com | (11) 9999-9999", color=ft.Colors.GREY_400
                ),
                ft.Text(
                    "© 2025 GMF-tech. Todos os direitos reservados.",
                    color=ft.Colors.GREY_400,
                ),
            ],
            alignment="center",
            spacing=10,
        ),
        bgcolor=primary_color,
        padding=ft.padding.symmetric(vertical=20, horizontal=20),
        border_radius=ft.border_radius.only(top_left=0, top_right=0),
    )

    # Renderizar diferentes páginas com base na rota
    def route_change(route):
        page.views.clear()

        # Conteúdo principal (varia por rota)
        main_content = None

        if page.route == "/":
            # Página Inicial (apenas Hero Section)
            main_content = ft.Column(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Soluções de TI Sob Medida",
                                    size=48,
                                    weight="bold",
                                    color=ft.Colors.WHITE,
                                    text_align="center",
                                ),
                                ft.Text(
                                    "Aceleramos seu sucesso com outsourcing especializado",
                                    size=20,
                                    color=ft.Colors.GREY_300,
                                    text_align="center",
                                ),
                                ft.ElevatedButton(
                                    "Fale Conosco",
                                    bgcolor=secondary_color,
                                    color=ft.Colors.WHITE,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=8)
                                    ),
                                ),
                            ],
                            alignment="center",
                            horizontal_alignment="center",
                            spacing=20,
                        ),
                        padding=ft.padding.symmetric(vertical=60, horizontal=20),
                        bgcolor=primary_color,
                        height=400 if page.window.width > 600 else 300,
                        alignment=ft.alignment.center,
                    )
                ]
            )
        elif page.route == "/services":
            # Página de Serviços (cards de "Nossos Serviços")
            main_content = ft.Column(
                [
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Nossos Serviços",
                                    size=36,
                                    weight="bold",
                                    text_align="center",
                                ),
                                ft.Row(
                                    [
                                        ft.Card(
                                            content=ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Icon(
                                                            ft.Icons.DEVELOPER_BOARD,
                                                            size=40,
                                                            color=primary_color,
                                                        ),
                                                        ft.Text(
                                                            "Desenvolvimento",
                                                            weight="bold",
                                                            size=20,
                                                        ),
                                                        ft.Text(
                                                            "Equipes dedicadas para seus projetos",
                                                            color=ft.Colors.GREY_700,
                                                        ),
                                                    ],
                                                    alignment="center",
                                                    spacing=10,
                                                ),
                                                padding=20,
                                            ),
                                            elevation=5,
                                            width=300
                                            if page.window.width > 900
                                            else 250,
                                            margin=ft.margin.all(10),
                                        ),
                                        ft.Card(
                                            content=ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Icon(
                                                            ft.Icons.SUPPORT_AGENT,
                                                            size=40,
                                                            color=primary_color,
                                                        ),
                                                        ft.Text(
                                                            "Suporte TI",
                                                            weight="bold",
                                                            size=20,
                                                        ),
                                                        ft.Text(
                                                            "Atendimento 24/7 para sua empresa",
                                                            color=ft.Colors.GREY_700,
                                                        ),
                                                    ],
                                                    alignment="center",
                                                    spacing=10,
                                                ),
                                                padding=20,
                                            ),
                                            elevation=5,
                                            width=300
                                            if page.window.width > 900
                                            else 250,
                                            margin=ft.margin.all(10),
                                        ),
                                        ft.Card(
                                            content=ft.Container(
                                                content=ft.Column(
                                                    [
                                                        ft.Icon(
                                                            ft.Icons.CLOUD,
                                                            size=40,
                                                            color=primary_color,
                                                        ),
                                                        ft.Text(
                                                            "Cloud Services",
                                                            weight="bold",
                                                            size=20,
                                                        ),
                                                        ft.Text(
                                                            "Soluções em nuvem escaláveis",
                                                            color=ft.Colors.GREY_700,
                                                        ),
                                                    ],
                                                    alignment="center",
                                                    spacing=10,
                                                ),
                                                padding=20,
                                            ),
                                            elevation=5,
                                            width=300
                                            if page.window.width > 900
                                            else 250,
                                            margin=ft.margin.all(10),
                                        ),
                                    ],
                                    alignment="center",
                                    wrap=True,
                                    spacing=20,
                                ),
                            ]
                        ),
                        padding=ft.padding.symmetric(vertical=50, horizontal=20),
                        bgcolor=ft.Colors.WHITE,
                    )
                ]
            )
        elif page.route == "/about":
            # Página Sobre
            main_content = ft.Column(
                [
                    ft.Container(
                        content=ft.Text(
                            "Página Sobre",
                            size=30,
                            weight="bold",
                            color=ft.Colors.WHITE,
                            text_align="center",
                        ),
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Saiba mais sobre a GMF-tech...",
                            size=20,
                            color=ft.Colors.GREY_300,
                        ),
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                    ),
                ]
            )
        elif page.route == "/contact":
            # Página Contato
            main_content = ft.Column(
                [
                    ft.Container(
                        content=ft.Text(
                            "Página Contato",
                            size=30,
                            weight="bold",
                            color=ft.Colors.WHITE,
                            text_align="center",
                        ),
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Entre em contato com a GMF-tech...",
                            size=20,
                            color=ft.Colors.GREY_300,
                        ),
                        padding=20,
                        bgcolor=ft.Colors.WHITE,
                    ),
                ]
            )

        # Adicionar o header fixo, o conteúdo principal e o footer à view
        if main_content:
            page.views.append(
                ft.View(
                    route if route else "/",
                    [
                        header,  # Header fixo no topo
                        ft.Container(
                            content=main_content,
                            expand=True,  # Permite que o conteúdo ocupe o espaço disponível
                            bgcolor=ft.Colors.WHITE,  # Fundo branco para o conteúdo principal
                        ),
                        footer,  # Footer fixo na base
                    ],
                )
            )

        page.update()

    # Adicionando o listener para mudanças de rota
    page.on_route_change = route_change
    page.go(page.route if page.route else "/")


# Executando o app
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
