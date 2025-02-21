import flet as ft
from pages.home import home_content
from pages.services import services_content
from pages.about import about_content
from pages.contact import contact_content

# Variáveis globais para header e footer
header = None
footer = None


def main(page: ft.Page):
    global header, footer
    # Configurações iniciais da página
    page.title = "GMF-tech - Outsourcing em TI"
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.scroll = "auto"
    page.padding = 0

    # Paleta de cores
    primary_color = ft.Colors.INDIGO_700
    secondary_color = ft.Colors.AMBER_600

    # Função para fechar o diálogo
    def close_dialog(e):
        if page.overlay:  # Verifica se há elementos no overlay
            # dialog = page.overlay[-1]  # Pega o último elemento (o diálogo aberto)
            page.close(page.login_dialog)  # Fecha o diálogo
        page.update()

    # Funções de login simuladas
    def login_with_google(e):
        page.snack_bar = ft.SnackBar(ft.Text("Login com Google iniciado..."), open=True)
        page.open(page.snack_bar)
        close_dialog(e)
        page.update()

    def login_with_apple(e):
        page.snack_bar = ft.SnackBar(ft.Text("Login com Apple iniciado..."), open=True)
        page.open(page.snack_bar)
        close_dialog(e)
        page.update()

    def login_with_x(e):
        page.snack_bar = ft.SnackBar(ft.Text("Login com X iniciado..."), open=True)
        page.open(page.snack_bar)
        close_dialog(e)
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

    def handle_login_click(e):
        page.login_dialog = ft.AlertDialog(
            modal=True,
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
            actions=[ft.TextButton("Cancelar", on_click=lambda e: close_dialog(e))],
            actions_alignment="end",
        )
        page.overlay.append(page.login_dialog)
        page.login_dialog.open = True
        page.update()

    def create_header(is_mobile):
        # Itens do menu para o mobile (submenu ou NavigationBar)
        navigation_items = [
            ft.PopupMenuItem(text="Início", on_click=go_to_home),
            ft.PopupMenuItem(text="Serviços", on_click=go_to_services),
            ft.PopupMenuItem(text="Sobre", on_click=go_to_about),
            ft.PopupMenuItem(text="Contato", on_click=go_to_contact),
            ft.PopupMenuItem(text="Login", on_click=handle_login_click),
        ]

        # Verifica o tamanho da tela
        if not is_mobile:
            # Header para desktop: textos ao longo da barra
            navigation_controls = ft.Row(
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
                        bgcolor=secondary_color,  # Substitua secondary_color pela cor definida no seu projeto
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
            )
        else:
            # Header para mobile: menu compacto (exemplo com PopupMenuButton)
            navigation_controls = ft.PopupMenuButton(
                icon=ft.Icons.MENU,
                items=navigation_items,
            )

        return ft.Container(
            content=ft.Row(
                [
                    ft.Text(
                        "GMF-tech",
                        size=30 if page.window.width > 600 else 20,
                        weight="bold",
                        color=ft.Colors.WHITE,
                    ),
                    navigation_controls,
                ],
                alignment="spaceBetween",
            ),
            bgcolor=primary_color,  # Substitua primary_color pela cor definida no seu projeto
            padding=ft.padding.symmetric(horizontal=20),
            border_radius=ft.border_radius.only(top_left=0, top_right=0),
        )

    def create_footer():
        # Calcula a altura máxima do footer como 15% da altura da janela
        max_height = (
            page.window.height * 0.15 if page.window.height else 100
        )  # Valor padrão caso a altura não esteja disponível

        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "GMF-tech - Outsourcing em TI",
                        size=16 if page.window.width > 600 else 14,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "contato@gmf-tech.com | (11) 9999-9999",
                        size=14 if page.window.width > 600 else 12,
                        color=ft.Colors.GREY_400,
                    ),
                    ft.Text(
                        "© 2025 GMF-tech. Todos os direitos reservados.",
                        size=12 if page.window.width > 600 else 10,
                        color=ft.Colors.GREY_400,
                    ),
                ],
                alignment="center",
                spacing=5 if page.window.width > 600 else 3,
            ),
            bgcolor=primary_color,  # Substitua primary_color pela cor definida no seu projeto
            padding=ft.padding.symmetric(vertical=10, horizontal=20),
            border_radius=ft.border_radius.only(top_left=0, top_right=0),
            alignment=ft.alignment.center,
            height=max_height,  # Limita a altura a 15% da tela
            expand=False,  # Impede que o container expanda além do necessário
        )

    is_mobile = page.width <= 600

    # Inicializar header e footer
    header = create_header(is_mobile)
    footer = create_footer()

    # Listener para redimensionamento da janela
    def on_resize(e):
        footer.content = create_footer().content
        is_mobile = page.width <= 600
        header.content = create_header(is_mobile).content
        page.update()

    page.on_resized = on_resize

    # Renderizar diferentes páginas com base na rota
    def route_change(route):
        page.views.clear()

        # Conteúdo principal (varia por rota)
        main_content = None

        if page.route == "/":
            main_content = home_content(page)
        elif page.route == "/services":
            main_content = services_content(page)
        elif page.route == "/about":
            main_content = about_content(page)
        elif page.route == "/contact":
            main_content = contact_content(page)

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

    # # Chama on_resize uma vez após o carregamento da página
    # def on_page_load(e):
    #     on_resize(None)

    # Usa um evento como on_route_change para garantir o carregamento inicial
    # page.on_route_change = on_page_load


# Executando o app
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
