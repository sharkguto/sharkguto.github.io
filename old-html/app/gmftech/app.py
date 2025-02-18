import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class OutsourcingApp(toga.App):
    def startup(self):
        # Container principal com layout flexível
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1))

        # Cabeçalho
        header = toga.Label("Empresa de Outsourcing de TI", style=Pack(padding=5))
        main_box.add(header)

        # Barra de navegação simples (apenas exemplificada)
        nav_box = toga.Box(style=Pack(direction=ROW, padding=5, alignment="center"))
        btn_home = toga.Button("Home", on_press=self.show_home, style=Pack(padding=5))
        btn_services = toga.Button(
            "Serviços", on_press=self.show_services, style=Pack(padding=5)
        )
        btn_about = toga.Button(
            "Sobre", on_press=self.show_about, style=Pack(padding=5)
        )
        btn_contact = toga.Button(
            "Contato", on_press=self.show_contact, style=Pack(padding=5)
        )

        for btn in (btn_home, btn_services, btn_about, btn_contact):
            nav_box.add(btn)
        main_box.add(nav_box)

        # Área de conteúdo: usamos uma Box que conterá vários Labels
        self.content_box = toga.Box(style=Pack(direction=COLUMN, padding=5, flex=1))
        main_box.add(self.content_box)

        # Cria a janela principal
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        # Exibe o conteúdo inicial (Home)
        self.show_home(None)

    def clear_content(self):
        # Remove todos os widgets anteriores da content_box
        self.content_box.children.clear()

    def show_home(self, widget):
        self.clear_content()
        paragraphs = [
            "Bem-vindo à nossa empresa de Outsourcing de TI!",
            "",
            "Oferecemos soluções inovadoras e personalizadas para atender às necessidades "
            "tecnológicas de sua empresa, com foco em qualidade e eficiência.",
            "",
            "Navegue pelas seções para saber mais sobre nossos serviços, sobre nós e como entrar em contato.",
        ]
        for para in paragraphs:
            lbl = toga.Label(para, style=Pack(padding_bottom=5))
            self.content_box.add(lbl)

    def show_services(self, widget):
        self.clear_content()
        paragraphs = [
            "Serviços:",
            "- Desenvolvimento de Software",
            "- Gestão de Infraestrutura",
            "- Consultoria em TI",
            "- Suporte Técnico",
        ]
        for para in paragraphs:
            lbl = toga.Label(para, style=Pack(padding_bottom=5))
            self.content_box.add(lbl)

    def show_about(self, widget):
        self.clear_content()
        paragraphs = [
            "Sobre Nós:",
            "Somos uma empresa com ampla experiência no setor de TI, comprometida em oferecer "
            "soluções que impulsionam o sucesso de nossos clientes.",
        ]
        for para in paragraphs:
            lbl = toga.Label(para, style=Pack(padding_bottom=5))
            self.content_box.add(lbl)

    def show_contact(self, widget):
        self.clear_content()
        paragraphs = [
            "Contato:",
            "Email: contato@empresaoutsourcing.com",
            "Telefone: (11) 1234-5678",
            "Endereço: Rua Exemplo, 123 - São Paulo, SP",
        ]
        for para in paragraphs:
            lbl = toga.Label(para, style=Pack(padding_bottom=5))
            self.content_box.add(lbl)


def main():
    return OutsourcingApp("Empresa Outsourcing TI", "org.exemplo.outsourcing")


if __name__ == "__main__":
    main().main_loop()
