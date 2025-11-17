"""
Unit tests for services page module.
Tests services_content function with different viewport sizes and grid layout responsiveness.
"""

import pytest
import flet as ft
from pages.services import services_content
from theme import COLORS


class TestServicesContent:
    """Tests for services_content function"""
    
    def test_services_content_returns_valid_container(self, mock_page):
        """Test that services_content() returns a valid Container"""
        result = services_content(mock_page)
        
        assert isinstance(result, ft.Container)
        assert result.content is not None
        assert isinstance(result.content, ft.Column)
    
    def test_services_content_has_correct_structure(self, mock_page):
        """Test that services_content has the correct nested structure"""
        result = services_content(mock_page)
        
        # Outer container
        assert isinstance(result, ft.Container)
        assert result.padding is not None
        
        # Column
        column = result.content
        assert isinstance(column, ft.Column)
        assert column.spacing == 15
        
        # Should have 4 main controls: services title, services grid, tech title, tech grid
        assert len(column.controls) == 4
    
    def test_services_content_has_services_title(self, mock_page):
        """Test that services_content contains 'Nossos Serviços' title"""
        result = services_content(mock_page)
        
        column = result.content
        title = column.controls[0]
        
        assert isinstance(title, ft.Text)
        assert title.value == "Nossos Serviços"
        assert title.weight == "bold"
        assert title.color == COLORS["text_primary"]
        assert title.text_align == "center"
    
    def test_services_content_has_technologies_title(self, mock_page):
        """Test that services_content contains 'Tecnologias' title"""
        result = services_content(mock_page)
        
        column = result.content
        tech_title_container = column.controls[2]
        
        assert isinstance(tech_title_container, ft.Container)
        tech_title = tech_title_container.content
        assert isinstance(tech_title, ft.Text)
        assert tech_title.value == "Tecnologias"
        assert tech_title.weight == "bold"
        assert tech_title.color == COLORS["text_primary"]
        assert tech_title.text_align == "center"
    
    def test_services_list_has_8_items(self, mock_page):
        """Test that services list has exactly 8 items"""
        result = services_content(mock_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        assert isinstance(services_grid, ft.GridView)
        # GridView controls contains the list of service cards
        assert len(services_grid.controls) == 8
    
    def test_technologies_list_has_8_items(self, mock_page):
        """Test that technologies list has exactly 8 items"""
        result = services_content(mock_page)
        
        column = result.content
        tech_grid = column.controls[3]
        
        assert isinstance(tech_grid, ft.GridView)
        # GridView controls contains the list of technology cards
        assert len(tech_grid.controls) == 8


class TestCreateCard:
    """Tests for create_card function (indirectly through services_content)"""
    
    def test_create_card_returns_valid_container(self, mock_page):
        """Test that create_card() returns a valid Container with correct structure"""
        result = services_content(mock_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        # Get first card
        card = services_grid.controls[0]
        
        assert isinstance(card, ft.Container)
        assert card.bgcolor == COLORS["surface"]
        assert card.border_radius is not None
        assert card.shadow is not None
        assert card.padding is not None
    
    def test_create_card_has_icon_title_description(self, mock_page):
        """Test that cards have icon, title, and description"""
        result = services_content(mock_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        # Get first card
        card = services_grid.controls[0]
        card_column = card.content
        
        assert isinstance(card_column, ft.Column)
        assert card_column.horizontal_alignment == "center"
        assert card_column.alignment == "center"
        
        # Should have 3 containers: icon, title, description
        assert len(card_column.controls) == 3
        
        # Icon container
        icon_container = card_column.controls[0]
        assert isinstance(icon_container, ft.Container)
        icon = icon_container.content
        assert isinstance(icon, ft.Icon)
        assert icon.color == COLORS["primary"]
        
        # Title container
        title_container = card_column.controls[1]
        assert isinstance(title_container, ft.Container)
        title = title_container.content
        assert isinstance(title, ft.Text)
        assert title.weight == "bold"
        assert title.color == COLORS["text_primary"]
        assert title.text_align == "center"
        
        # Description container
        desc_container = card_column.controls[2]
        assert isinstance(desc_container, ft.Container)
        desc = desc_container.content
        assert isinstance(desc, ft.Text)
        assert desc.color == COLORS["text_secondary"]
        assert desc.text_align == "center"
    
    def test_create_card_with_different_parameters(self, mock_page):
        """Test that different cards have different content"""
        result = services_content(mock_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        # Get first and second cards
        card1 = services_grid.controls[0]
        card2 = services_grid.controls[1]
        
        # Extract titles
        title1 = card1.content.controls[1].content.value
        title2 = card2.content.controls[1].content.value
        
        # Titles should be different
        assert title1 != title2
        assert "Levantamento de Requisitos" in title1
        assert "Arquitetura de Software" in title2


class TestServicesGridMobile:
    """Tests for services grid on mobile viewport"""
    
    def test_gridview_runs_count_on_mobile_should_be_1(self, mobile_page):
        """Test that GridView runs_count is 1 on mobile (400px width)"""
        result = services_content(mobile_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        assert isinstance(services_grid, ft.GridView)
        # Mobile should show 1 card per row
        assert services_grid.runs_count == 1
    
    def test_mobile_has_responsive_font_sizes(self, mobile_page):
        """Test that mobile layout has scaled font sizes"""
        result = services_content(mobile_page)
        
        column = result.content
        
        # Title font size (24 * 0.85 = 20.4 -> 20)
        title = column.controls[0]
        assert title.size == 20
        
        # Card icon size (40 * 0.85 = 34)
        services_grid = column.controls[1]
        card = services_grid.controls[0]
        icon = card.content.controls[0].content
        assert icon.size == 34
        
        # Card title size (20 * 0.85 = 17)
        card_title = card.content.controls[1].content
        assert card_title.size == 17
        
        # Card description size (16 * 0.85 = 13.6 -> 13)
        card_desc = card.content.controls[2].content
        assert card_desc.size == 13
    
    def test_mobile_has_responsive_padding(self, mobile_page):
        """Test that mobile layout has scaled padding"""
        result = services_content(mobile_page)
        
        column = result.content
        services_grid = column.controls[1]
        card = services_grid.controls[0]
        
        # Card padding (20 * 0.75 = 15)
        assert card.padding.left == 15
        assert card.padding.right == 15
        assert card.padding.top == 15
        assert card.padding.bottom == 15


class TestServicesGridTablet:
    """Tests for services grid on tablet viewport"""
    
    def test_gridview_runs_count_on_tablet_should_be_2(self, tablet_page):
        """Test that GridView runs_count is 2 on tablet (768px width)"""
        result = services_content(tablet_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        assert isinstance(services_grid, ft.GridView)
        # Tablet should show 2 cards per row
        assert services_grid.runs_count == 2
    
    def test_tablet_has_responsive_font_sizes(self, tablet_page):
        """Test that tablet layout has scaled font sizes"""
        result = services_content(tablet_page)
        
        column = result.content
        
        # Title font size (24 * 0.95 = 22.8 -> 22)
        title = column.controls[0]
        assert title.size == 22
        
        # Card icon size (40 * 0.95 = 38)
        services_grid = column.controls[1]
        card = services_grid.controls[0]
        icon = card.content.controls[0].content
        assert icon.size == 38
        
        # Card title size (20 * 0.95 = 19)
        card_title = card.content.controls[1].content
        assert card_title.size == 19
        
        # Card description size (16 * 0.95 = 15.2 -> 15)
        card_desc = card.content.controls[2].content
        assert card_desc.size == 15
    
    def test_tablet_has_responsive_padding(self, tablet_page):
        """Test that tablet layout has scaled padding"""
        result = services_content(tablet_page)
        
        column = result.content
        services_grid = column.controls[1]
        card = services_grid.controls[0]
        
        # Card padding (20 * 0.9 = 18)
        assert card.padding.left == 18
        assert card.padding.right == 18
        assert card.padding.top == 18
        assert card.padding.bottom == 18


class TestServicesGridDesktop:
    """Tests for services grid on desktop viewport"""
    
    def test_gridview_runs_count_on_desktop_should_be_2(self, desktop_page):
        """Test that GridView runs_count is 2 on desktop (1920px width) for services"""
        result = services_content(desktop_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        assert isinstance(services_grid, ft.GridView)
        # Desktop should show 2 cards per row for services
        assert services_grid.runs_count == 2
    
    def test_desktop_has_full_font_sizes(self, desktop_page):
        """Test that desktop layout has full font sizes"""
        result = services_content(desktop_page)
        
        column = result.content
        
        # Title font size (24 * 1.0 = 24)
        title = column.controls[0]
        assert title.size == 24
        
        # Card icon size (40 * 1.0 = 40)
        services_grid = column.controls[1]
        card = services_grid.controls[0]
        icon = card.content.controls[0].content
        assert icon.size == 40
        
        # Card title size (20 * 1.0 = 20)
        card_title = card.content.controls[1].content
        assert card_title.size == 20
        
        # Card description size (16 * 1.0 = 16)
        card_desc = card.content.controls[2].content
        assert card_desc.size == 16
    
    def test_desktop_has_full_padding(self, desktop_page):
        """Test that desktop layout has full padding"""
        result = services_content(desktop_page)
        
        column = result.content
        services_grid = column.controls[1]
        card = services_grid.controls[0]
        
        # Card padding (20 * 1.0 = 20)
        assert card.padding.left == 20
        assert card.padding.right == 20
        assert card.padding.top == 20
        assert card.padding.bottom == 20


class TestTechnologiesGrid:
    """Tests for technologies grid responsiveness"""
    
    def test_technologies_grid_mobile_runs_count(self, mobile_page):
        """Test that technologies GridView has 1 column on mobile"""
        result = services_content(mobile_page)
        
        column = result.content
        tech_grid = column.controls[3]
        
        assert isinstance(tech_grid, ft.GridView)
        # Mobile should show 1 card per row
        assert tech_grid.runs_count == 1
    
    def test_technologies_grid_tablet_runs_count(self, tablet_page):
        """Test that technologies GridView has 2 columns on tablet"""
        result = services_content(tablet_page)
        
        column = result.content
        tech_grid = column.controls[3]
        
        assert isinstance(tech_grid, ft.GridView)
        # Tablet should show 2 cards per row
        assert tech_grid.runs_count == 2
    
    def test_technologies_grid_desktop_runs_count(self, desktop_page):
        """Test that technologies GridView has 3 columns on desktop"""
        result = services_content(desktop_page)
        
        column = result.content
        tech_grid = column.controls[3]
        
        assert isinstance(tech_grid, ft.GridView)
        # Desktop should show 3 cards per row
        assert tech_grid.runs_count == 3
    
    def test_technologies_grid_has_correct_spacing(self, mock_page):
        """Test that technologies grid has correct spacing"""
        result = services_content(mock_page)
        
        column = result.content
        tech_grid = column.controls[3]
        
        # Grid spacing should be responsive (8 * 1.0 = 8 for desktop-like mock_page)
        assert tech_grid.spacing == 8
        assert tech_grid.run_spacing == 8
    
    def test_technologies_grid_has_correct_padding(self, mock_page):
        """Test that technologies grid has correct padding"""
        result = services_content(mock_page)
        
        column = result.content
        tech_grid = column.controls[3]
        
        # Grid padding
        assert tech_grid.padding.left == 10
        assert tech_grid.padding.right == 10
        assert tech_grid.padding.top == 8
        assert tech_grid.padding.bottom == 8


class TestServicesGridProperties:
    """Tests for services grid properties"""
    
    def test_services_grid_has_correct_max_extent(self, mock_page):
        """Test that services grid has correct max_extent"""
        result = services_content(mock_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        assert services_grid.max_extent == 400
    
    def test_services_grid_has_correct_spacing(self, mock_page):
        """Test that services grid has correct spacing"""
        result = services_content(mock_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        # Grid spacing should be responsive (8 * 1.0 = 8 for desktop-like mock_page)
        assert services_grid.spacing == 8
        assert services_grid.run_spacing == 8
    
    def test_services_grid_has_correct_padding(self, mock_page):
        """Test that services grid has correct padding"""
        result = services_content(mock_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        # Grid padding
        assert services_grid.padding.left == 10
        assert services_grid.padding.right == 10
        assert services_grid.padding.top == 8
        assert services_grid.padding.bottom == 8
    
    def test_services_grid_child_aspect_ratio_is_none(self, mock_page):
        """Test that services grid has child_aspect_ratio set to None for auto height"""
        result = services_content(mock_page)
        
        column = result.content
        services_grid = column.controls[1]
        
        assert services_grid.child_aspect_ratio is None
