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
- **Cotação USD/BRL**: Gráfico interativo com dados dos últimos 15 dias usando Apache ECharts
- **Portfólio**: Showcase de projetos realizados com imagens e descrições detalhadas
- **Design Responsivo**: Interface adaptável para desktop, tablet e mobile
- **Sistema de Login**: Modal de autenticação (Google, Apple, X)
- **Tema Customizado**: Paleta de cores moderna e consistente

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal
- **Flet 0.27.6**: Framework para aplicações multiplataforma
- **PyECharts 2.0.8**: Biblioteca de visualização de dados
- **HTTPX 0.28.1**: Cliente HTTP assíncrono
- **Flet WebView 0.1.0**: Componente para renderização de conteúdo web

## 📋 Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd gmf_tech
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

Ou usando o pyproject.toml:
```bash
pip install -e .
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
flet build web
```

Os arquivos compilados estarão disponíveis na pasta `dist/`.

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
├── pages/               # Módulos das páginas
│   ├── __init__.py
│   ├── home.py         # Página inicial
│   ├── services.py     # Página de serviços
│   ├── about.py        # Página sobre
│   ├── contact.py      # Página de contato
│   ├── coins.py        # Página de cotação
│   └── portfolio.py    # Página de portfólio
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

A aplicação é totalmente responsiva e se adapta a diferentes tamanhos de tela:
- **Desktop**: Layout completo com navegação horizontal
- **Tablet**: Layout adaptado com ajustes de espaçamento
- **Mobile**: Menu hambúrguer e layout vertical otimizado

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
FROM python:3.11-slim
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

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📞 Suporte

Para suporte, entre em contato através do email: contato@gmf-tech.com ou telefone: (11) 9999-9999

---

Desenvolvido com ❤️ usando Flet
