from urllib.parse import unquote

import flet as ft

from pages.contact import build_mailto_url, contact_content
from tests.helpers import find_controls, text_exists
from theme import COLORS


def _fields(result):
    fields = find_controls(result, ft.TextField)
    return {field.label: field for field in fields}


def _submit_button(result):
    return next(
        button
        for button in find_controls(result, ft.Button)
        if button.content == "Continuar por e-mail"
    )


def test_contact_renders_commercial_landing(mock_page):
    result = contact_content(mock_page)

    assert isinstance(result, ft.Container)
    assert isinstance(result.content, ft.Column)
    assert len(result.content.controls) == 2
    assert text_exists(result, "Converse com a GMF-tech sobre seu próximo projeto")
    assert text_exists(result, "Novo produto digital")
    assert text_exists(result, "Modernização e integração")
    assert text_exists(result, "Dados e automação")


def test_contact_form_has_required_fields_and_button(mock_page):
    result = contact_content(mock_page)
    fields = _fields(result)

    assert set(fields) == {"Nome", "E-mail", "Contexto do projeto"}
    assert fields["Contexto do projeto"].multiline is True
    assert fields["Contexto do projeto"].min_lines == 5
    assert _submit_button(result).on_click is not None


def test_contact_validation_shows_error_for_empty_fields(mock_page):
    result = contact_content(mock_page)

    _submit_button(result).on_click(None)

    assert isinstance(mock_page.snack_bar, ft.SnackBar)
    assert mock_page.snack_bar.bgcolor == COLORS["error"]
    assert "preencha todos os campos" in mock_page.snack_bar.content.value.lower()
    assert mock_page.snack_bar.open is True


def test_contact_submit_opens_prefilled_email_without_claiming_it_was_sent(mock_page):
    result = contact_content(mock_page)
    fields = _fields(result)
    fields["Nome"].value = "Gustavo"
    fields["E-mail"].value = "gustavo@gmf-tech.com"
    fields["Contexto do projeto"].value = "Quero automatizar atendimento com IA"

    _submit_button(result).on_click(None)

    mock_page.launch_url.assert_called_once()
    mailto_url = unquote(mock_page.launch_url.call_args.args[0])
    assert mailto_url.startswith("mailto:contato@gmf-tech.com")
    assert "Nome: Gustavo" in mailto_url
    assert "Email: gustavo@gmf-tech.com" in mailto_url
    assert "Quero automatizar atendimento com IA" in mailto_url
    assert mock_page.snack_bar.bgcolor == COLORS["success"]
    assert "aplicativo de e-mail" in mock_page.snack_bar.content.value
    assert fields["Nome"].value == "Gustavo"
    assert fields["E-mail"].value == "gustavo@gmf-tech.com"
    assert fields["Contexto do projeto"].value == "Quero automatizar atendimento com IA"


def test_build_mailto_url_encodes_subject_and_project_context():
    url = unquote(build_mailto_url("Nome", "nome@empresa.com", "Portal & API"))

    assert "subject=Contato pelo site GMF-tech" in url
    assert "Contexto do projeto:\nPortal & API" in url


def test_contact_field_widths_are_responsive(mobile_page, tablet_page, desktop_page):
    mobile_fields = _fields(contact_content(mobile_page))
    tablet_fields = _fields(contact_content(tablet_page))
    desktop_fields = _fields(contact_content(desktop_page))

    assert mobile_fields["Nome"].width is None
    assert tablet_fields["Nome"].width == 440
    assert desktop_fields["Nome"].width == 440
