import flet as ft

from pages.portfolio import portfolio_content
from tests.helpers import find_controls, text_exists
from theme import COLORS


def _projects_row(result):
    return result.content.controls[1].content


def test_portfolio_renders_enterprise_case_studies(mock_page):
    result = portfolio_content(mock_page)

    assert isinstance(result, ft.Container)
    assert isinstance(result.content, ft.Column)
    assert len(result.content.controls) == 3
    assert text_exists(result, "Projetos com Flet, dados e automacao em producao")
    assert text_exists(result, "Stack GMF-tech")


def test_portfolio_lists_three_projects(mock_page):
    result = portfolio_content(mock_page)
    row = _projects_row(result)

    assert isinstance(row, ft.ResponsiveRow)
    assert len(row.controls) == 3

    assert text_exists(result, "Velejar Facil")
    assert text_exists(result, "Monitoramento de Cotacoes")
    assert text_exists(result, "Website GMF-tech")


def test_portfolio_cards_have_images_and_technologies(mock_page):
    result = portfolio_content(mock_page)
    images = find_controls(result, ft.Image)

    assert any(image.src == "/velejar_facil.png" for image in images)
    assert any(image.src == "/chart-project.jpg" for image in images)
    assert any(image.src == "/website-project.jpg" for image in images)

    for label in ["Python", "Flet", "PyECharts", "WebAssembly", "Playwright"]:
        assert text_exists(result, label)


def test_portfolio_card_layout_uses_current_visual_system(mock_page):
    result = portfolio_content(mock_page)
    first_project_wrapper = _projects_row(result).controls[0]
    first_card = first_project_wrapper.content

    assert first_project_wrapper.col == {"sm": 12, "md": 6, "lg": 4}
    assert first_project_wrapper.padding == 8
    assert first_card.bgcolor == COLORS["surface"]
    assert first_card.border_radius == ft.BorderRadius.all(8)
    assert first_card.shadow is not None


def test_velejar_facil_card_links_to_live_site(mock_page):
    result = portfolio_content(mock_page)
    cards = [wrapper.content for wrapper in _projects_row(result).controls]
    velejar_card, quotes_card, gmftech_card = cards

    assert velejar_card.url == "https://www.velejarfacil.com.br/"
    assert velejar_card.ink is True
    assert velejar_card.tooltip == "Abrir Velejar Facil"
    assert quotes_card.url is None
    assert gmftech_card.url is None


def test_portfolio_image_sizes_follow_breakpoints(mobile_page, tablet_page, desktop_page):
    mobile_image = next(image for image in find_controls(portfolio_content(mobile_page), ft.Image) if image.src == "/velejar_facil.png")
    tablet_image = next(image for image in find_controls(portfolio_content(tablet_page), ft.Image) if image.src == "/velejar_facil.png")
    desktop_image = next(image for image in find_controls(portfolio_content(desktop_page), ft.Image) if image.src == "/velejar_facil.png")

    assert mobile_image.width == 320
    assert mobile_image.height == 200
    assert tablet_image.width == 330
    assert tablet_image.height == 220
    assert desktop_image.width == 390
    assert desktop_image.height == 250
