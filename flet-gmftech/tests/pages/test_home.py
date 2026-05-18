import flet as ft

from pages.home import home_content
from tests.helpers import find_controls, text_exists
from theme import COLORS


def test_home_renders_new_gmftech_landing(mock_page):
    result = home_content(mock_page)

    assert isinstance(result, ft.Container)
    assert isinstance(result.content, ft.Column)
    assert len(result.content.controls) == 3
    assert result.bgcolor == COLORS["background"]

    assert text_exists(result, "Software, Flet e IA para acelerar sua operação")
    assert text_exists(result, "Flet-first software studio")
    assert text_exists(result, "Cobertura full-stack")
    assert text_exists(result, "Modelo de trabalho")


def test_home_exposes_primary_services(mock_page):
    result = home_content(mock_page)

    for label in [
        "Levantamento de Requisitos",
        "Arquitetura de Software",
        "IoT e Prototipagem",
        "Web e Mobile",
        "Cloud e Segurança",
        "Consultoria e Automação com IA",
    ]:
        assert text_exists(result, label)


def test_home_has_three_hero_navigation_buttons(mock_page):
    result = home_content(mock_page)
    buttons = find_controls(result, ft.Button)
    button_labels = [button.content for button in buttons if isinstance(button.content, str)]

    assert "Agendar diagnóstico" in button_labels
    assert "Ver serviços" in button_labels
    assert "Portfólio" in button_labels


def test_home_navigation_buttons_route_correctly(mock_page):
    result = home_content(mock_page)
    buttons = {
        button.content: button
        for button in find_controls(result, ft.Button)
        if isinstance(button.content, str)
    }

    buttons["Agendar diagnóstico"].on_click(None)
    mock_page.push_route.assert_called_with("/contact")

    buttons["Ver serviços"].on_click(None)
    mock_page.push_route.assert_called_with("/services")

    buttons["Portfólio"].on_click(None)
    mock_page.push_route.assert_called_with("/portfolio")


def test_home_mobile_keeps_document_flow_layout(mobile_page):
    result = home_content(mobile_page)
    button_labels = [button.content for button in find_controls(result, ft.Button) if isinstance(button.content, str)]

    assert result.height is None
    assert result.content.scroll is None
    assert "Agendar diagnóstico" in button_labels
