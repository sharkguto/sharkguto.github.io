import base64
import flet as ft
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

# Gera o gráfico com pyecharts
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(["A", "B", "C"])
    .add_yaxis("Series 1", [1, 2, 4])
    .set_global_opts(title_opts=opts.TitleOpts(title="Gráfico de Barras"))
)

# Obtém o HTML incorporado do gráfico
html = bar.render_embed()

# Codifica o HTML em Base64 e cria um data URL
encoded_html = base64.b64encode(html.encode("utf-8")).decode("utf-8")
data_url = f"data:text/html;base64,{encoded_html}"


def main(page: ft.Page):
    page.title = "Pyecharts in Flet - Responsivo"
    page.scroll = "adaptive"

    header = ft.Text(
        "Gráfico Integrado Pyecharts com Flet",
        style="headlineMedium",
        weight="bold",
        text_align=ft.TextAlign.CENTER,
    )

    # Cria o WebView usando o parâmetro 'url' e define a altura fixa para o gráfico
    chart_webview = ft.WebView(url=data_url, expand=True)
    chart_webview.height = 400  # altura fixa para o gráfico

    # Container que envolve o gráfico; ele expande para preencher a largura disponível
    chart_container = ft.Container(
        content=chart_webview,
        expand=True,
        padding=10,
        border=ft.border.all(1, ft.colors.OUTLINE),
        border_radius=5,
    )

    # Layout principal em coluna, que se adapta ao tamanho da tela
    layout = ft.Column(
        controls=[
            header,
            ft.Divider(),
            chart_container,
        ],
        expand=True,
        spacing=20,
    )

    page.add(layout)


ft.app(target=main, view=ft.WEB_BROWSER)
