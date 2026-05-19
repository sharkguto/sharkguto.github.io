# GMF-tech

Website institucional da GMF-tech feito em Python com Flet, WebAssembly/Pyodide e build estatico para GitHub Pages.

O site posiciona a GMF-tech como especialista em Flet, Python, IA aplicada, automacao, dados, cloud e sistemas internos prontos para producao.

## Stack

- Python `>=3.13`
- Flet `0.85.1`
- Flet WebView `0.85.1`
- HTTPX `0.28.1`
- PyECharts `2.1.0`
- `typing_extensions==4.15.0`
- Pyodide `0.29.4` no bundle final via patch pos-build

`flet-web==0.85.1` fica apenas em `requirements-dev.txt`/extra `serve`, porque nao deve entrar no runtime Pyodide do GitHub Pages.

## Conteudo Do Site

- Home com hero enterprise, CTAs e servicos principais.
- Servicos com cards clicaveis para mostrar stacks relacionadas a levantamento de requisitos, arquitetura, IoT/Arduino, prototipagem, web, mobile, cloud, seguranca e IA.
- Sobre com posicionamento da GMF-tech e identidade da caravela.
- Contato com formulario de diagnostico tecnico.
- Portfolio com projetos e tecnologias.
- Terminal de mercado para cambio e acoes, com campo digitavel no cambio, dois graficos padrao (USD/BRL e EUR/BRL) e PyECharts de preco/volume renderizado em `flet_webview.WebView`.

## Desenvolvimento

```bash
python3 -m pip install -r requirements-dev.txt
python3 app.py
```

## Testes

```bash
python3 -m compileall app.py pages theme.py utils tests
python3 -m pytest
```

## Build Web

```bash
flet build web --yes
```

O bundle e gerado em `build/web/`.

Configuracao web em `pyproject.toml`:

- `base_url = "/"`
- `renderer = "canvaskit"`
- `route_url_strategy = "hash"`

## Docker/Nginx

Para testar o build estatico sem executar deploy:

```bash
cd ..
docker compose build
docker compose up -d
```

O site fica em:

```text
http://127.0.0.1:8080/
```

Validacao com Playwright:

```bash
PLAYWRIGHT_BROWSER=chromium python3 flet-gmftech/tools/validate_frontend_playwright.py http://127.0.0.1:8080/
```

O `Dockerfile` serve `flet-gmftech/build/web/` com Nginx e atualiza `python.js` para carregar Pyodide `0.29.4`.

## Deploy

O script `../deploy-flet.sh` existe para publicar no GitHub Pages, mas deve ser executado somente quando o deploy for solicitado explicitamente.

Antes de publicar, valide:

- testes unitarios;
- `flet build web --yes`;
- Docker/Nginx local;
- Playwright;
- assets principais carregando no navegador.

## Estrutura

```text
flet-gmftech/
├── app.py
├── theme.py
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
├── pages/
│   ├── home.py
│   ├── services.py
│   ├── about.py
│   ├── contact.py
│   ├── portfolio.py
│   └── coins.py
├── utils/
│   ├── flet_runtime.py
│   └── responsive.py
├── assets/
│   ├── favicon.ico
│   ├── favicon.png
│   ├── velejar_facil.png
│   ├── chart-project.jpg
│   └── website-project.jpg
├── tools/
│   └── validate_frontend_playwright.py
└── tests/
```

## Tema

Paleta atual em `theme.py`:

- `primary`: `#071B2C`
- `secondary`: `#0E7C7B`
- `accent`: `#2DD4BF`
- `accent_alt`: `#F6C85F`
- `coral`: `#FF6B4A`
- `background`: `#F4F8FA`
- `surface`: `#FFFFFF`
- `surface_alt`: `#EAF3F5`
- `dark_surface`: `#0B2536`

## Observacoes

- A pagina de mercado depende da AwesomeAPI, da brapi para acoes e de CDN do ECharts.
- `send_email()` em `pages/contact.py` ainda e simulado.
- `old.py` e `new2.py` sao prototipos legados.
- O projeto deve continuar usando Flet como stack de frontend.
