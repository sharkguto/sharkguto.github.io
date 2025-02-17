from js import document

# --- Injetando estilos CSS via Python ---
style = document.createElement("style")
style.innerHTML = """
body {
  background: #2e2e2e;
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.app-window {
  width: 800px;
  height: 600px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.5);
  display: flex;
  flex-direction: column;
  overflow: hidden;
}
.title-bar {
  background: #007BFF;
  color: #fff;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.title-bar .title {
  font-size: 18px;
  font-weight: bold;
}
.window-controls {
  display: flex;
  gap: 10px;
}
.window-controls span {
  display: inline-block;
  width: 20px;
  height: 20px;
  text-align: center;
  line-height: 20px;
  border-radius: 3px;
  background: rgba(255,255,255,0.3);
  cursor: pointer;
  user-select: none;
}
.menu-bar {
  background: #e0e0e0;
  padding: 8px;
  display: flex;
  gap: 15px;
  border-bottom: 1px solid #ccc;
}
.menu-bar button {
  background: none;
  border: none;
  font-size: 16px;
  cursor: pointer;
  padding: 5px 10px;
  border-radius: 4px;
  transition: background 0.3s;
}
.menu-bar button:hover {
  background: #ccc;
}
.content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
.content section {
  display: none;
}
.content section.active {
  display: block;
}
form label {
  display: block;
  margin-top: 10px;
  font-weight: bold;
}
form input,
form textarea {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
form button {
  margin-top: 15px;
  padding: 10px;
  background: #007BFF;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
}
#resultado {
  margin-top: 15px;
  font-weight: bold;
}
"""
document.head.appendChild(style)

# --- Criando a interface "desktop" via Python ---

# Cria o container principal da aplicação
app_window = document.createElement("div")
app_window.className = "app-window"

# Cria a barra de título
title_bar = document.createElement("div")
title_bar.className = "title-bar"
app_window.appendChild(title_bar)

title_text = document.createElement("div")
title_text.className = "title"
title_text.innerText = "Tech Outsource"
title_bar.appendChild(title_text)

# Cria os controles da janela
window_controls = document.createElement("div")
window_controls.className = "window-controls"
title_bar.appendChild(window_controls)

minimize_btn = document.createElement("span")
minimize_btn.innerText = "_"


def minimize_action(event):
    content.style.display = "none"


minimize_btn.addEventListener("click", minimize_action)
window_controls.appendChild(minimize_btn)

maximize_btn = document.createElement("span")
maximize_btn.innerText = "[]"


def maximize_action(event):
    content.style.display = "block"


maximize_btn.addEventListener("click", maximize_action)
window_controls.appendChild(maximize_btn)

close_btn = document.createElement("span")
close_btn.innerText = "X"


def close_action(event):
    app_window.style.display = "none"


close_btn.addEventListener("click", close_action)
window_controls.appendChild(close_btn)

# Cria a barra de menu
menu_bar = document.createElement("div")
menu_bar.className = "menu-bar"
app_window.appendChild(menu_bar)


def create_menu_button(text, section_id):
    btn = document.createElement("button")
    btn.innerText = text
    btn.addEventListener("click", lambda event: show_section(section_id))
    menu_bar.appendChild(btn)


create_menu_button("Início", "home")
create_menu_button("Serviços", "services")
create_menu_button("Contato", "contact")

# Cria a área de conteúdo
content = document.createElement("div")
content.className = "content"
app_window.appendChild(content)


# Função para alternar seções (simula "state" como no React)
def show_section(section_id):
    sections = content.querySelectorAll("section")
    for section in sections:
        if section.id == section_id:
            section.classList.add("active")
        else:
            section.classList.remove("active")


# Seção: Início
home_section = document.createElement("section")
home_section.id = "home"
home_section.className = "active"  # exibe inicialmente
h2_home = document.createElement("h2")
h2_home.innerText = "Bem-vindo à Tech Outsource"
home_section.appendChild(h2_home)
p_home = document.createElement("p")
p_home.innerText = "Transforme sua TI com nossa expertise. Oferecemos soluções completas de outsourcing para potencializar o seu negócio."
home_section.appendChild(p_home)
content.appendChild(home_section)

# Seção: Serviços
services_section = document.createElement("section")
services_section.id = "services"
h2_services = document.createElement("h2")
h2_services.innerText = "Nossos Serviços"
services_section.appendChild(h2_services)
ul_services = document.createElement("ul")
for service in [
    "Suporte Técnico 24/7",
    "Gestão de Infraestrutura",
    "Consultoria em TI",
]:
    li = document.createElement("li")
    li.innerText = service
    ul_services.appendChild(li)
services_section.appendChild(ul_services)
content.appendChild(services_section)

# Seção: Contato (com formulário)
contact_section = document.createElement("section")
contact_section.id = "contact"
h2_contact = document.createElement("h2")
h2_contact.innerText = "Entre em Contato"
contact_section.appendChild(h2_contact)

form = document.createElement("form")
form.id = "contact-form"

# Campo: Nome
label_nome = document.createElement("label")
label_nome.innerText = "Nome:"
form.appendChild(label_nome)
input_nome = document.createElement("input")
input_nome.id = "nome"
input_nome.placeholder = "Seu nome"
form.appendChild(input_nome)

# Campo: Email
label_email = document.createElement("label")
label_email.innerText = "Email:"
form.appendChild(label_email)
input_email = document.createElement("input")
input_email.id = "email"
input_email.type = "email"
input_email.placeholder = "Seu email"
form.appendChild(input_email)

# Campo: Mensagem
label_mensagem = document.createElement("label")
label_mensagem.innerText = "Mensagem:"
form.appendChild(label_mensagem)
textarea_mensagem = document.createElement("textarea")
textarea_mensagem.id = "mensagem"
textarea_mensagem.placeholder = "Sua mensagem"
form.appendChild(textarea_mensagem)

# Botão de envio
submit_btn = document.createElement("button")
submit_btn.type = "button"
submit_btn.innerText = "Enviar"


def enviar_formulario(event):
    nome = input_nome.value
    email = input_email.value
    mensagem = textarea_mensagem.value
    resultado = document.getElementById("resultado")
    if not nome or not email or not mensagem:
        resultado.innerHTML = (
            "<p style='color: red;'>Por favor, preencha todos os campos.</p>"
        )
    else:
        resultado.innerHTML = f"<p style='color: green;'>Obrigado, {nome}! Em breve entraremos em contato.</p>"
    # Limpa os campos
    input_nome.value = ""
    input_email.value = ""
    textarea_mensagem.value = ""


submit_btn.addEventListener("click", enviar_formulario)
form.appendChild(submit_btn)
contact_section.appendChild(form)

# Div para resultado do formulário
resultado_div = document.createElement("div")
resultado_div.id = "resultado"
contact_section.appendChild(resultado_div)
content.appendChild(contact_section)

# Adiciona toda a aplicação à página
document.body.appendChild(app_window)
