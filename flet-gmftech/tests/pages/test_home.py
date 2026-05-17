"""
Unit tests for home page module.
Tests home_content function with different viewport sizes and button navigation handlers.
"""

import pytest
import flet as ft
from pages.home import home_content
from theme import COLORS


class TestHomeContent:
    """Tests for home_content function"""
    
    def test_home_content_returns_valid_container(self, mock_page):
        """Test that home_content() returns a valid Container"""
        result = home_content(mock_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        assert result.content is not None
        assert isinstance(result.content, ft.Container)
    
    def test_home_content_has_correct_structure(self, mock_page):
        """Test that home_content has the correct nested structure"""
        result = home_content(mock_page)
        
        # Outer container
        assert isinstance(result, ft.Container)
        
        # Inner container
        inner_container = result.content
        assert isinstance(inner_container, ft.Container)
        assert inner_container.expand is True
        
        # Column
        column = inner_container.content
        assert isinstance(column, ft.Column)
        assert column.horizontal_alignment == "center"
        assert column.alignment == "center"
    
    def test_home_content_has_title_and_subtitle(self, mock_page):
        """Test that home_content contains title and subtitle texts"""
        result = home_content(mock_page)
        
        column = result.content.content
        controls = column.controls
        
        # Should have at least 3 controls: title, subtitle, button container
        assert len(controls) >= 3
        
        # First control should be title
        title = controls[0]
        assert isinstance(title, ft.Text)
        assert "GMF-tech" in title.value
        assert title.weight == "bold"
        assert title.color == COLORS["text_primary"]
        
        # Second control should be subtitle
        subtitle = controls[1]
        assert isinstance(subtitle, ft.Text)
        assert "soluções de TI" in subtitle.value
        assert subtitle.color == COLORS["text_secondary"]
    
    def test_home_content_has_three_buttons(self, mock_page):
        """Test that home_content contains three navigation buttons"""
        result = home_content(mock_page)
        
        column = result.content.content
        button_container = column.controls[2]
        
        assert isinstance(button_container, ft.Container)
        
        button_row = button_container.content
        assert isinstance(button_row, ft.Row)
        assert button_row.alignment == "center"
        assert button_row.wrap is True
        
        buttons = button_row.controls
        assert len(buttons) == 3
        
        # Check all are Flet 0.85 buttons
        for button in buttons:
            assert isinstance(button, ft.Button)


class TestHomeContentMobile:
    """Tests for home_content with mobile viewport"""
    
    def test_home_content_with_mobile_page(self, mobile_page):
        """Test home_content() with mobile_page fixture (400px width)"""
        result = home_content(mobile_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        
        # Verify responsive calculations were applied
        column = result.content.content
        title = column.controls[0]
        subtitle = column.controls[1]
        
        # Mobile should have smaller font sizes (scaled by 0.85)
        # Base title: 48 * 0.85 = 40.8 -> 40
        assert title.size == 40
        
        # Base subtitle: 32 * 0.85 = 27.2 -> 27
        assert subtitle.size == 27
    
    def test_home_content_mobile_has_responsive_spacing(self, mobile_page):
        """Test that mobile layout has appropriate spacing"""
        result = home_content(mobile_page)
        
        column = result.content.content
        
        # Mobile spacing should be scaled by 0.75
        # Base column_spacing: 20 * 0.75 = 15
        assert column.spacing == 15
        
        # Button container margin
        button_container = column.controls[2]
        # Base top_margin: 40 * 0.75 = 30
        assert button_container.margin.top == 30
    
    def test_home_content_mobile_buttons_wrap(self, mobile_page):
        """Test that buttons wrap properly on mobile"""
        result = home_content(mobile_page)
        
        column = result.content.content
        button_container = column.controls[2]
        button_row = button_container.content
        
        # Verify wrap is enabled for mobile
        assert button_row.wrap is True


class TestHomeContentTablet:
    """Tests for home_content with tablet viewport"""
    
    def test_home_content_with_tablet_page(self, tablet_page):
        """Test home_content() with tablet_page fixture (768px width)"""
        result = home_content(tablet_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        
        # Verify responsive calculations for tablet
        column = result.content.content
        title = column.controls[0]
        subtitle = column.controls[1]
        
        # Tablet should have medium font sizes (scaled by 0.95)
        # Base title: 48 * 0.95 = 45.6 -> 45
        assert title.size == 45
        
        # Base subtitle: 32 * 0.95 = 30.4 -> 30
        assert subtitle.size == 30
    
    def test_home_content_tablet_has_responsive_spacing(self, tablet_page):
        """Test that tablet layout has appropriate spacing"""
        result = home_content(tablet_page)
        
        column = result.content.content
        
        # Tablet spacing should be scaled by 0.9
        # Base column_spacing: 20 * 0.9 = 18
        assert column.spacing == 18
        
        # Button container margin
        button_container = column.controls[2]
        # Base top_margin: 40 * 0.9 = 36
        assert button_container.margin.top == 36


class TestHomeContentDesktop:
    """Tests for home_content with desktop viewport"""
    
    def test_home_content_with_desktop_page(self, desktop_page):
        """Test home_content() with desktop_page fixture (1920px width)"""
        result = home_content(desktop_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        
        # Verify responsive calculations for desktop
        column = result.content.content
        title = column.controls[0]
        subtitle = column.controls[1]
        
        # Desktop should have full font sizes (scaled by 1.0)
        # Base title: 48 * 1.0 = 48
        assert title.size == 48
        
        # Base subtitle: 32 * 1.0 = 32
        assert subtitle.size == 32
    
    def test_home_content_desktop_has_responsive_spacing(self, desktop_page):
        """Test that desktop layout has full spacing"""
        result = home_content(desktop_page)
        
        column = result.content.content
        
        # Desktop spacing should be scaled by 1.0
        # Base column_spacing: 20 * 1.0 = 20
        assert column.spacing == 20
        
        # Button container margin
        button_container = column.controls[2]
        # Base top_margin: 40 * 1.0 = 40
        assert button_container.margin.top == 40


class TestButtonNavigationHandlers:
    """Tests for button navigation handlers"""
    
    def test_portfolio_button_navigation(self, mock_page):
        """Test that 'Ver Portfólio' button navigates to /portfolio"""
        result = home_content(mock_page)
        
        column = result.content.content
        button_container = column.controls[2]
        button_row = button_container.content
        buttons = button_row.controls
        
        # First button should be "Ver Portfólio"
        portfolio_button = buttons[0]
        assert "Portfólio" in portfolio_button.content
        
        # Trigger the click handler
        portfolio_button.on_click(None)
        
        # Verify page.push_route was called with /portfolio
        mock_page.push_route.assert_called_once_with("/portfolio")
    
    def test_services_button_navigation(self, mock_page):
        """Test that 'Nossos Serviços' button navigates to /services"""
        result = home_content(mock_page)
        
        column = result.content.content
        button_container = column.controls[2]
        button_row = button_container.content
        buttons = button_row.controls
        
        # Second button should be "Nossos Serviços"
        services_button = buttons[1]
        assert "Serviços" in services_button.content
        
        # Trigger the click handler
        services_button.on_click(None)
        
        # Verify page.push_route was called with /services
        mock_page.push_route.assert_called_once_with("/services")
    
    def test_contact_button_navigation(self, mock_page):
        """Test that 'Entre em Contato' button navigates to /contact"""
        result = home_content(mock_page)
        
        column = result.content.content
        button_container = column.controls[2]
        button_row = button_container.content
        buttons = button_row.controls
        
        # Third button should be "Entre em Contato"
        contact_button = buttons[2]
        assert "Contato" in contact_button.content
        
        # Trigger the click handler
        contact_button.on_click(None)
        
        # Verify page.push_route was called with /contact
        mock_page.push_route.assert_called_once_with("/contact")
    
    def test_all_buttons_have_correct_colors(self, mock_page):
        """Test that buttons have correct background colors"""
        result = home_content(mock_page)
        
        column = result.content.content
        button_container = column.controls[2]
        button_row = button_container.content
        buttons = button_row.controls
        
        # Portfolio button - secondary color
        assert buttons[0].style.bgcolor == COLORS["secondary"]
        
        # Services button - primary color
        assert buttons[1].style.bgcolor == COLORS["primary"]
        
        # Contact button - accent color
        assert buttons[2].style.bgcolor == COLORS["accent"]
    
    def test_all_buttons_have_white_text(self, mock_page):
        """Test that all buttons have white text color"""
        result = home_content(mock_page)
        
        column = result.content.content
        button_container = column.controls[2]
        button_row = button_container.content
        buttons = button_row.controls
        
        for button in buttons:
            assert button.style.color == ft.Colors.WHITE
    
    def test_buttons_have_responsive_padding(self, mobile_page, desktop_page):
        """Test that buttons have responsive padding based on viewport"""
        # Mobile buttons
        mobile_result = home_content(mobile_page)
        mobile_column = mobile_result.content.content
        mobile_button_row = mobile_column.controls[2].content
        mobile_button = mobile_button_row.controls[0]
        
        # Mobile padding: 30 * 0.75 = 22.5 -> 22 (horizontal)
        # Mobile padding: 15 * 0.75 = 11.25 -> 11 (vertical)
        mobile_padding = mobile_button.style.padding
        assert mobile_padding.left == 22
        assert mobile_padding.right == 22
        assert mobile_padding.top == 11
        assert mobile_padding.bottom == 11
        
        # Desktop buttons
        desktop_result = home_content(desktop_page)
        desktop_column = desktop_result.content.content
        desktop_button_row = desktop_column.controls[2].content
        desktop_button = desktop_button_row.controls[0]
        
        # Desktop padding: 30 * 1.0 = 30 (horizontal)
        # Desktop padding: 15 * 1.0 = 15 (vertical)
        desktop_padding = desktop_button.style.padding
        assert desktop_padding.left == 30
        assert desktop_padding.right == 30
        assert desktop_padding.top == 15
        assert desktop_padding.bottom == 15
