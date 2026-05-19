# AGENTS.md

Contexto para Codex e qualquer agente trabalhando no projeto `flet-gmftech`.

## Objetivo

`flet-gmftech` e o website institucional da GMF-tech. O produto deve continuar sendo um site/app web feito com Python, Flet e WebAssembly, com bundle estatico para publicacao em GitHub Pages.

Direcao do produto:

- Flet e a tecnologia principal do frontend e tambem a principal oferta comercial da GMF-tech.
- Python 3.13+ e a linguagem base.
- WebAssembly/Pyodide e o runtime do site no navegador.
- PyECharts e usado nos graficos, especialmente na pagina de cotacao.
- O site comunica desenvolvimento em Flet, Python, IA aplicada, automacao, dados, cloud, IoT e modernizacao.
- Nao migrar para React, Next, Vue, Astro ou templates JS. Melhorias visuais devem ser feitas em Flet.

## Identidade Atual

Marca: GMF-tech.

Contato principal:

- Gustavo M Freitas
- `gustavo@gmf-tech.com`
- `contato@gmf-tech.com`

Identidade visual atual:

- Visual inspirado em sites enterprise de tecnologia, com hero forte, secoes full-width, servicos por ciclo completo e foco em resultado.
- Referencia estrutural usada: BairesDev, sem copiar texto, marca ou layout literal.
- A marca da caravela deve aparecer via `assets/favicon.ico` e `assets/favicon.png`.
- Paleta em `theme.py`: azul profundo, verde oceano, teal, amarelo quente e coral.
- Evitar voltar ao visual antigo totalmente Material azul.

Copy e posicionamento atuais:

- Home: "Software, Flet e IA para acelerar sua operacao".
- Footer: "GMF-tech - Tecnologia para negócios".
- Serviços: Flet, Python, IA, automacao, dados, cloud, IoT, seguranca e modernizacao.
- Contato: diagnostico tecnico para Flet, IA e automacao.
- Portfolio: projetos com Flet, dados e automacao em producao.
- Cotacao: terminal tecnico para cambio e acoes usando PyECharts; no cambio, campo digitavel e padrao USD/BRL.

## Stack

Fonte principal de dependencias: `pyproject.toml`.

Versoes atuais:

- Python `>=3.13`.
- Flet `0.85.1`.
- Flet WebView `0.85.1`.
- HTTPX `0.28.1`.
- PyECharts `2.1.0`.
- `typing_extensions==4.15.0`.
- `flet-web==0.85.1` apenas para desenvolvimento/serve local, fora de `requirements.txt`.

Arquivos de dependencias:

- `requirements.txt`: seguro para Pyodide/WebAssembly. Nao incluir `flet-web`.
- `requirements-dev.txt`: inclui `-r requirements.txt` e `flet-web==0.85.1`.
- `pyproject.toml`: dependencias de runtime, extras `serve` e `test`, e configuracao do build Flet.

Observacao importante:

- O Flet 0.85.1 ainda pode gerar bundle com Pyodide antigo por padrao.
- O projeto usa patch pos-build para Pyodide `0.29.4`, que entrega Python 3.13 no navegador.
- O patch existe no `deploy-flet.sh` e tambem no `Dockerfile` via `ARG PYODIDE_VERSION=0.29.4`.
- Nao usar `--no-cdn` sem tambem atualizar a pasta local `pyodide/` gerada pelo Flet.

## Comandos

Executar comandos de app dentro de `flet-gmftech/`, salvo quando indicado.

Instalacao local:

```bash
python3 -m pip install -r requirements-dev.txt
```

Instalacao editavel com testes:

```bash
python3 -m pip install -e ".[test,serve]"
```

Rodar local:

```bash
python3 app.py
```

Testes:

```bash
python3 -m pytest
```

Build web:

```bash
flet build web --yes
```

Docker/Nginx, a partir da raiz do repositorio:

```bash
docker compose build
docker compose up -d
docker compose exec gmftech-web nginx -t
```

Validacao Playwright, a partir da raiz:

```bash
PLAYWRIGHT_BROWSER=chromium python3 flet-gmftech/tools/validate_frontend_playwright.py http://127.0.0.1:8080/
```

Nao executar `../deploy-flet.sh` sem pedido explicito do usuario.

## Deploy E Build

Fluxo esperado:

1. Alterar codigo em `flet-gmftech/`.
2. Rodar testes.
3. Gerar `flet-gmftech/build/web/` com `flet build web --yes`.
4. Testar o bundle via Docker/Nginx.
5. Validar com Playwright.
6. So publicar no GitHub Pages quando o usuario pedir.

Configuracao web atual em `pyproject.toml`:

- `base_url = "/"`.
- `renderer = "canvaskit"`.
- `route_url_strategy = "hash"`.
- modulo do app: `app`.

Arquivos de container:

- `Dockerfile`: serve `flet-gmftech/build/web/` com Nginx e troca `python.js` para Pyodide `0.29.4`.
- `docker/nginx.conf`: cache control conservador para HTML, Python worker, service worker e app.zip.
- `docker-compose.yml`: publica `gmftech-web` em `http://127.0.0.1:8080/`.
- `.dockerignore`: reduz contexto de build.

## Estrutura

Arquivos principais:

- `app.py`: entrada Flet, tema, AppBar, drawer mobile, footer, rotas e modal de diagnostico.
- `theme.py`: paleta, tema Flet, estilos de botao/texto/sombra e helpers responsivos.
- `utils/responsive.py`: breakpoints, escalas de fonte/espacamento e colunas responsivas.
- `utils/flet_runtime.py`: chamada segura para metodos da pagina em testes e runtime.
- `pages/home.py`: landing principal com hero, servicos e modelo de trabalho.
- `pages/services.py`: catalogo de servicos e stack principal.
- `pages/about.py`: posicionamento, valores e modo de trabalho.
- `pages/contact.py`: formulario de diagnostico, validacao local e SnackBar.
- `pages/portfolio.py`: projetos e provas de stack.
- `pages/coins.py`: terminal de mercado para cambio e acoes com PyECharts em `flet_webview.WebView`.
- `tools/validate_frontend_playwright.py`: smoke test real do bundle servido no navegador.
- `tests/`: testes unitarios de paginas, app, tema, responsividade e cotacao.

Arquivos legados:

- `old.py` e `new2.py` sao prototipos. Nao evoluir como produto principal.

Assets:

- `assets/favicon.ico`
- `assets/favicon.png`
- `assets/velejar_facil.png`
- `assets/chart-project.jpg`
- `assets/website-project.jpg`
- `assets/loading-animation.png`
- `assets/icons/loading-animation.png`

A pasta `images/` duplica imagens do portfolio. Para Flet web, preferir `assets/`.

## Rotas

Rotas registradas em `app.py`:

- `/`: Home.
- `/services`: Servicos e stack.
- `/about`: Sobre.
- `/contact`: Contato/diagnostico.
- `/coins`: Terminal de mercado para cambio e acoes.
- `/portfolio`: Portfolio.

Navegacao:

- Desktop usa AppBar com botoes.
- Mobile usa `NavigationDrawer`.
- O botao "Diagnostico" abre um modal simulado com Google, Apple e X.
- Na rota `/coins`, o CTA de diagnostico e ocultado para manter foco na demo.

## Servicos

Servicos atuais em `pages/services.py`:

- Levantamento de Requisitos.
- Arquitetura de Software.
- IoT com Arduino.
- Prototipagem Eletronica.
- Desenvolvimento Web.
- Desenvolvimento Mobile.
- Cloud Computing.
- Seguranca.
- Consultoria e Automacao com IA.

Stack principal exibida:

- Python.
- Flet.
- PostgreSQL.
- ScyllaDB.
- Redis.
- AWS.
- Azure DevOps.
- Apache ECharts.
- IA e LLMs.

Ao mudar copy, preservar esses servicos como base do que a GMF-tech presta e adicionar IA como camada nova de consultoria, automacao e melhoria operacional.

## Paginas

Home:

- Hero escuro com CTA para diagnostico, servicos e portfolio.
- Imagem `velejar_facil.png` como visual de produto.
- Cards de servico para levantamento de requisitos, arquitetura, IoT/prototipagem, web/mobile, cloud/seguranca e IA.
- Secao de modelo de trabalho em 3 passos.

Servicos:

- Header enterprise.
- Grade responsiva de 9 servicos com cards clicaveis.
- Ao clicar em um servico, o card mostra uma previa de stacks e o painel "Stacks para ..." exibe tecnologias e aplicacoes tipicas.
- Grade responsiva de 9 tecnologias.

Sobre:

- Hero com caravela/favicon.
- Blocos de valor: consultoria sem enrolacao, Flet como especialidade e IA para operacao real.
- Processo: Diagnostico, Prototipo, Producao.

Contato:

- Hero com prompts de projeto Flet, IA e automacao.
- Formulario valida nome, email e mensagem.
- `send_email()` ainda e simulado e apenas imprime dados.
- Nao apresentar envio real sem integrar backend/API.

Portfolio:

- Casos atuais: Velejar Facil, Monitoramento de Cotacoes e Website GMF-tech.
- Mostrar tecnologias por projeto.
- Usar imagens de `assets/`.

Cotacao:

- Usa AwesomeAPI para cambio e brapi para acoes; cambio aceita lista digitavel como `USD, EUR` ou pares como `USD/EUR`; quando a fonte de acoes falha, exibe serie demonstrativa deterministica.
- Em Pyodide usa `pyodide.http.pyfetch`.
- Em local/native usa `httpx.AsyncClient`.
- Cache global por 5 minutos.
- Grafico de preco e volume gerado com PyECharts e renderizado por `WebView` via data URL base64.
- Depende de internet e do CDN ECharts usado pelo PyECharts.

## Responsividade

Breakpoints em `utils/responsive.py`:

- Mobile: `<= 600px`.
- Tablet: `601px` a `900px`.
- Desktop: `> 900px`.

Escalas:

- Fonte: mobile `0.85`, tablet `0.95`, desktop `1.0`.
- Espacamento: mobile `0.75`, tablet `0.9`, desktop `1.0`.
- Grid padrao: mobile `1`, tablet `2`, desktop `3`.
- Padding de container: mobile `20`, tablet `30`, desktop `40`.

Ao alterar layout, conferir pelo menos:

- 400px.
- 768px.
- 1920px.

## Tema Visual

Paleta atual em `theme.py`:

- `primary`: `#071B2C`
- `secondary`: `#0E7C7B`
- `accent`: `#2DD4BF`
- `accent_alt`: `#F6C85F`
- `coral`: `#FF6B4A`
- `error`: `#D64545`
- `warning`: `#F6C85F`
- `success`: `#1A936F`
- `background`: `#F4F8FA`
- `surface`: `#FFFFFF`
- `surface_alt`: `#EAF3F5`
- `text_primary`: `#10212F`
- `text_secondary`: `#53656F`
- `muted`: `#D8E6EA`
- `dark_surface`: `#0B2536`

Estilo:

- Cards com raio de 8px.
- Botoes com raio de 6px.
- Secoes full-width, sem empilhar cards dentro de cards.
- Usar icones Flet/Lucide-equivalentes disponiveis em `ft.Icons`.
- Evitar texto explicando como usar o site dentro da interface.

## Testes

Configuracao:

- `pytest.ini` define `testpaths = tests`.
- Testes unitarios usam paginas Flet instanciadas com mocks de `ft.Page`.
- `tools/validate_frontend_playwright.py` faz smoke test real do frontend web servido.

Antes de finalizar mudanca relevante:

```bash
python3 -m compileall app.py pages theme.py utils tests
python3 -m pytest
```

Quando houver mudanca visual/build:

```bash
flet build web --yes
docker compose build
docker compose up -d
PLAYWRIGHT_BROWSER=chromium python3 flet-gmftech/tools/validate_frontend_playwright.py http://127.0.0.1:8080/
```

## Cuidados De Compatibilidade

- Flet 0.85 usa `ft.Border.all(...)`; nao usar `ft.border.all(...)` em codigo novo.
- `PopupMenuItem(text=...)` nao e aceito no Flet novo; usar `content=ft.Text(...)` quando precisar de menu.
- `page.width` pode ser `None` no inicio; usar fallback `page.width or 1024`.
- `flet-web` nao deve entrar em `requirements.txt`, pois pode puxar dependencias sem wheel pure Python no Pyodide.
- `typing_extensions` deve continuar explicito por causa do `flet_webview` no Pyodide.
- Build web gera `build/web/`, normalmente ignorado pelo git.
- Em GitHub Pages, manter `route_url_strategy = "hash"` para reduzir problemas de refresh/deep link.
- Paths de assets com `/arquivo.png` dependem do `base_url`; revisar se publicar em subpasta.

## Regras Para Novas Alteracoes

- Manter Flet como framework unico do frontend.
- Manter arquitetura em `pages/`, tema em `theme.py` e responsividade em `utils/responsive.py`.
- Usar PyECharts para graficos.
- Nao adicionar dependencias pesadas sem motivo claro.
- Nao reintroduzir specs antigas ou diretorios de outra ferramenta.
- Nao evoluir `old.py` e `new2.py`.
- Atualizar README, AGENTS e testes quando mudar stack, rotas, servicos, build ou comportamento de UI.
- Nao executar deploy sem pedido explicito.

## Definition Of Done

Para codigo:

- `python3 -m pytest` passa.
- Layout pensado para mobile, tablet e desktop.
- Copy publica reflete Flet, Python, IA e automacao.
- App segue Flet 0.85.1 sem APIs antigas quebradas.

Para frontend/build:

- `flet build web --yes` executa sem erro.
- Docker/Nginx serve o bundle.
- Playwright valida que a pagina carrega e nao fica branca.
- Assets principais aparecem no navegador.

Para deploy:

- Confirmar destino do GitHub Pages antes.
- Usar Pyodide `0.29.4`.
- Nao publicar automaticamente sem confirmacao do usuario.
