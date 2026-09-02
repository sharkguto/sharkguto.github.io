from unittest.mock import Mock

import flet as ft

from app import main
from tests.helpers import find_controls, text_exists
from theme import COLORS


def _page_layout(page):
    return page.controls[0]


def _footer(page):
    return _page_layout(page).controls[1]


def _header_buttons(page):
    navigation_row = page.appbar.actions[0]
    return {
        button.content: button
        for button in navigation_row.controls
        if isinstance(button.content, str)
    }


def test_main_initializes_page_and_initial_route(mock_page):
    main(mock_page)

    assert mock_page.title == "GMF-tech | Fábrica de software"
    assert mock_page.bgcolor == COLORS["background"]
    assert mock_page.scroll is None
    assert mock_page.padding == 0
    assert mock_page.theme_mode == ft.ThemeMode.LIGHT
    assert isinstance(mock_page.appbar, ft.AppBar)
    assert len(mock_page.controls) == 1
    assert mock_page._content_scroller is mock_page.controls[0].controls[0]
    assert text_exists(
        _page_layout(mock_page),
        "Arquitetura de soluções e sistemas sob medida",
    )
    assert not mock_page.run_task.called
    assert mock_page.update.called


def test_desktop_header_has_navigation_and_commercial_cta(desktop_page):
    main(desktop_page)

    buttons = _header_buttons(desktop_page)
    assert "Início" in buttons
    assert "Serviços" in buttons
    assert "Contato" in buttons
    assert "Portfólio" in buttons
    assert "Fale com a GMF-tech" in buttons

    buttons["Fale com a GMF-tech"].on_click(None)
    desktop_page.push_route.assert_called_with("/contact")


def test_mobile_header_uses_drawer_with_commercial_cta(mobile_page):
    main(mobile_page)

    assert isinstance(mobile_page.drawer, ft.NavigationDrawer)
    assert text_exists(mobile_page.drawer, "Engenharia de software sob medida")
    drawer_titles = [
        control.title.value
        for control in mobile_page.drawer.controls
        if isinstance(control, ft.ListTile)
    ]
    assert "Portfólio" in drawer_titles
    assert "Fale com a GMF-tech" in drawer_titles

    menu_button = mobile_page.appbar.actions[0]
    assert isinstance(menu_button, ft.IconButton)
    menu_button.on_click(None)
    assert mobile_page.show_drawer.called


def test_route_change_renders_requested_page(mock_page):
    main(mock_page)

    mock_page.on_route_change(Mock(route="/services"))

    assert mock_page.route == "/services"
    assert text_exists(_page_layout(mock_page), "Serviços de engenharia de software")


def test_footer_is_fixed_outside_scroll_region(mock_page):
    main(mock_page)

    layout = _page_layout(mock_page)
    scroll_region, footer = layout.controls
    assert isinstance(scroll_region, ft.Column)
    assert scroll_region.expand is True
    assert scroll_region.scroll == ft.ScrollMode.AUTO
    assert footer not in scroll_region.controls
    assert layout.controls[-1] is footer
    assert footer.bgcolor == COLORS["primary"]
    assert text_exists(footer, "GMF-tech")
    assert text_exists(footer, "Fábrica de software sob medida")
    assert text_exists(footer, "contato@gmf-tech.com")
    assert not find_controls(footer, ft.IconButton)
    footer_links = [
        control.url
        for control in find_controls(footer, ft.Container)
        if control.url
    ]
    assert "mailto:contato@gmf-tech.com" in footer_links


def test_resize_rebuilds_header_drawer_and_footer(mock_page):
    main(mock_page)
    original_footer = _footer(mock_page)

    mock_page.width = 400
    mock_page.on_resize(None)

    assert isinstance(mock_page.drawer, ft.NavigationDrawer)
    assert _footer(mock_page) is not original_footer
    assert mock_page.update.called


def test_desktop_market_page_omits_duplicate_commercial_cta(desktop_page):
    desktop_page.route = "/coins"
    main(desktop_page)

    assert "Fale com a GMF-tech" not in _header_buttons(desktop_page)
