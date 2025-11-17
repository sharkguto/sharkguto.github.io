"""
Unit tests for portfolio page module.
Tests portfolio_content function with different viewport sizes and responsive image dimensions.
"""

import pytest
import flet as ft
from pages.portfolio import portfolio_content
from theme import COLORS


class TestPortfolioContent:
    """Tests for portfolio_content function"""
    
    def test_portfolio_content_returns_valid_container(self, mock_page):
        """Test that portfolio_content() returns a valid Container"""
        result = portfolio_content(mock_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        assert result.content is not None
        assert isinstance(result.content, ft.Column)
    
    def test_portfolio_content_has_correct_structure(self, mock_page):
        """Test that portfolio_content has the correct nested structure"""
        result = portfolio_content(mock_page)
        
        # Outer container
        assert isinstance(result, ft.Container)
        assert result.expand is True
        assert result.padding is not None
        
        # Column
        column = result.content
        assert isinstance(column, ft.Column)
        assert column.expand is True
        assert column.alignment == "start"
        assert column.scroll == ft.ScrollMode.AUTO
    
    def test_portfolio_content_has_title_and_subtitle(self, mock_page):
        """Test that portfolio_content contains title and subtitle texts"""
        result = portfolio_content(mock_page)
        
        column = result.content
        controls = column.controls
        
        # Should have at least 3 controls: title, subtitle, ResponsiveRow
        assert len(controls) >= 3
        
        # First control should be title
        title = controls[0]
        assert isinstance(title, ft.Text)
        assert title.value == "Nossos Projetos"
        assert title.weight == "bold"
        assert title.color == COLORS["text_primary"]
        assert title.text_align == "center"
        
        # Second control should be subtitle
        subtitle = controls[1]
        assert isinstance(subtitle, ft.Text)
        assert "casos de sucesso" in subtitle.value
        assert subtitle.color == COLORS["text_secondary"]
        assert subtitle.text_align == "center"
    
    def test_portfolio_content_has_responsive_row(self, mock_page):
        """Test that portfolio_content contains ResponsiveRow with projects"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        assert isinstance(responsive_row, ft.ResponsiveRow)
        assert responsive_row.alignment == "center"


class TestProjectsList:
    """Tests for projects list"""
    
    def test_projects_list_has_3_items(self, mock_page):
        """Test that projects list has exactly 3 items"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # ResponsiveRow contains Container wrappers for each project
        assert len(responsive_row.controls) == 3
    
    def test_all_projects_have_required_fields(self, mock_page):
        """Test that all projects have title, description, image, and technologies"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        for project_container in responsive_row.controls:
            assert isinstance(project_container, ft.Container)
            
            # Get the project card
            project_card = project_container.content
            assert isinstance(project_card, ft.Container)
            
            # Get the card column
            card_column = project_card.content
            assert isinstance(card_column, ft.Column)
            
            # Should have 4 controls: image container, title, description, technologies
            assert len(card_column.controls) == 4


class TestCreateProjectCard:
    """Tests for create_project_card function (indirectly through portfolio_content)"""
    
    def test_create_project_card_returns_valid_container(self, mock_page):
        """Test that create_project_card() returns a valid Container with correct structure"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project card
        project_container = responsive_row.controls[0]
        card = project_container.content
        
        assert isinstance(card, ft.Container)
        assert card.bgcolor == ft.colors.WHITE
        assert card.border_radius is not None
        assert card.shadow is not None
        assert card.padding is not None
        assert card.margin is not None
    
    def test_create_project_card_has_image(self, mock_page):
        """Test that project cards have an image with correct properties"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project card
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # First control should be image container
        image_container = card_column.controls[0]
        assert isinstance(image_container, ft.Container)
        assert image_container.margin is not None
        
        # Image
        image = image_container.content
        assert isinstance(image, ft.Image)
        assert image.fit == ft.ImageFit.COVER
        assert image.border_radius is not None
        assert "/images/" in image.src
    
    def test_create_project_card_has_title(self, mock_page):
        """Test that project cards have a title"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project card
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Second control should be title
        title = card_column.controls[1]
        assert isinstance(title, ft.Text)
        assert title.weight == "bold"
        assert title.color == COLORS["text_primary"]
        assert len(title.value) > 0
    
    def test_create_project_card_has_description(self, mock_page):
        """Test that project cards have a description"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project card
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Third control should be description
        description = card_column.controls[2]
        assert isinstance(description, ft.Text)
        assert description.color == COLORS["text_secondary"]
        assert description.text_align == "justify"
        assert len(description.value) > 0
    
    def test_create_project_card_has_technologies(self, mock_page):
        """Test that project cards have technology tags"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project card
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Fourth control should be technologies container
        tech_container = card_column.controls[3]
        assert isinstance(tech_container, ft.Container)
        assert tech_container.margin is not None
        
        # Technologies row
        tech_row = tech_container.content
        assert isinstance(tech_row, ft.Row)
        assert tech_row.wrap is True
        assert tech_row.alignment == ft.MainAxisAlignment.START
        
        # Should have at least one technology tag
        assert len(tech_row.controls) > 0
        
        # Check first technology tag
        first_tag = tech_row.controls[0]
        assert isinstance(first_tag, ft.Container)
        assert first_tag.bgcolor == COLORS["surface"]
        assert first_tag.border_radius is not None
        assert first_tag.padding is not None
        
        # Tag text
        tag_text = first_tag.content
        assert isinstance(tag_text, ft.Text)
        assert tag_text.color == COLORS["primary"]
        assert tag_text.weight == "w500"


class TestImageDimensionsMobile:
    """Tests for image dimensions on mobile viewport"""
    
    def test_image_dimensions_on_mobile(self, mobile_page):
        """Test that images have correct dimensions on mobile (viewport_width - 80px)"""
        result = portfolio_content(mobile_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project card
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Get image
        image_container = card_column.controls[0]
        image = image_container.content
        
        # Mobile: width = 400 - 80 = 320, height = 200
        assert image.width == 320
        assert image.height == 200
    
    def test_mobile_has_responsive_font_sizes(self, mobile_page):
        """Test that mobile layout has scaled font sizes"""
        result = portfolio_content(mobile_page)
        
        column = result.content
        
        # Title font size (32 * 0.85 = 27.2 -> 27)
        title = column.controls[0]
        assert title.size == 27
        
        # Subtitle font size (16 * 0.85 = 13.6 -> 13)
        subtitle = column.controls[1]
        assert subtitle.size == 13
        
        # Get first project card
        responsive_row = column.controls[2]
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Card title size (24 * 0.85 = 20.4 -> 20)
        card_title = card_column.controls[1]
        assert card_title.size == 20
        
        # Card description size (16 * 0.85 = 13.6 -> 13)
        card_desc = card_column.controls[2]
        assert card_desc.size == 13
        
        # Technology tag size (14 * 0.85 = 11.9 -> 11)
        tech_container = card_column.controls[3]
        tech_row = tech_container.content
        first_tag = tech_row.controls[0]
        tag_text = first_tag.content
        assert tag_text.size == 11
    
    def test_mobile_has_responsive_padding(self, mobile_page):
        """Test that mobile layout has scaled padding"""
        result = portfolio_content(mobile_page)
        
        column = result.content
        responsive_row = column.controls[2]
        project_container = responsive_row.controls[0]
        card = project_container.content
        
        # Card padding (30 * 0.75 = 22.5 -> 22)
        # Padding is set using ft.padding.all() which returns an integer
        assert card.padding == 22


class TestImageDimensionsTablet:
    """Tests for image dimensions on tablet viewport"""
    
    def test_image_dimensions_on_tablet(self, tablet_page):
        """Test that images have correct dimensions on tablet (350px x 220px)"""
        result = portfolio_content(tablet_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project card
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Get image
        image_container = card_column.controls[0]
        image = image_container.content
        
        # Tablet: width = 350, height = 220
        assert image.width == 350
        assert image.height == 220
    
    def test_tablet_has_responsive_font_sizes(self, tablet_page):
        """Test that tablet layout has scaled font sizes"""
        result = portfolio_content(tablet_page)
        
        column = result.content
        
        # Title font size (32 * 0.95 = 30.4 -> 30)
        title = column.controls[0]
        assert title.size == 30
        
        # Subtitle font size (16 * 0.95 = 15.2 -> 15)
        subtitle = column.controls[1]
        assert subtitle.size == 15
        
        # Get first project card
        responsive_row = column.controls[2]
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Card title size (24 * 0.95 = 22.8 -> 22)
        card_title = card_column.controls[1]
        assert card_title.size == 22
        
        # Card description size (16 * 0.95 = 15.2 -> 15)
        card_desc = card_column.controls[2]
        assert card_desc.size == 15
        
        # Technology tag size (14 * 0.95 = 13.3 -> 13)
        tech_container = card_column.controls[3]
        tech_row = tech_container.content
        first_tag = tech_row.controls[0]
        tag_text = first_tag.content
        assert tag_text.size == 13


class TestImageDimensionsDesktop:
    """Tests for image dimensions on desktop viewport"""
    
    def test_image_dimensions_on_desktop(self, desktop_page):
        """Test that images have correct dimensions on desktop (400px x 250px)"""
        result = portfolio_content(desktop_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project card
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Get image
        image_container = card_column.controls[0]
        image = image_container.content
        
        # Desktop: width = 400, height = 250
        assert image.width == 400
        assert image.height == 250
    
    def test_desktop_has_full_font_sizes(self, desktop_page):
        """Test that desktop layout has full font sizes"""
        result = portfolio_content(desktop_page)
        
        column = result.content
        
        # Title font size (32 * 1.0 = 32)
        title = column.controls[0]
        assert title.size == 32
        
        # Subtitle font size (16 * 1.0 = 16)
        subtitle = column.controls[1]
        assert subtitle.size == 16
        
        # Get first project card
        responsive_row = column.controls[2]
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Card title size (24 * 1.0 = 24)
        card_title = card_column.controls[1]
        assert card_title.size == 24
        
        # Card description size (16 * 1.0 = 16)
        card_desc = card_column.controls[2]
        assert card_desc.size == 16
        
        # Technology tag size (14 * 1.0 = 14)
        tech_container = card_column.controls[3]
        tech_row = tech_container.content
        first_tag = tech_row.controls[0]
        tag_text = first_tag.content
        assert tag_text.size == 14
    
    def test_desktop_has_full_padding(self, desktop_page):
        """Test that desktop layout has full padding"""
        result = portfolio_content(desktop_page)
        
        column = result.content
        responsive_row = column.controls[2]
        project_container = responsive_row.controls[0]
        card = project_container.content
        
        # Card padding (30 * 1.0 = 30)
        # Padding is set using ft.padding.all() which returns an integer
        assert card.padding == 30


class TestResponsiveRowConfiguration:
    """Tests for ResponsiveRow configuration"""
    
    def test_responsive_row_col_configuration(self, mock_page):
        """Test that ResponsiveRow has correct col configuration for responsive layout"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project container
        project_container = responsive_row.controls[0]
        
        # Check col configuration
        # Mobile: 12/12 (full width), Tablet & Desktop: 6/12 (half width)
        assert project_container.col == {"sm": 12, "md": 6, "lg": 6}
    
    def test_responsive_row_has_correct_alignment(self, mock_page):
        """Test that ResponsiveRow has center alignment"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        assert responsive_row.alignment == "center"
    
    def test_all_project_containers_have_same_col_config(self, mock_page):
        """Test that all project containers have the same col configuration"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        expected_col = {"sm": 12, "md": 6, "lg": 6}
        
        for project_container in responsive_row.controls:
            assert project_container.col == expected_col
    
    def test_all_project_containers_have_padding(self, mock_page):
        """Test that all project containers have padding"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        for project_container in responsive_row.controls:
            assert isinstance(project_container, ft.Container)
            assert project_container.padding == 10


class TestProjectContent:
    """Tests for specific project content"""
    
    def test_first_project_is_velejar_facil(self, mock_page):
        """Test that first project is 'Velejar Fácil'"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get first project card
        project_container = responsive_row.controls[0]
        card = project_container.content
        card_column = card.content
        
        # Check title
        title = card_column.controls[1]
        assert "Velejar Fácil" in title.value
        
        # Check image path
        image_container = card_column.controls[0]
        image = image_container.content
        assert "velejar_facil" in image.src
    
    def test_second_project_is_monitoring_system(self, mock_page):
        """Test that second project is monitoring system"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get second project card
        project_container = responsive_row.controls[1]
        card = project_container.content
        card_column = card.content
        
        # Check title
        title = card_column.controls[1]
        assert "Monitoramento de Cotações" in title.value
        
        # Check image path
        image_container = card_column.controls[0]
        image = image_container.content
        assert "chart-project" in image.src
    
    def test_third_project_is_website(self, mock_page):
        """Test that third project is GMF-tech website"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        # Get third project card
        project_container = responsive_row.controls[2]
        card = project_container.content
        card_column = card.content
        
        # Check title
        title = card_column.controls[1]
        assert "Website Institucional GMF-tech" in title.value
        
        # Check image path
        image_container = card_column.controls[0]
        image = image_container.content
        assert "website-project" in image.src
    
    def test_all_projects_have_technologies(self, mock_page):
        """Test that all projects have technology tags"""
        result = portfolio_content(mock_page)
        
        column = result.content
        responsive_row = column.controls[2]
        
        for project_container in responsive_row.controls:
            card = project_container.content
            card_column = card.content
            
            # Get technologies container
            tech_container = card_column.controls[3]
            tech_row = tech_container.content
            
            # Should have at least one technology
            assert len(tech_row.controls) > 0
