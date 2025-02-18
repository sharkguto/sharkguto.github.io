import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class OutsourcingApp(toga.App):
    def startup(self):
        # Cria um contêiner principal
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20))

        # Cria rótulos para as seções da aplicação
        home_label = toga.Label(
            "Bem-vindo!\nDescubra como nossa expertise em TI pode ajudar seu negócio a crescer.",
            style=Pack(padding=10),
        )
        services_label = toga.Label(
            "Serviços:\nConsultoria, desenvolvimento e suporte técnico.",
            style=Pack(padding=10),
        )
        about_label = toga.Label(
            "Sobre Nós:\nEquipe dedicada a entregar soluções inovadoras.",
            style=Pack(padding=10),
        )
        contact_label = toga.Label(
            "Contato:\nEntre em contato conosco!", style=Pack(padding=10)
        )

        # Aqui você pode implementar uma navegação entre as seções.
        # Para este exemplo, apenas adicionaremos a seção inicial.
        main_box.add(home_label)

        # Cria e mostra a janela principal
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return OutsourcingApp("Outsourcing de TI", "org.exemplo.outsourcing")


if __name__ == "__main__":
    main().main_loop()
