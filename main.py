from pyscript import window


# Função que será chamada quando o DOM estiver completamente carregado
def on_dom_loaded(*args):
    from pyscript import document

    # Função para adicionar elementos ao DOM
    def adiciona_elemento(tag, text, **kwargs):
        el = document.createElement(tag)
        el.textContent = text
        for key, value in kwargs.items():
            el.setAttribute(key, value)
        document.body.appendChild(el)
        return el

    # Adiciona o cabeçalho
    adiciona_elemento(
        "header",
        "",
        class_="header",
        style="background-color: #4CAF50; color: white; padding: 20px 0; text-align: center;",
    )
    adiciona_elemento("h1", "NuvemPython", parent=document.querySelector("header"))
    adiciona_elemento(
        "p",
        "Soluções em Nuvem e Desenvolvimento Backend com Python",
        parent=document.querySelector("header"),
    )

    # ... (continuar adicionando o restante dos elementos)

    # Adiciona botão de contato
    button = adiciona_elemento(
        "button",
        "Contate-nos",
        id="contactBtn",
        style="background-color: #4CAF50; border: none; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer;",
    )

    # Função para o botão de contato
    def show_message(*args):
        window.alert("Obrigado pelo interesse! Entraremos em contato em breve.")

    # Adiciona evento ao botão
    button.addEventListener("click", show_message)

    # Remove a tela de carregamento
    document.getElementById("loading-screen").style.display = "none"


# Configura para que `on_dom_loaded` seja chamada quando o evento 'DOMContentLoaded' ocorrer
window.addEventListener("DOMContentLoaded", on_dom_loaded)
