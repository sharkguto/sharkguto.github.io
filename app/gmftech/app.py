import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class OutsourcingApp(toga.App):
    def startup(self):
        # Container principal
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, flex=1))

        # Cabeçalho
        header = toga.Label("Empresa de Outsourcing de TI", style=Pack(padding=5))
        main_box.add(header)

        # Barra de navegação (Home, Serviços, Sobre, Contato)
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

        # WebView para exibir o conteúdo em HTML
        self.webview = toga.WebView(style=Pack(flex=1, padding=5))
        main_box.add(self.webview)

        # Janela principal
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        # Exibe o conteúdo inicial (Home)
        self.show_home(None)

    def show_home(self, widget):
        html_content = """
        <h2>Bem-vindo à nossa empresa de Outsourcing de TI!</h2>
        <p>
          Oferecemos soluções inovadoras e personalizadas para atender às necessidades
          tecnológicas de sua empresa, com foco em qualidade e eficiência.
        </p>
        """
        self.webview.set_content("home", html_content)

    def show_services(self, widget):
        html_content = """
        <h3>Serviços</h3>
        <ul>
          <li>Desenvolvimento de Software</li>
          <li>Gestão de Infraestrutura</li>
          <li>Consultoria em TI</li>
          <li>Suporte Técnico</li>
        </ul>
        """
        self.webview.set_content("services", html_content)

    def show_about(self, widget):
        html_content = """
        <h3>Sobre Nós</h3>
        <p>
          Somos uma empresa com ampla experiência no setor de TI, comprometida em oferecer
          soluções que impulsionam o sucesso de nossos clientes.
        </p>
        """
        self.webview.set_content("about", html_content)

    def show_contact(self, widget):
        html_content = """
        <h3>Contato</h3>
        <p>
          Email: contato@empresaoutsourcing.com<br/>
          Telefone: (11) 1234-5678<br/>
          Endereço: Rua Exemplo, 123 - São Paulo, SP
        </p>
        """
        self.webview.set_content("contact", html_content)


def main():
    return OutsourcingApp("Empresa Outsourcing TI", "org.exemplo.outsourcing")


if __name__ == "__main__":
    main().main_loop()
