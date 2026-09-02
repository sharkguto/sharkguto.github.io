import flet as ft

from pages.services import services_content
from tests.helpers import find_controls, text_exists
from theme import COLORS


def _service_grid(result):
    return result.content.controls[1].content


def _tech_grid(result):
    return result.content.controls[3].content


def _stack_panel(result):
    detail_wrapper = next(
        control
        for control in _service_grid(result).controls
        if control.data == "service-detail"
    )
    return detail_wrapper.content


def _service_wrappers(result):
    return [
        control
        for control in _service_grid(result).controls
        if control.data != "service-detail"
    ]


def test_services_renders_header_grids_and_stack(mock_page):
    result = services_content(mock_page)

    assert isinstance(result, ft.Container)
    assert isinstance(result.content, ft.Column)
    assert len(result.content.controls) == 4
    assert text_exists(result, "Serviços de engenharia de software")
    assert text_exists(result, "Tecnologias e plataformas")
    assert text_exists(result, "Detalhes do serviço")
    assert text_exists(_stack_panel(result), "Arquitetura de Software")

    services_grid = _service_grid(result)
    tech_grid = _tech_grid(result)
    assert isinstance(services_grid, ft.ResponsiveRow)
    assert isinstance(tech_grid, ft.ResponsiveRow)
    assert len(services_grid.controls) == 10
    assert len(tech_grid.controls) == 12


def test_services_lists_current_offers(mock_page):
    result = services_content(mock_page)

    for label in [
        "Levantamento de Requisitos",
        "Arquitetura de Software",
        "IoT com Arduino",
        "Prototipagem Eletrônica",
        "Desenvolvimento Web",
        "Desenvolvimento Mobile",
        "Cloud Computing",
        "Segurança",
        "Automação e Inteligência Artificial",
    ]:
        assert text_exists(result, label)


def test_services_lists_current_technologies(mock_page):
    result = services_content(mock_page)

    for label in ["Python", "Flet", "React", "Node.js", "PostgreSQL", "Cloudflare", "AWS", "Azure DevOps", "IA e LLMs"]:
        assert text_exists(result, label)


def test_services_grid_responsiveness(mobile_page, tablet_page, desktop_page):
    mobile_result = services_content(mobile_page)
    tablet_result = services_content(tablet_page)
    desktop_result = services_content(desktop_page)

    for result in [mobile_result, tablet_result, desktop_result]:
        assert _service_wrappers(result)[0].col == {"sm": 12, "md": 6, "lg": 4}
        assert _tech_grid(result).controls[0].col == {"sm": 12, "md": 6, "lg": 4}


def test_services_detail_follows_selected_row_at_each_breakpoint(mobile_page, tablet_page, desktop_page):
    expected_detail_positions = [1, 2, 3]

    for page, expected_position in zip(
        [mobile_page, tablet_page, desktop_page],
        expected_detail_positions,
        strict=True,
    ):
        grid = _service_grid(services_content(page))
        assert grid.controls[expected_position].data == "service-detail"


def test_services_cards_keep_gmftech_styling(mock_page):
    result = services_content(mock_page)
    first_card = _service_wrappers(result)[0].content

    assert isinstance(first_card, ft.Container)
    assert first_card.bgcolor != COLORS["surface"]
    assert first_card.border is not None
    assert first_card.border_radius == ft.BorderRadius.all(8)
    assert first_card.shadow is not None
    assert first_card.on_click is not None
    assert text_exists(first_card, "Arquitetura de Software")


def test_services_clicking_card_updates_stack_panel(mock_page):
    result = services_content(mock_page)
    services_grid = _service_grid(result)
    service_wrappers = _service_wrappers(result)

    service_wrappers[8].content.on_click(None)

    assert text_exists(_stack_panel(result), "Automação e Inteligência Artificial")
    assert text_exists(_stack_panel(result), "LLMs")
    assert service_wrappers[8].content.border.top.width == 2
    assert text_exists(service_wrappers[8].content, "Selecionado")
    assert text_exists(service_wrappers[0].content, "Ver detalhes")
    assert services_grid.controls[-1].data == "service-detail"
    assert mock_page.update.called
    mock_page.run_task.assert_called_once()


def test_services_stack_panel_has_clickable_service_stacks(mock_page):
    result = services_content(mock_page)
    chips = find_controls(_stack_panel(result), ft.Text)
    values = [chip.value for chip in chips if getattr(chip, "value", None)]

    assert "FastAPI" in values
    assert "PostgreSQL" in values
    assert "Azure DevOps" in values
