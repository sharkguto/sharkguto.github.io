import flet as ft

import pages.contact as contact_module
from pages.contact import contact_content
from tests.helpers import find_controls, text_exists
from theme import COLORS


def _fields(result):
    fields = find_controls(result, ft.TextField)
    return {field.label: field for field in fields}


def _submit_button(result):
    return next(
        button
        for button in find_controls(result, ft.Button)
        if button.content == "Enviar diagnostico"
    )


def test_contact_renders_diagnostic_landing(mock_page):
    result = contact_content(mock_page)

    assert isinstance(result, ft.Container)
    assert isinstance(result.content, ft.Column)
    assert len(result.content.controls) == 2
    assert text_exists(result, "Agende um diagnostico para Flet, IA e automacao")
    assert text_exists(result, "Projeto Flet")
    assert text_exists(result, "Consultoria de IA")
    assert text_exists(result, "Automacao")


def test_contact_form_has_required_fields_and_button(mock_page):
    result = contact_content(mock_page)
    fields = _fields(result)

    assert set(fields) == {"Nome", "Email", "Mensagem"}
    assert fields["Mensagem"].multiline is True
    assert fields["Mensagem"].min_lines == 5
    assert _submit_button(result).on_click is not None


def test_contact_validation_shows_error_for_empty_fields(mock_page):
    result = contact_content(mock_page)

    _submit_button(result).on_click(None)

    assert isinstance(mock_page.snack_bar, ft.SnackBar)
    assert mock_page.snack_bar.bgcolor == COLORS["error"]
    assert "preencha todos os campos" in mock_page.snack_bar.content.value
    assert mock_page.snack_bar.open is True


def test_contact_submit_calls_send_email_and_clears_fields(mock_page, monkeypatch):
    calls = []

    def fake_send_email(name, email, message):
        calls.append((name, email, message))
        return True, "ok"

    monkeypatch.setattr(contact_module, "send_email", fake_send_email)
    result = contact_content(mock_page)
    fields = _fields(result)
    fields["Nome"].value = "Gustavo"
    fields["Email"].value = "gustavo@gmf-tech.com"
    fields["Mensagem"].value = "Quero automatizar atendimento com IA"

    _submit_button(result).on_click(None)

    assert calls == [("Gustavo", "gustavo@gmf-tech.com", "Quero automatizar atendimento com IA")]
    assert mock_page.snack_bar.bgcolor == COLORS["success"]
    assert "sucesso" in mock_page.snack_bar.content.value
    assert fields["Nome"].value == ""
    assert fields["Email"].value == ""
    assert fields["Mensagem"].value == ""


def test_contact_field_widths_are_responsive(mobile_page, tablet_page, desktop_page):
    mobile_fields = _fields(contact_content(mobile_page))
    tablet_fields = _fields(contact_content(tablet_page))
    desktop_fields = _fields(contact_content(desktop_page))

    assert mobile_fields["Nome"].width is None
    assert tablet_fields["Nome"].width == 440
    assert desktop_fields["Nome"].width == 440
