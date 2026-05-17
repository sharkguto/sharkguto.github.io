# AGENTS.md

Orientacoes para qualquer agente trabalhando no projeto `flet-gmftech`.

## Objetivo Do Projeto

Este projeto deve ser o website institucional da GMF-tech, feito com Python 3 e Flet, com foco em web via WebAssembly/Pyodide e build estatico para deploy no GitHub Pages.

Direcao do usuario:

- Foco exclusivo em Flet como tecnologia principal e como oferta comercial da GMF-tech.
- Usar Python 3, Flet e WebAssembly para entregar o site.
- Gerar bundle web estatico para publicar no GitHub Pages.
- Todos os servicos ja listados no projeto sao servicos prestados pela GMF-tech, mas a comunicacao deve puxar claramente para especialidade em Flet.
- Nao migrar para React, Next, Vue, Astro, templates JS ou outro stack de frontend. Se precisar de interatividade visual, implementar com controles Flet ou integracao pontual dentro do padrao atual.

## Produto E Posicionamento

Marca: GMF-tech.

Autor/contato atual no projeto:

- Gustavo M Freitas
- `gustavo@gmf-tech.com`
- README tambem cita `contato@gmf-tech.com` e telefone `(11) 9999-9999`.

Mensagem atual do site:

- Home: "Bem-vindo a GMF-tech" e "Sua parceira em solucoes de TI".
- Footer: "GMF-tech - Outsourcing em TI".
- Sobre: historia, missao e valores da empresa.
- Servicos: catalogo de servicos e tecnologias.
- Portfolio: projetos realizados.
- Cotacao: demonstracao tecnica com grafico USD/BRL.

Ao evoluir o conteudo, tratar a GMF-tech como especialista em:

- Aplicacoes web com Flet.
- Aplicacoes Python multiplataforma.
- WebAssembly/Pyodide para apps Python rodando no navegador.
- Prototipos, MVPs e sistemas internos em Flet.
- Dashboards, formularios, portais, sites institucionais e apps responsivos feitos em Flet.
- Deploy estatico do bundle web em GitHub Pages.

Os servicos atuais continuam validos, mas devem ser apresentados como capacidades da GMF-tech com Flet no centro.

## Stack Atual

Fonte mais autoritativa de dependencias: `pyproject.toml`.

- Python 3.13 ou superior.
- Runtime web desejado: Pyodide `0.29.4`, para CPython 3.13 no navegador.
- `flet==0.85.1`.
- `flet-web==0.85.1`.
- `flet-webview==0.85.1`.
- `pyecharts==2.1.0`.
- `httpx==0.28.1`.
- `typing_extensions==4.15.0`.
- Testes opcionais: `pytest`, `pytest-cov`, `pytest-asyncio`.

`requirements.txt` deve ficar seguro para WebAssembly/Pyodide. Nao incluir dependencias de servidor local nele:

- `flet==0.85.1`
- `flet-webview==0.85.1`
- `httpx==0.28.1`
- `pyecharts==2.1.0`
- `typing_extensions==4.15.0`

Para desenvolvimento local com browser, usar `requirements-dev.txt` ou `.[serve]`, pois `flet-web` puxa dependencias de servidor que nao rodam no Pyodide.

O Flet `0.85.1` ainda aponta o web runtime padrao para Pyodide `0.27.7`. O script `../deploy-flet.sh` aplica um patch pos-build em `python.js` para trocar o CDN para `https://cdn.jsdelivr.net/pyodide/v0.29.4/full/pyodide.js`. Nao usar `--no-cdn` sem tambem atualizar a pasta local `pyodide/`, pois ela e gerada pelo Flet.

Prefira manter `pyproject.toml` como fonte principal quando precisar de reproducibilidade.

## Comandos Comuns

Sempre executar a partir de `flet-gmftech/`.

Instalacao para desenvolvimento:

```bash
python -m pip install -e ".[test]"
```

Alternativa simples para desenvolvimento local:

```bash
python -m pip install -r requirements-dev.txt
```

Rodar localmente:

```bash
python app.py
```

Testes:

```bash
python -m pytest
```

Cobertura:

```bash
python -m pytest --cov=. --cov-report=term --cov-report=html
```

Build web:

```bash
flet build web --yes
```

Antes de publicar no GitHub Pages, verificar o destino real:

- Para site de usuario/organizacao no dominio raiz, `base_url = "/"` pode ser adequado.
- Para deploy em subpasta, ajustar `base_url` para `/<repo-ou-subpasta>/` ou passar flag equivalente no build.
- O projeto usa `route_url_strategy = "hash"` para funcionar bem em hospedagem estatica do GitHub Pages.
- O build web do Flet 0.85 gera saida em `build/web/`.

## Estrutura Do Projeto

Arquivos principais:

- `app.py`: entrada principal do app Flet, configuracao da pagina, AppBar, drawer mobile, footer, roteamento e modal de login.
- `theme.py`: paleta de cores, tema Flet, estilos de botao/texto/sombra e helpers responsivos.
- `utils/responsive.py`: breakpoints e regras centralizadas de responsividade.
- `pages/home.py`: home com titulo, subtitulo e botoes para portfolio, servicos e contato.
- `pages/services.py`: cards de servicos e tecnologias.
- `pages/about.py`: historia, missao e valores.
- `pages/contact.py`: formulario de contato com validacao local e SnackBar.
- `pages/coins.py`: grafico USD/BRL com PyECharts renderizado em WebView, cache e fetch async.
- `pages/portfolio.py`: cards de projetos com imagens e tecnologias.
- `tests/`: suite de testes unitarios por modulo e pagina.
- `old.py` e `new2.py`: prototipos antigos. Nao usar como base principal para novas features.

Assets:

- `assets/favicon.ico`
- `assets/favicon.png`
- `assets/loading-animation.png`
- `assets/icons/loading-animation.png`
- `assets/velejar_facil.png`
- `assets/chart-project.jpg`
- `assets/website-project.jpg`

A pasta `images/` duplica imagens do portfolio. Para Flet web, prefira `assets/` como fonte principal.

Artefatos e ignores:

- `.gitignore` ignora `dist`, `build` e `*.pyc`.
- `.coverage` existe como artefato local de cobertura.
- Se o bundle gerado precisar ser versionado para GitHub Pages, confirmar antes o fluxo desejado, porque os diretorios comuns de build estao ignorados.

## Rotas

Rotas registradas em `app.py`:

- `/`: `home_content(page)`.
- `/services`: `services_content(page)`.
- `/about`: `about_content(page)`.
- `/contact`: `contact_content(page)`.
- `/coins`: `currency_chart_content(page)`.
- `/portfolio`: `portfolio_content(page)`.

A AppBar desktop mostra: Inicio, Servicos, Sobre, Contato, Cotacao e Login. Em mobile, usa `NavigationDrawer` com Inicio, Servicos, Sobre, Contato, Cotacao, Portfolio e Login quando aplicavel.

## Servicos E Tecnologias Listados Hoje

Servicos atuais em `pages/services.py`:

- Levantamento de Requisitos.
- Arquitetura de Software.
- IoT com Arduino.
- Prototipagem Eletronica.
- Desenvolvimento Web.
- Desenvolvimento Mobile.
- Cloud Computing.
- Seguranca.

Tecnologias atuais:

- Python.
- Flet.
- PostgreSQL.
- ScyllaDB.
- Redis.
- AWS.
- Azure DevOps.
- Apache ECharts.

Ao reescrever marketing/copy, nao remover automaticamente essas capacidades; reposiciona-las como servicos prestados pela GMF-tech, com Flet como eixo da oferta.

## Portfolio Atual

Projetos em `pages/portfolio.py`:

- Velejar Facil: plataforma para controle de embarcacoes, marinas, reservas, pagamentos, avaliacoes e interface web/mobile.
- Sistema de Monitoramento de Cotacoes: visualizacao em tempo real, historico, performance, escalabilidade e interface responsiva.
- Website Institucional GMF-tech: site responsivo, performance, acessibilidade, animacoes e analytics.

Imagens usadas:

- `/velejar_facil.png`
- `/chart-project.jpg`
- `/website-project.jpg`

Verificar caminhos de assets depois do build web, especialmente se `base_url` for diferente de `/`.

## Responsividade

Breakpoints definidos em `utils/responsive.py`:

- Mobile: `<= 600px`.
- Tablet: `601px` a `900px`.
- Desktop: `> 900px`.

Escalas atuais:

- Fonte: mobile `0.85`, tablet `0.95`, desktop `1.0`.
- Espacamento: mobile `0.75`, tablet `0.9`, desktop `1.0`.
- Grid padrao: mobile `1`, tablet `2`, desktop `3`.
- Padding de container: mobile `20`, tablet `30`, desktop `40`.

Use os helpers existentes:

- `ResponsiveConfig.get_breakpoint(width)`.
- `ResponsiveConfig.get_font_size(base_size, breakpoint)`.
- `ResponsiveConfig.get_spacing(base_spacing, breakpoint)`.
- `ResponsiveConfig.get_grid_columns(breakpoint)`.
- `ResponsiveConfig.get_container_padding(breakpoint)`.
- `get_responsive_font_size(base_size, width)`.
- `get_responsive_padding(base_padding, width)`.
- `get_responsive_spacing(base_spacing, width)`.

Ao alterar layout, testar pelo menos larguras proximas de `400px`, `768px` e `1920px`.

## Tema Visual

Paleta atual em `theme.py`:

- `primary`: `#1a237e`
- `secondary`: `#0d47a1`
- `accent`: `#1e88e5`
- `error`: `#d32f2f`
- `warning`: `#ffa000`
- `success`: `#388e3c`
- `background`: `#f5f5f5`
- `surface`: `#ffffff`
- `text_primary`: `#212121`
- `text_secondary`: `#757575`

O visual atual e institucional, azul e Material-like. Se melhorar design, manter consistencia com a marca, mas evitar que toda a interface vire apenas variacoes de azul. Usar contraste, hierarquia tipografica, bons espacos e componentes Flet reais.

## Pagina De Cotacao

`pages/coins.py` mostra uma demo tecnica com USD/BRL:

- API: `https://economia.awesomeapi.com.br/json/daily/USD-BRL/15`.
- Em WebAssembly/Pyodide usa `pyodide.http.pyfetch`.
- Em ambiente local Python usa `httpx.AsyncClient`.
- Cache global por 5 minutos.
- Grafico gerado com PyECharts e renderizado em `flet_webview.WebView` via data URL base64.
- WebView deve ficar na mesma versao do Flet (`0.85.1`) para o build Flutter/WebAssembly compilar.

Cuidados:

- Em deploy estatico, a pagina depende de internet para AwesomeAPI.
- Verificar CORS no GitHub Pages.
- Se a meta for site estatico totalmente resiliente, adicionar fallback visual ou dados mockados.

## Contato E Login

Contato:

- `send_email()` hoje apenas imprime dados e retorna sucesso.
- `contact_content()` valida campos obrigatorios e mostra SnackBar.
- Nao existe envio real de email ainda.

Login:

- Modal simulado com Google, Apple e X.
- Mostra SnackBar de sucesso.
- Nao existe autenticacao real.
- O botao de login e escondido na pagina `/coins` para manter foco na demo de cotacao.

Nao apresentar login ou envio de formulario como funcionalidade real em copy publica sem implementar backend ou integracao.

## Testes

Configuracao:

- `pytest.ini` define `testpaths = tests`, padrao `test_*.py`, classes `Test*`, funcoes `test_*`, `-v` e `--strict-markers`.
- `.coveragerc` omite `tests/*`, caches, venvs, `dist/*`, `old.py` e `new2.py`.

Fixtures em `tests/conftest.py`:

- `mock_page`: 1024x768.
- `mobile_page`: 400x800.
- `tablet_page`: 768x1024.
- `desktop_page`: 1920x1080.
- `theme_colors`.

Cobertura de testes atual:

- `tests/test_theme.py`: tema, estilos, sombras e helpers responsivos.
- `tests/test_responsive.py`: breakpoints, fontes, espacamentos, colunas e padding.
- `tests/test_app.py`: expectativas de header/footer, rotas, login, resize e inicializacao.
- `tests/pages/test_home.py`: estrutura, responsividade e botoes.
- `tests/pages/test_services.py`: estrutura, cards, grids, listas e responsividade.
- `tests/pages/test_about.py`: estrutura, secoes, responsividade e larguras.
- `tests/pages/test_contact.py`: campos, validacao, SnackBars e responsividade.
- `tests/pages/test_coins.py`: loading, grafico, cache, fetch mockado e erros.
- `tests/pages/test_portfolio.py`: projetos, cards, imagens, tecnologias e ResponsiveRow.

Ao alterar comportamento, atualizar testes junto. Alguns testes sao mais estruturais/mocados do que integrados, entao nao assumir que passam como garantia visual completa.

## Contexto Codex

Este `AGENTS.md` e a fonte principal de contexto para Codex neste projeto.

- Registrar aqui decisoes importantes sobre produto, stack, build e deploy.
- Manter a direcao do projeto alinhada com Flet, Python 3, WebAssembly e GitHub Pages.
- Atualizar este arquivo quando comandos, rotas, servicos, assets ou fluxo de deploy mudarem.
- Nao recriar diretorios ou specs de outras ferramentas de agente; centralizar a orientacao do projeto neste arquivo.

## Arquivos Legados

`old.py`:

- Prototipo com Tabs, PyeCharts, `flet_webview` e grafico simples.
- Gera HTML de chart em `assets/chart.html`.
- Comentarios indicam dificuldades com grafico em web/browser.

`new2.py`:

- Prototipo de landing page em arquivo unico.
- Header, hero, cards de servicos, footer e modal de login simulados.
- Usa `page.window.width` e API antiga `ft.icons`.

Nao evoluir esses arquivos como produto principal. Se alguma ideia visual for reaproveitada, migrar para a arquitetura atual em `app.py`, `pages/`, `theme.py` e `utils/`.

## Cuidados Conhecidos

- `app.py` usa `ft.run(...)` protegido por `if __name__ == "__main__":`.
- `page.width` pode ser `None` no inicio de uma sessao Flet; usar fallback `page.width or 1024` antes de comparacoes.
- Ha inconsistencia entre documentacao/spec e codigo em `services.py`: README/spec falam em 3 colunas no desktop, mas o codigo atual usa 2 colunas para servicos quando `page.width >= 768`.
- README e footer misturam anos 2025 e 2026.
- Build web sai em `build/web/`; `.gitignore` ignora diretorios de build.
- Imagens existem em `assets/` e `images/`; evitar divergencia.
- Paths de imagem com `/arquivo.png` podem se comportar diferente dependendo de `base_url`.
- O grafico depende da API externa de cotacao e do CDN do ECharts usado pelo PyECharts. Para demonstracao comercial, ter mensagem de fallback elegante.

## Regras Para Novas Alteracoes

- Manter Flet como framework unico do frontend.
- Preferir controles e componentes Flet nativos, exceto onde houver decisao explicita do produto, como o grafico PyECharts da cotacao.
- Manter arquitetura por paginas em `pages/`.
- Manter tema centralizado em `theme.py`.
- Manter responsividade centralizada em `utils/responsive.py`.
- Evitar hardcodes de largura/altura quando houver helper responsivo aplicavel.
- Para codigo que roda no navegador via Pyodide, usar `pyfetch` quando necessario; para local/native, usar `httpx`.
- Nao adicionar dependencias pesadas sem necessidade clara.
- Nao tratar `old.py` e `new2.py` como arquivos produtivos.
- Atualizar README e testes quando mudar comandos, rotas, servicos, build ou comportamento de UI.
- Antes de finalizar uma mudanca relevante, rodar testes e, quando mexer em UI/build, gerar/validar o build web.

## Definition Of Done

Para alteracoes de codigo:

- App roda localmente com `python app.py`.
- Testes relevantes passam com `python -m pytest`.
- Layout foi pensado para mobile, tablet e desktop.
- Copy publica reflete GMF-tech com Flet como foco principal.
- Bundle web foi considerado para GitHub Pages.

Para alteracoes de deploy:

- `flet build web` executa sem erro.
- `base_url` esta adequado ao destino.
- Rotas funcionam em refresh/deep link ou existe fallback.
- Assets carregam corretamente no caminho final.
- Conteudo gerado para Pages foi colocado no local esperado pelo fluxo de deploy do repositorio.
