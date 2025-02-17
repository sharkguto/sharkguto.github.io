import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class ResponsiveApp(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1))

        header = toga.Label("Empresa de Outsourcing de TI", style=Pack(padding=5))
        main_box.add(header)

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

        nav_box.add(btn_home)
        nav_box.add(btn_services)
        nav_box.add(btn_about)
        nav_box.add(btn_contact)
        main_box.add(nav_box)

        # MultilineTextInput pode ser usado para exibir texto com quebra de linha,
        # desde que o backend Web ofereça suporte. Deixe-o como somente leitura.
        self.content = toga.MultilineTextInput(
            readonly=True, style=Pack(flex=1, padding=5)
        )
        main_box.add(self.content)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        self.show_home(None)

    def show_home(self, widget):
        self.content.value = (
            "Bem-vindo à nossa empresa de Outsourcing de TI!\n\n"
            "Oferecemos soluções inovadoras e personalizadas para atender às necessidades "
            "tecnológicas de sua empresa, com foco em qualidade e eficiência."
        )

    def show_services(self, widget):
        self.content.value = (
            "Serviços:\n"
            "- Desenvolvimento de Software\n"
            "- Gestão de Infraestrutura\n"
            "- Consultoria em TI\n"
            "- Suporte Técnico"
        )

    def show_about(self, widget):
        self.content.value = (
            "Sobre nós:\n"
            "Somos uma empresa com ampla experiência no setor de TI, comprometida em oferecer "
            "soluções que impulsionam o sucesso de nossos clientes."
        )

    def show_contact(self, widget):
        self.content.value = (
            "Contato:\n"
            "Email: contato@empresaoutsourcing.com\n"
            "Telefone: (11) 1234-5678\n"
            "Endereço: Rua Exemplo, 123 - São Paulo, SP"
        )


def main():
    return ResponsiveApp("Empresa Outsourcing TI", "org.exemplo.outsourcing")


if __name__ == "__main__":
    main().main_loop()
