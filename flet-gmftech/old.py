import base64
import os
import flet as ft
import flet_webview as fwv
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType


def update_chart_file():
    bar = (
        Bar(
            init_opts=opts.InitOpts(width="100%", height="400px", theme=ThemeType.LIGHT)
        )
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("Series 1", [1, 2, 4])
        .set_global_opts(title_opts=opts.TitleOpts(title="Gráfico Responsivo"))
    )
    html = bar.render_embed()
    assets_dir = "assets"
    if not os.path.exists(assets_dir):
        os.makedirs(assets_dir)
    file_path = os.path.join(assets_dir, "chart.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)


# Função para definir a altura do WebView como 80% da altura da página
def set_webview_height(page, chart_webview):
    page_height = page.height
    chart_webview.height = int(page_height * 0.8)


def main(page: ft.Page):
    page.title = "Empresa de Outsourcing em TI"
    page.scroll = "adaptive"
    page.padding = 20  # garante que haja espaçamento na página

    home_content = ft.Column(
        controls=[
            ft.Text(
                "Bem-vindo à Empresa GMF-TECH",
                style=ft.TextThemeStyle.HEADLINE_LARGE,
            ),
            ft.Text(
                "Soluções inovadoras em outsourcing de TI.",
                style=ft.TextThemeStyle.HEADLINE_SMALL,
            ),
        ],
        expand=True,
        spacing=5,
    )

    # Conteúdo da aba "Serviços"
    services_content = ft.Column(
        controls=[
            ft.Text(
                "Nossos Serviços",
                style=ft.TextThemeStyle.HEADLINE_MEDIUM,
            ),
            ft.Text("• Desenvolvimento de Software"),
            ft.Text("• Suporte Técnico"),
            ft.Text("• Consultoria em TI"),
            ft.Text("• Gerenciamento de Infraestrutura"),
        ],
        expand=True,
        spacing=5,
    )

    ######################################################################
    #######################################################################

    # Gera o gráfico com pyecharts
    bar = (
        Bar(
            init_opts=opts.InitOpts(width="100%", height="400px", theme=ThemeType.LIGHT)
        )
        .add_xaxis(["A", "B", "C"])
        .add_yaxis("Series 1", [1, 2, 4])
        .set_global_opts(title_opts=opts.TitleOpts(title="Gráfico Responsivo"))
    )

    # Obtém o HTML incorporado do gráfico
    html = bar.render_embed()

    # Codifica o HTML em Base64 e cria um data URL
    encoded_html = base64.b64encode(html.encode("utf-8")).decode("utf-8")
    data_url = f"data:text/html;base64,{encoded_html}"

    chart_webview = fwv.WebView(
        url=data_url,
        # url=chart_url,
        on_page_started=lambda _: page.eval_js(
            "console.log('Log do navegador: echarts iniciado!');"
        ),
        on_page_ended=lambda _: page.eval_js(
            "console.log('Log do navegador: echarts carregou!');"
        ),
        on_web_resource_error=lambda e: page.eval_js(
            f"console.log('Log do navegador: erro: {e.data}!');"
        ),
        expand=True,
    )

    chart_webview.height = page.height - 48  # altura fixa para o gráfico

    header = ft.Text(
        "Gráfico Integrado Pyecharts com Flet",
        style="headlineMedium",
        weight="bold",
        text_align=ft.TextAlign.CENTER,
    )

    # Container que envolve o gráfico; ele expande para preencher a largura disponível
    chart_container = ft.Container(
        content=chart_webview,
        expand=True,
        padding=10,
        border=ft.border.all(1, ft.Colors.OUTLINE),
        border_radius=5,
    )

    # Layout principal em coluna, que se adapta ao tamanho da tela
    market_container = ft.Column(
        controls=[
            header,
            ft.Divider(),
            chart_container,
        ],
        expand=True,
        spacing=20,
    )

    ###############################################################################
    ###############################################################################

    # Conteúdo da aba "Sobre Nós"
    about_content = ft.Column(
        controls=[
            ft.Text("Sobre Nós", style="headlineMedium"),
            ft.Text(
                "Somos uma empresa dedicada a fornecer soluções de outsourcing em TI com excelência e inovação. "
                "Nossa equipe especializada garante que as operações de TI dos nossos clientes sejam eficientes e seguras."
            ),
        ],
        expand=True,
        spacing=10,
    )

    # Criação das abas
    tabs = ft.Tabs(
        selected_index=0,  # define a aba "Início" como padrão
        tabs=[
            ft.Tab(
                text="Início",
                content=ft.Container(content=home_content, padding=20, expand=True),
            ),
            ft.Tab(
                text="Serviços",
                content=ft.Container(content=services_content, padding=20, expand=True),
            ),
            ft.Tab(
                text="Sobre Nós",
                content=ft.Container(content=about_content, padding=20, expand=True),
            ),
            ft.Tab(
                text="Comparativo de Mercado",
                content=ft.Container(content=market_container, padding=20, expand=True),
            ),
        ],
        expand=True,
    )

    page.add(tabs)
    page.on_resized = (
        lambda e: set_webview_height(page, chart_webview)
        if e.data == "window_resize"
        else None
    )
    page.update()


# Se estiver usando WEB_BROWSER, a aba do gráfico exibirá o aviso;
# Para ver o gráfico, execute como aplicativo desktop:
ft.app(target=main, view=ft.WEB_BROWSER)
# Para testar o gráfico, descomente uma das linhas abaixo:
# ft.app(target=main, view=ft.FLET_APP)
# ft.app(target=main, view=ft.DESKTOP)
