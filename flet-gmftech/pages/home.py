import flet as ft


def home_content(page):
    primary_color = ft.Colors.INDIGO_700
    secondary_color = ft.Colors.AMBER_600

    def go_to_contact(e):
        page.go("/contact")

    return ft.Column(
        [
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            "Soluções de TI Sob Medida",
                            size=48 if page.window.width > 600 else 30,
                            weight="bold",
                            color=ft.Colors.WHITE,
                            text_align="center",
                        ),
                        ft.Text(
                            "Aceleramos seu sucesso com outsourcing especializado",
                            size=20 if page.window.width > 600 else 16,
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
                            on_click=go_to_contact,  # Navega para "/contact"
                        ),
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                    spacing=20 if page.window.width > 600 else 10,
                ),
                padding=ft.padding.symmetric(
                    vertical=60 if page.window.width > 600 else 30, horizontal=20
                ),
                bgcolor=primary_color,
                height=400 if page.window.width > 600 else 250,
                alignment=ft.alignment.center,
            )
        ]
    )
