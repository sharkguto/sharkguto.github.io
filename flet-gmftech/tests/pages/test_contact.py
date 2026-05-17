"""
Unit tests for contact page module.
Tests contact_content function, form validation, and responsive field widths.
"""

import pytest
import flet as ft
from pages.contact import contact_content
from theme import COLORS
from utils.responsive import Breakpoint


class TestContactContent:
    """Tests for contact_content function"""
    
    def test_contact_content_returns_valid_container(self, mock_page):
        """Test that contact_content() returns a valid Container"""
        result = contact_content(mock_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        assert result.content is not None
        assert isinstance(result.content, ft.Container)
    
    def test_contact_content_has_correct_structure(self, mock_page):
        """Test that contact_content has the correct nested structure"""
        result = contact_content(mock_page)
        
        # Outer container
        assert isinstance(result, ft.Container)
        assert result.expand is True
        
        # Inner container
        inner_container = result.content
        assert isinstance(inner_container, ft.Container)
        assert inner_container.expand is True
        
        # Column
        column = inner_container.content
        assert isinstance(column, ft.Column)
        assert column.horizontal_alignment == "center"
        assert column.alignment == "center"
    
    def test_contact_content_has_title(self, mock_page):
        """Test that contact_content contains title text"""
        result = contact_content(mock_page)
        
        column = result.content.content
        controls = column.controls
        
        # Should have at least 2 controls: title and form container
        assert len(controls) >= 2
        
        # First control should be title
        title = controls[0]
        assert isinstance(title, ft.Text)
        assert "Entre em Contato" in title.value
        assert title.weight == "bold"
        assert title.color == COLORS["text_primary"]
    
    def test_contact_content_has_form_container(self, mock_page):
        """Test that contact_content contains form container with fields"""
        result = contact_content(mock_page)
        
        column = result.content.content
        form_container = column.controls[1]
        
        assert isinstance(form_container, ft.Container)
        assert form_container.bgcolor == COLORS["surface"]
        assert form_container.border_radius.top_left == 15
        
        # Form column
        form_column = form_container.content
        assert isinstance(form_column, ft.Column)
        assert form_column.horizontal_alignment == "center"
    
    def test_contact_content_has_three_text_fields(self, mock_page):
        """Test that contact_content contains name, email, and message fields"""
        result = contact_content(mock_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        form_controls = form_column.controls
        
        # Should have 4 controls: name, email, message, button container
        assert len(form_controls) == 4
        
        # Name field
        name_field = form_controls[0]
        assert isinstance(name_field, ft.TextField)
        assert name_field.label == "Nome"
        assert name_field.border_color == COLORS["primary"]
        
        # Email field
        email_field = form_controls[1]
        assert isinstance(email_field, ft.TextField)
        assert email_field.label == "Email"
        assert email_field.border_color == COLORS["primary"]
        
        # Message field
        message_field = form_controls[2]
        assert isinstance(message_field, ft.TextField)
        assert message_field.label == "Mensagem"
        assert message_field.multiline is True
        assert message_field.border_color == COLORS["primary"]
    
    def test_contact_content_has_submit_button(self, mock_page):
        """Test that contact_content contains submit button"""
        result = contact_content(mock_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        button_container = form_column.controls[3]
        
        assert isinstance(button_container, ft.Container)
        
        button = button_container.content
        assert isinstance(button, ft.Button)
        assert "Enviar" in button.content
        assert button.on_click is not None


class TestHandleSubmitValidation:
    """Tests for handle_submit validation logic"""
    
    def test_handle_submit_with_empty_fields_shows_error(self, mock_page):
        """Test that handle_submit() with empty fields shows error SnackBar"""
        result = contact_content(mock_page)
        
        # Get form fields and button
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        button_container = form_column.controls[3]
        button = button_container.content
        
        # Leave all fields empty
        name_field.value = ""
        email_field.value = ""
        message_field.value = ""
        
        # Trigger submit
        button.on_click(None)
        
        # Verify error SnackBar was set
        assert mock_page.snack_bar is not None
        assert isinstance(mock_page.snack_bar, ft.SnackBar)
        assert mock_page.snack_bar.bgcolor == COLORS["error"]
        assert "preencha todos os campos" in mock_page.snack_bar.content.value
        assert mock_page.snack_bar.open is True
        
        # Verify page.update was called
        mock_page.update.assert_called()
    
    def test_handle_submit_with_missing_name_shows_error(self, mock_page):
        """Test that handle_submit() with missing name shows error"""
        result = contact_content(mock_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        button_container = form_column.controls[3]
        button = button_container.content
        
        # Only name is empty
        name_field.value = ""
        email_field.value = "test@example.com"
        message_field.value = "Test message"
        
        # Trigger submit
        button.on_click(None)
        
        # Verify error SnackBar
        assert mock_page.snack_bar.bgcolor == COLORS["error"]
        assert mock_page.snack_bar.open is True
    
    def test_handle_submit_with_missing_email_shows_error(self, mock_page):
        """Test that handle_submit() with missing email shows error"""
        result = contact_content(mock_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        button_container = form_column.controls[3]
        button = button_container.content
        
        # Only email is empty
        name_field.value = "Test User"
        email_field.value = ""
        message_field.value = "Test message"
        
        # Trigger submit
        button.on_click(None)
        
        # Verify error SnackBar
        assert mock_page.snack_bar.bgcolor == COLORS["error"]
        assert mock_page.snack_bar.open is True
    
    def test_handle_submit_with_missing_message_shows_error(self, mock_page):
        """Test that handle_submit() with missing message shows error"""
        result = contact_content(mock_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        button_container = form_column.controls[3]
        button = button_container.content
        
        # Only message is empty
        name_field.value = "Test User"
        email_field.value = "test@example.com"
        message_field.value = ""
        
        # Trigger submit
        button.on_click(None)
        
        # Verify error SnackBar
        assert mock_page.snack_bar.bgcolor == COLORS["error"]
        assert mock_page.snack_bar.open is True


class TestHandleSubmitSuccess:
    """Tests for handle_submit success logic"""
    
    def test_handle_submit_with_valid_data_shows_success(self, mock_page):
        """Test that handle_submit() with valid data shows success SnackBar"""
        result = contact_content(mock_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        button_container = form_column.controls[3]
        button = button_container.content
        
        # Fill all fields with valid data
        name_field.value = "Test User"
        email_field.value = "test@example.com"
        message_field.value = "This is a test message"
        
        # Trigger submit
        button.on_click(None)
        
        # Verify success SnackBar was set
        assert mock_page.snack_bar is not None
        assert isinstance(mock_page.snack_bar, ft.SnackBar)
        assert mock_page.snack_bar.bgcolor == COLORS["success"]
        assert "sucesso" in mock_page.snack_bar.content.value
        assert mock_page.snack_bar.open is True
        
        # Verify page.update was called
        mock_page.update.assert_called()
    
    def test_form_fields_cleared_after_successful_submit(self, mock_page):
        """Test that form fields are cleared after successful submit"""
        result = contact_content(mock_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        button_container = form_column.controls[3]
        button = button_container.content
        
        # Fill all fields with valid data
        name_field.value = "Test User"
        email_field.value = "test@example.com"
        message_field.value = "This is a test message"
        
        # Trigger submit
        button.on_click(None)
        
        # Verify all fields are cleared
        assert name_field.value == ""
        assert email_field.value == ""
        assert message_field.value == ""
    
    def test_page_updated_after_successful_submit(self, mock_page):
        """Test that page.update() is called after successful submit"""
        result = contact_content(mock_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        button_container = form_column.controls[3]
        button = button_container.content
        
        # Fill all fields
        name_field.value = "Test User"
        email_field.value = "test@example.com"
        message_field.value = "Test message"
        
        # Reset mock to count calls
        mock_page.update.reset_mock()
        
        # Trigger submit
        button.on_click(None)
        
        # Verify page.update was called
        assert mock_page.update.call_count >= 1


class TestResponsiveFieldWidths:
    """Tests for responsive field widths on different breakpoints"""
    
    def test_field_widths_on_mobile(self, mobile_page):
        """Test that form fields have 100% width (None) on mobile"""
        result = contact_content(mobile_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        
        # Mobile fields should have width=None (100%)
        assert name_field.width is None
        assert email_field.width is None
        assert message_field.width is None
    
    def test_field_widths_on_tablet(self, tablet_page):
        """Test that form fields have fixed width on tablet"""
        result = contact_content(tablet_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        
        # Tablet fields should have width=400
        assert name_field.width == 400
        assert email_field.width == 400
        assert message_field.width == 400
    
    def test_field_widths_on_desktop(self, desktop_page):
        """Test that form fields have fixed width on desktop"""
        result = contact_content(desktop_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        name_field = form_column.controls[0]
        email_field = form_column.controls[1]
        message_field = form_column.controls[2]
        
        # Desktop fields should have width=400
        assert name_field.width == 400
        assert email_field.width == 400
        assert message_field.width == 400
    
    def test_form_container_width_on_mobile(self, mobile_page):
        """Test that form container has no fixed width on mobile"""
        result = contact_content(mobile_page)
        
        column = result.content.content
        form_container = column.controls[1]
        
        # Mobile form container should have width=None
        assert form_container.width is None
    
    def test_form_container_width_on_desktop(self, desktop_page):
        """Test that form container has fixed width on desktop"""
        result = contact_content(desktop_page)
        
        column = result.content.content
        form_container = column.controls[1]
        
        # Desktop form container should have width=500
        assert form_container.width == 500


class TestResponsiveStyling:
    """Tests for responsive styling and spacing"""
    
    def test_responsive_title_font_size_mobile(self, mobile_page):
        """Test that title has responsive font size on mobile"""
        result = contact_content(mobile_page)
        
        column = result.content.content
        title = column.controls[0]
        
        # Mobile title: 32 * 0.85 = 27.2 -> 27
        assert title.size == 27
    
    def test_responsive_title_font_size_tablet(self, tablet_page):
        """Test that title has responsive font size on tablet"""
        result = contact_content(tablet_page)
        
        column = result.content.content
        title = column.controls[0]
        
        # Tablet title: 32 * 0.95 = 30.4 -> 30
        assert title.size == 30
    
    def test_responsive_title_font_size_desktop(self, desktop_page):
        """Test that title has responsive font size on desktop"""
        result = contact_content(desktop_page)
        
        column = result.content.content
        title = column.controls[0]
        
        # Desktop title: 32 * 1.0 = 32
        assert title.size == 32
    
    def test_responsive_container_padding_mobile(self, mobile_page):
        """Test that form container has responsive padding on mobile"""
        result = contact_content(mobile_page)
        
        column = result.content.content
        form_container = column.controls[1]
        
        # Mobile padding: 30 * 0.75 = 22.5 -> 22
        assert form_container.padding == 22
    
    def test_responsive_container_padding_desktop(self, desktop_page):
        """Test that form container has responsive padding on desktop"""
        result = contact_content(desktop_page)
        
        column = result.content.content
        form_container = column.controls[1]
        
        # Desktop padding: 30 * 1.0 = 30
        assert form_container.padding == 30
    
    def test_responsive_field_spacing_mobile(self, mobile_page):
        """Test that form fields have responsive spacing on mobile"""
        result = contact_content(mobile_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        # Mobile field spacing: 15 * 0.75 = 11.25 -> 11
        assert form_column.spacing == 11
    
    def test_responsive_field_spacing_desktop(self, desktop_page):
        """Test that form fields have responsive spacing on desktop"""
        result = contact_content(desktop_page)
        
        column = result.content.content
        form_container = column.controls[1]
        form_column = form_container.content
        
        # Desktop field spacing: 15 * 1.0 = 15
        assert form_column.spacing == 15
    
    def test_responsive_section_spacing_mobile(self, mobile_page):
        """Test that sections have responsive spacing on mobile"""
        result = contact_content(mobile_page)
        
        column = result.content.content
        
        # Mobile section spacing: 20 * 0.75 = 15
        assert column.spacing == 15
    
    def test_responsive_section_spacing_desktop(self, desktop_page):
        """Test that sections have responsive spacing on desktop"""
        result = contact_content(desktop_page)
        
        column = result.content.content
        
        # Desktop section spacing: 20 * 1.0 = 20
        assert column.spacing == 20
