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

    assert text_exists(result, "Arquitetura de soluções e sistemas sob medida")
    assert text_exists(result, "Fábrica de software especializada")
    assert text_exists(result, "Especialização técnica para soluções completas")
    assert text_exists(result, "Processo de entrega")


def test_home_exposes_primary_services(mock_page):
    result = home_content(mock_page)

    for label in [
        "Arquitetura de Soluções",
        "Backend Python e FastAPI",
        "Frontend React",
        "Aplicações com Flet",
        "Dados e Integrações",
        "Cloud, DevOps e Segurança",
    ]:
        assert text_exists(result, label)


def test_home_has_three_hero_navigation_buttons(mock_page):
    result = home_content(mock_page)
    buttons = find_controls(result, ft.Button)
    button_labels = [button.content for button in buttons if isinstance(button.content, str)]

    assert "Falar sobre um projeto" in button_labels
    assert "Conhecer serviços" in button_labels
    assert "Ver projetos" in button_labels


def test_home_navigation_buttons_route_correctly(mock_page):
    result = home_content(mock_page)
    buttons = {
        button.content: button
        for button in find_controls(result, ft.Button)
        if isinstance(button.content, str)
    }

    buttons["Falar sobre um projeto"].on_click(None)
    mock_page.push_route.assert_called_with("/contact")

    buttons["Conhecer serviços"].on_click(None)
    mock_page.push_route.assert_called_with("/services")

    buttons["Ver projetos"].on_click(None)
    mock_page.push_route.assert_called_with("/portfolio")


def test_home_mobile_keeps_document_flow_layout(mobile_page):
    result = home_content(mobile_page)
    button_labels = [button.content for button in find_controls(result, ft.Button) if isinstance(button.content, str)]

    assert result.height is None
    assert result.content.scroll is None
    assert "Falar sobre um projeto" in button_labels
