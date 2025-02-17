from js import document, window, console


# Lista para manter vivos os proxies dos event listeners
event_proxies = []


def remove_loading_screen(event):
    loading = document.getElementById("loading-screen")
    if loading:
        loading.style.display = "none"


window.addEventListener("pyscript:ready", remove_loading_screen)

console.log("Olá, mundo!")


# # Função que será chamada quando o DOM estiver completamente carregado
# def on_dom_loaded(*args):
#     # Injetando estilos CSS dinamicamente
#     style = document.createElement("style")
#     style.innerHTML = """
#     body {
#         margin: 0;
#         font-family: Arial, sans-serif;
#         background-color: #f9f9f9;
#     }
#     header {
#         background-color: #007BFF;
#         color: #fff;
#         padding: 15px;
#         text-align: center;
#     }
#     nav {
#         background-color: #e0e0e0;
#         display: flex;
#         justify-content: center;
#         gap: 20px;
#         padding: 10px;
#     }
#     nav button {
#         background: none;
#         border: none;
#         font-size: 16px;
#         cursor: pointer;
#         padding: 8px 12px;
#         border-radius: 4px;
#     }
#     nav button:hover {
#         background-color: #ccc;
#     }
#     main {
#         padding: 20px;
#     }
#     """
#     document.head.appendChild(style)

#     # Cria um container para o site
#     container = document.createElement("div")

#     # Cria o cabeçalho com o nome da empresa
#     header = document.createElement("header")
#     h1 = document.createElement("h1")
#     h1.innerText = "Tech Outsource"
#     header.appendChild(h1)
#     container.appendChild(header)

#     # Cria a barra de navegação (menu)
#     nav = document.createElement("nav")
#     container.appendChild(nav)

#     # Cria a área principal de conteúdo
#     main_content = document.createElement("main")
#     container.appendChild(main_content)

#     # Adiciona o container ao body
#     document.body.appendChild(container)

#     # Função para atualizar o conteúdo principal
#     def update_content(content_html):
#         main_content.innerHTML = content_html

#     # Dicionário com as opções do menu e seus conteúdos
#     menu_options = {
#         "Início": (
#             "<h2>Bem-vindo à Tech Outsource</h2>"
#             "<p>Potencialize seu negócio com soluções inovadoras em outsourcing de TI.</p>"
#         ),
#         "Serviços": (
#             "<h2>Nossos Serviços</h2>"
#             "<ul>"
#             "<li>Suporte Técnico 24/7</li>"
#             "<li>Gestão de Infraestrutura</li>"
#             "<li>Consultoria em TI</li>"
#             "</ul>"
#         ),
#         "Contato": (
#             "<h2>Contato</h2>"
#             "<p>Envie um e-mail para <strong>contato@techoutsource.com.br</strong> ou ligue para (11) 1234-5678.</p>"
#         ),
#     }

#     # Cria os botões do menu dinamicamente
#     for option, content_html in menu_options.items():
#         btn = document.createElement("button")
#         btn.innerText = option

#         # Cria um proxy para a função de clique
#         def on_click(event, content=content_html):
#             update_content(content)

#         proxy = create_proxy(on_click)
#         event_proxies.append(proxy)  # Armazena o proxy para que ele não seja destruído
#         btn.addEventListener("click", proxy)

#         nav.appendChild(btn)

#     # Define o conteúdo inicial (Início)
#     update_content(menu_options["Início"])


# # Configura para que `on_dom_loaded` seja chamada quando o evento 'DOMContentLoaded' ocorrer
# window.addEventListener("DOMContentLoaded", on_dom_loaded)
