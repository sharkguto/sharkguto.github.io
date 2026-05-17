# GMF-tech - Landing Page

Landing page institucional da GMF-tech desenvolvida em Python com Flet, oferecendo uma experiência moderna e responsiva para apresentar os serviços de outsourcing em TI da empresa.

## 🚀 Sobre o Projeto

Este projeto é uma aplicação web multiplataforma construída com Flet (framework Python para criar aplicações web, desktop e mobile). A landing page apresenta os serviços, tecnologias, portfólio e informações de contato da GMF-tech, além de funcionalidades interativas como cotação de moedas em tempo real.

## ✨ Funcionalidades

- **Página Inicial**: Apresentação da empresa com navegação rápida
- **Serviços**: Catálogo completo de serviços oferecidos (desenvolvimento web/mobile, IoT, cloud, etc.)
- **Tecnologias**: Stack tecnológico utilizado (Python, Flet, PostgreSQL, ScyllaDB, Redis, AWS, etc.)
- **Sobre**: História, missão e valores da empresa
- **Contato**: Formulário de contato com validação
- **Cotação USD/BRL**: Gráfico PyECharts com dados dos últimos 15 dias
- **Portfólio**: Showcase de projetos realizados com imagens e descrições detalhadas
- **Design Responsivo**: Interface adaptável para desktop, tablet e mobile
- **Sistema de Login**: Modal de autenticação (Google, Apple, X)
- **Tema Customizado**: Paleta de cores moderna e consistente

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**: Linguagem principal
- **Flet 0.85.1**: Framework para aplicações multiplataforma
- **Flet Web 0.85.1**: Runtime web usado pelo Flet 0.85
- **Flet WebView 0.85.1**: Renderização do gráfico PyECharts no app web
- **PyECharts 2.1.0**: Biblioteca de visualização de dados usada na cotação
- **HTTPX 0.28.1**: Cliente HTTP assíncrono
- **typing_extensions 4.15.0**: Dependência explícita para compatibilidade do WebView no Pyodide

## 📋 Pré-requisitos

- Python 3.13 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd gmf_tech
```

2. Instale as dependências:
```bash
pip install -r requirements-dev.txt
```

Ou usando o pyproject.toml:
```bash
pip install -e ".[serve]"
```

## 🚀 Como Executar

### Modo Desenvolvimento

Execute a aplicação localmente:
```bash
python app.py
```

A aplicação será aberta automaticamente no navegador padrão.

### Build para Produção (Web)

Para gerar os arquivos estáticos para deploy:
```bash
flet build web --yes
```

Os arquivos compilados estarão disponíveis na pasta `build/web/`.

### Build para Desktop

Para criar executável desktop:
```bash
flet build windows  # Para Windows
flet build macos    # Para macOS
flet build linux    # Para Linux
```

## 📁 Estrutura do Projeto

```
gmf_tech/
├── app.py                 # Arquivo principal da aplicação
├── theme.py              # Configurações de tema e estilos
├── requirements.txt      # Dependências do projeto
├── pyproject.toml       # Configurações do projeto e build
├── pytest.ini           # Configuração do pytest
├── .coveragerc          # Configuração de cobertura de testes
├── pages/               # Módulos das páginas
│   ├── __init__.py
│   ├── home.py         # Página inicial
│   ├── services.py     # Página de serviços
│   ├── about.py        # Página sobre
│   ├── contact.py      # Página de contato
│   ├── coins.py        # Página de cotação
│   └── portfolio.py    # Página de portfólio
├── utils/              # Utilitários
│   ├── __init__.py
│   └── responsive.py   # Sistema de responsividade
├── tests/              # Testes unitários
│   ├── __init__.py
│   ├── conftest.py     # Fixtures compartilhadas
│   ├── test_app.py     # Testes do app principal
│   ├── test_theme.py   # Testes do módulo de tema
│   ├── test_responsive.py  # Testes do sistema responsivo
│   └── pages/          # Testes das páginas
│       ├── test_home.py
│       ├── test_services.py
│       ├── test_about.py
│       ├── test_contact.py
│       ├── test_coins.py
│       └── test_portfolio.py
├── assets/             # Recursos estáticos
│   ├── favicon.ico
│   ├── favicon.png
│   └── icons/
└── images/             # Imagens do portfólio
    ├── chart-project.jpg
    ├── velejar_facil.png
    └── website-project.jpg
```

## 🎨 Paleta de Cores

O projeto utiliza uma paleta de cores moderna e profissional:

- **Primary**: #1a237e (Azul escuro)
- **Secondary**: #0d47a1 (Azul médio)
- **Accent**: #1e88e5 (Azul claro)
- **Error**: #d32f2f (Vermelho)
- **Warning**: #ffa000 (Laranja)
- **Success**: #388e3c (Verde)
- **Background**: #f5f5f5 (Cinza claro)
- **Surface**: #ffffff (Branco)

## 🌐 API Utilizada

A página de cotação consome dados da API pública:
- **AwesomeAPI**: https://economia.awesomeapi.com.br/json/daily/USD-BRL/15

## 📱 Responsividade

A aplicação é totalmente responsiva e se adapta a diferentes tamanhos de tela usando um sistema de breakpoints centralizado.

### Breakpoints

O sistema de responsividade utiliza três breakpoints principais:

| Breakpoint | Largura | Descrição |
|------------|---------|-----------|
| **Mobile** | ≤ 600px | Layout vertical, menu hambúrguer, 1 coluna |
| **Tablet** | 601-900px | Layout adaptado, 2 colunas, elementos redimensionados |
| **Desktop** | > 900px | Layout completo, navegação horizontal, 3 colunas |

### Características por Breakpoint

**Mobile (≤ 600px)**:
- Menu hambúrguer (PopupMenuButton)
- Grid de serviços: 1 coluna
- Grid de portfólio: 1 coluna
- Imagens: largura máxima (viewport - 80px)
- Gráfico de cotações: altura 300px
- Campos de formulário: largura 100%
- Font scale: 0.85x

**Tablet (601-900px)**:
- Navegação horizontal compacta
- Grid de serviços: 2 colunas
- Grid de portfólio: 2 colunas
- Imagens: largura proporcional
- Gráfico de cotações: altura 350px
- Campos de formulário: largura 100%
- Font scale: 0.95x

**Desktop (> 900px)**:
- Navegação horizontal completa
- Grid de serviços: 3 colunas
- Grid de portfólio: 2 colunas (imagens 400px)
- Imagens: tamanho otimizado
- Gráfico de cotações: altura 400px
- Campos de formulário: largura 400px
- Font scale: 1.0x

### Usando o Sistema Responsivo

O módulo `utils/responsive.py` fornece utilitários para trabalhar com responsividade:

```python
from utils.responsive import ResponsiveConfig, Breakpoint

# Detectar breakpoint atual
breakpoint = ResponsiveConfig.get_breakpoint(page.width)

# Obter tamanho de fonte responsivo
font_size = ResponsiveConfig.get_font_size(base_size=16, breakpoint=breakpoint)

# Obter espaçamento responsivo
spacing = ResponsiveConfig.get_spacing(base_spacing=20, breakpoint=breakpoint)

# Obter número de colunas para grid
columns = ResponsiveConfig.get_grid_columns(breakpoint)

# Obter padding do container
padding = ResponsiveConfig.get_container_padding(breakpoint)
```

O módulo `theme.py` também oferece funções responsivas convenientes:

```python
from theme import get_responsive_font_size, get_responsive_padding, get_responsive_spacing

# Calcular valores responsivos baseado na largura da página
font_size = get_responsive_font_size(base_size=16, width=page.width)
padding = get_responsive_padding(base_padding=20, width=page.width)
spacing = get_responsive_spacing(base_spacing=10, width=page.width)
```

## 🧪 Testes

O projeto possui uma suite completa de testes unitários para garantir a qualidade e confiabilidade do código.

### Executando os Testes

Para executar todos os testes:
```bash
pytest
```

Para executar com saída detalhada:
```bash
pytest -v
```

Para executar testes específicos:
```bash
# Testar apenas o módulo de tema
pytest tests/test_theme.py

# Testar apenas a página home
pytest tests/pages/test_home.py

# Testar apenas o sistema responsivo
pytest tests/test_responsive.py
```

### Cobertura de Testes

Para gerar relatório de cobertura:
```bash
pytest --cov=. --cov-report=html --cov-report=term
```

Isso irá:
- Exibir um resumo de cobertura no terminal
- Gerar um relatório HTML detalhado em `htmlcov/index.html`

Para visualizar o relatório HTML:
```bash
# Linux/Mac
open htmlcov/index.html

# Windows
start htmlcov/index.html
```

### Estrutura dos Testes

Os testes estão organizados espelhando a estrutura do código fonte:

- **tests/test_app.py**: Testes do aplicativo principal (header, footer, navegação, login)
- **tests/test_theme.py**: Testes das funções de tema e estilos
- **tests/test_responsive.py**: Testes do sistema de responsividade
- **tests/pages/**: Testes de cada página individual
- **tests/conftest.py**: Fixtures compartilhadas (mocks de Page, breakpoints, etc.)

### Fixtures Disponíveis

O arquivo `conftest.py` fornece fixtures reutilizáveis:

```python
# Mock de página genérica
def test_something(mock_page):
    content = home_content(mock_page)
    assert content is not None

# Mock de página mobile (400px)
def test_mobile_layout(mobile_page):
    content = services_content(mobile_page)
    # Verificar layout mobile

# Mock de página tablet (768px)
def test_tablet_layout(tablet_page):
    content = services_content(tablet_page)
    # Verificar layout tablet

# Mock de página desktop (1920px)
def test_desktop_layout(desktop_page):
    content = services_content(desktop_page)
    # Verificar layout desktop

# Cores do tema
def test_colors(theme_colors):
    assert theme_colors["primary"] == "#1a237e"
```

### Métricas de Qualidade

O projeto mantém os seguintes padrões de qualidade:

- ✅ Cobertura de código: ≥ 80%
- ✅ Todos os testes passando: 0 falhas
- ✅ Tempo de execução: < 30 segundos
- ✅ Testes para todas as páginas e componentes principais

### Executando Testes em CI/CD

Para integração contínua, use:
```bash
pytest --cov=. --cov-report=xml --cov-report=term
```

Isso gera um relatório XML compatível com ferramentas de CI/CD como GitHub Actions, GitLab CI, Jenkins, etc.

## 🔒 Segurança

- Validação de formulários no lado do cliente
- Tratamento de erros em requisições HTTP
- Cache inteligente para otimização de performance

## 🚀 Deploy

### Opções de Deploy

1. **Hospedagem Estática** (após build web):
   - GitHub Pages
   - Netlify
   - Vercel
   - AWS S3 + CloudFront

2. **Servidor Python**:
   - Deploy direto em servidor com Python
   - Docker container
   - Plataformas como Heroku, Railway, Render

### Exemplo de Deploy com Docker

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## 👨‍💻 Autor

**Gustavo M Freitas**
- Email: gustavo@gmf-tech.com
- Empresa: GMF-tech

## 📄 Licença

Copyright (C) 2026 by sharkguto


## 📞 Suporte

Para suporte, entre em contato através do email: contato@gmf-tech.com ou telefone: (11) 9999-9999

---

Desenvolvido com ❤️ usando Flet
