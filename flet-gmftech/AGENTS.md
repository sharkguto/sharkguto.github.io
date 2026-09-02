# AGENTS.md

Instrucoes para agentes que trabalham no codigo da GMF-tech.

## Escopo e limite do repositorio

- Este arquivo se aplica a toda a arvore `flet-gmftech/`.
- Todo codigo-fonte, teste, asset e documentacao do app deve permanecer dentro de
  `flet-gmftech/`.
- A raiz do repositorio contem os arquivos publicados no GitHub Pages. Trate-a
  como somente leitura: nao crie, edite, mova, apague ou formate arquivos fora de
  `flet-gmftech/`.
- Nao copie `build/web/` para a raiz e nao execute scripts de deploy sem um pedido
  explicito do usuario.
- Execute os comandos de desenvolvimento com `flet-gmftech/` como diretorio de
  trabalho. Use o prefixo `rtk` nos comandos de shell, conforme a instrucao
  herdada do repositorio.
- Use `uv` sempre para gerenciar o ambiente, instalar dependencias e executar
  comandos Python. Nao invoque `python`, `pip`, `pytest` ou `flet` diretamente e
  nao crie ambientes virtuais manualmente.
- Antes de editar, confira `rtk git status --short` e preserve alteracoes do
  usuario. Nao reverta trabalho alheio nem faca refatoracoes fora do pedido.

## Produto e stack

Este projeto e o site institucional da GMF-tech. Ele e uma aplicacao web escrita
em Python e Flet, compilada como bundle estatico WebAssembly/Pyodide para o
GitHub Pages.

Use como fontes de verdade:

- `pyproject.toml` para versao do Python, dependencias e configuracao do Flet;
- `requirements.txt` para dependencias compativeis com Pyodide;
- `requirements-dev.txt` para o ambiente local;
- `README.md` para o fluxo de desenvolvimento e publicacao;
- os testes para os contratos de comportamento existentes.

Stack atual:

- Python 3.14 (`>=3.14,<3.15` para manter o runtime web compativel);
- Flet e `flet-webview` 0.86.5;
- PyECharts 2.1.0;
- HTTPX 0.28.1;
- Pyodide 314.0.3 no bundle web.

Flet e o framework do frontend e parte central do posicionamento do produto.
Nao migre telas para React, Vue, Next, Astro ou HTML/JavaScript paralelo. Nao
adicione dependencias pesadas sem uma necessidade concreta e verificavel.

## Mapa do codigo

- `app.py`: entrada do Flet, configuracao da pagina, cabecalho, navegacao,
  drawer, footer, rotas e dialogos globais.
- `theme.py`: paleta e helpers compartilhados de tema, tipografia, botoes e
  sombras.
- `utils/responsive.py`: breakpoints, fontes, espacamentos, colunas e padding
  responsivos.
- `utils/flet_runtime.py`: compatibilidade entre metodos sync e async de
  `ft.Page`.
- `pages/home.py`: pagina inicial.
- `pages/services.py`: servicos, tecnologias e painel interativo de stacks.
- `pages/about.py`: posicionamento e processo de trabalho.
- `pages/contact.py`: formulario e validacao de contato.
- `pages/portfolio.py`: projetos e tecnologias utilizadas.
- `pages/coins.py`: cotacoes, cache, integracoes HTTP, graficos PyECharts e
  renderizacao por WebView.
- `tests/`: testes unitarios do app, paginas, tema e responsividade.
- `tools/validate_frontend_playwright.py`: smoke test do bundle web servido.
- `assets/`: arquivos consumidos pelo Flet no build web.

`old.py` e `new2.py` sao prototipos legados. Nao os use como base para novas
mudancas e nao os evolua junto com o produto. A pasta `images/` duplica parte do
portfolio; para codigo novo, prefira `assets/`.

## Regras de implementacao

- Mantenha o ponto de entrada e o roteamento em `app.py`; mantenha o conteudo de
  cada tela em seu modulo dentro de `pages/`.
- Reutilize `COLORS` e os helpers de `theme.py`. Nao espalhe novas cores,
  tipografias ou estilos equivalentes pelas paginas.
- Reutilize `ResponsiveConfig` em vez de criar breakpoints locais. Considere
  `page.width` como opcional e use um fallback coerente quando ele for `None`.
- Para chamadas de pagina que variam entre runtime sync e async, use
  `call_page_method()` conforme o padrao existente.
- Ao criar ou alterar uma rota, atualize navegacao desktop, drawer mobile,
  resolucao de rota e testes relacionados.
- Use controles e icones nativos do Flet. Preserve o sistema visual atual:
  secoes full-width, hierarquia compacta, cards com raio discreto e layout sem
  cards aninhados.
- Garanta que a interface funcione em mobile, tablet e desktop. Verifique como
  referencia larguras de 400, 768 e 1920 pixels.
- Mantenha o site em portugues e preserve a identidade GMF-tech. Mudancas de copy
  nao devem prometer recursos ainda simulados ou inexistentes.
- `pages/contact.py` nao envia email de verdade. Nao apresente a acao simulada
  como integracao concluida sem implementar e testar um backend apropriado.
- Preserve acessibilidade basica: rotulos claros, contraste, estados de erro e
  alvos de interacao utilizaveis em telas pequenas.

## Cotacoes e codigo assincrono

`pages/coins.py` concentra a parte mais sensivel do app. Ao altera-lo:

- preserve a separacao entre busca de dados, normalizacao, cache, geracao do
  grafico e controles Flet;
- mantenha suporte a `pyodide.http.pyfetch` no navegador e a `httpx.AsyncClient`
  no runtime local;
- mantenha timeouts, tratamento de falhas e o fallback demonstrativo
  deterministico para acoes;
- nao faca chamadas de rede reais em testes unitarios; use mocks;
- preserve a validade do HTML/data URL entregue ao `WebView`;
- use PyECharts para os graficos, salvo decisao explicita de arquitetura.

As fontes externas podem falhar ou mudar de payload. Valide dados antes de
acessar campos e cubra casos de resposta vazia, invalida ou parcial.

## Compatibilidade Flet e Pyodide

- Use APIs compativeis com Flet 0.86.5.
- Para bordas, use `ft.Border.all(...)`, nao a API antiga `ft.border.all(...)`.
- Em `PopupMenuItem`, use `content=ft.Text(...)`; `text=...` nao e aceito nesta
  versao.
- Nao coloque `flet-web` em `requirements.txt`; ele e apenas uma dependencia de
  desenvolvimento/serve e pode quebrar a resolucao no Pyodide.
- Mantenha `typing_extensions` explicito enquanto `flet_webview` depender dele
  no runtime web.
- Preserve `route_url_strategy = "hash"` para o GitHub Pages.
- Nao use `flet build web --no-cdn` sem revisar o Pyodide local e o processo de
  publicacao.

## Comandos de desenvolvimento

Execute a partir de `flet-gmftech/`:

```bash
rtk uv sync --extra test --extra serve
rtk uv run python app.py
```

Para ferramentas Python avulsas que nao fazem parte do projeto, use `rtk uvx`.
Ao mudar dependencias, altere `pyproject.toml` e atualize a resolucao com `uv`;
nao instale pacotes diretamente no ambiente.

Para uma verificacao rapida durante a implementacao:

```bash
rtk uv run python -m pytest tests/pages/test_home.py -q
```

Troque o caminho pelo teste diretamente relacionado a mudanca. Antes de
finalizar uma alteracao de codigo, execute:

```bash
rtk uv run python -m compileall app.py pages theme.py utils tests
rtk uv run python -m pytest
```

Para mudancas que afetam renderizacao, assets, dependencias ou configuracao web:

```bash
rtk uv run flet build web --yes
```

O build deve ficar em `flet-gmftech/build/web/`. Nao mova o resultado para a
raiz. O smoke test do Playwright exige que esse bundle esteja sendo servido; use
o fluxo documentado no `README.md`, sem alterar os arquivos de infraestrutura da
raiz.

## Testes e conclusao

- Adicione ou atualize testes no mesmo trabalho sempre que mudar comportamento.
- Testes de pagina devem usar os fixtures de `tests/conftest.py` e os helpers de
  `tests/helpers.py` para percorrer controles.
- Testes unitarios devem ser deterministas e independentes de internet, relogio
  real e estado deixado por outro teste.
- Para uma cor, helper ou breakpoint novo, cubra `theme.py` ou
  `utils/responsive.py` diretamente.
- Para mudancas visuais, valide ausencia de overflow, sobreposicao e texto
  cortado nos tres breakpoints de referencia.
- Nao versione caches, cobertura, ambientes virtuais ou `build/`.
- Ao terminar, confira o diff e confirme que nenhum arquivo fora de
  `flet-gmftech/` foi alterado.

Uma mudanca esta concluida quando os testes relevantes passam, os testes gerais
foram executados em alteracoes de codigo compartilhado, o comportamento web foi
validado quando aplicavel e a raiz do repositorio permaneceu intacta.
