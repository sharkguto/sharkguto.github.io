import flet as ft

from pages.about import about_content
from tests.helpers import find_controls, text_exists
from theme import COLORS


def test_about_renders_current_positioning(mock_page):
    result = about_content(mock_page)

    assert isinstance(result, ft.Container)
    assert isinstance(result.content, ft.Column)
    assert len(result.content.controls) == 3
    assert result.bgcolor == COLORS["background"]

    assert text_exists(result, "Sobre a GMF-tech")
    assert text_exists(result, "Fábrica de software")
    assert text_exists(result, "Identidade GMF-tech")


def test_about_lists_current_value_cards(mock_page):
    result = about_content(mock_page)

    for label in ["Consultoria e discovery", "Desenvolvimento sob medida", "Entrega e operação"]:
        assert text_exists(result, label)


def test_about_lists_work_model(mock_page):
    result = about_content(mock_page)

    for label in ["Como conduzimos cada projeto", "1. Descoberta e escopo", "2. Engenharia e validação", "3. Implantação e evolução"]:
        assert text_exists(result, label)


def test_about_uses_caravela_favicon(mock_page):
    result = about_content(mock_page)
    images = find_controls(result, ft.Image)

    assert any(image.src == "/favicon.png" for image in images)


def test_about_uses_document_flow_across_breakpoints(mobile_page, tablet_page, desktop_page):
    for page in [mobile_page, tablet_page, desktop_page]:
        result = about_content(page)
        assert result.content.scroll is None
        assert result.height is None
