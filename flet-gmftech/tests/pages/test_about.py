"""
Unit tests for about page module.
Tests about_content function with different viewport sizes and responsive layout.
"""

import pytest
import flet as ft
from pages.about import about_content
from theme import COLORS
from utils.responsive import Breakpoint


class TestAboutContent:
    """Tests for about_content function"""
    
    def test_about_content_returns_valid_container(self, mock_page):
        """Test that about_content() returns a valid Container"""
        result = about_content(mock_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        assert result.content is not None
        assert isinstance(result.content, ft.Container)
    
    def test_about_content_has_correct_structure(self, mock_page):
        """Test that about_content has the correct nested structure"""
        result = about_content(mock_page)
        
        # Outer container
        assert isinstance(result, ft.Container)
        assert result.expand is True
        assert result.alignment == ft.Alignment.CENTER
        
        # Inner container
        inner_container = result.content
        assert isinstance(inner_container, ft.Container)
        assert inner_container.expand is True
        assert inner_container.alignment == ft.Alignment.CENTER
        
        # Column
        column = inner_container.content
        assert isinstance(column, ft.Column)
        assert column.horizontal_alignment == "center"
        assert column.alignment == "center"
    
    def test_about_content_has_main_title(self, mock_page):
        """Test that about_content contains main title"""
        result = about_content(mock_page)
        
        column = result.content.content
        controls = column.controls
        
        # Should have at least 2 controls: title and content container
        assert len(controls) >= 2
        
        # First control should be main title
        title = controls[0]
        assert isinstance(title, ft.Text)
        assert "Sobre Nós" in title.value
        assert title.weight == "bold"
        assert title.color == COLORS["text_primary"]
        assert title.text_align == "center"
    
    def test_about_content_has_content_container(self, mock_page):
        """Test that about_content has a styled content container"""
        result = about_content(mock_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        assert isinstance(content_container, ft.Container)
        assert content_container.bgcolor == COLORS["surface"]
        assert content_container.border_radius == ft.BorderRadius.all(15)
        assert content_container.shadow is not None
        assert content_container.alignment == ft.Alignment.CENTER
    
    def test_about_content_has_all_sections(self, mock_page):
        """Test that about_content contains all required sections"""
        result = about_content(mock_page)
        
        column = result.content.content
        content_container = column.controls[1]
        inner_column = content_container.content
        
        assert isinstance(inner_column, ft.Column)
        assert inner_column.horizontal_alignment == "center"
        assert inner_column.alignment == "center"
        
        # Should have 6 text elements: 3 section titles + 3 section contents
        text_controls = [c for c in inner_column.controls if isinstance(c, ft.Text)]
        assert len(text_controls) == 6
        
        # Check section titles
        section_titles = [c.value for c in text_controls if c.weight == "bold"]
        assert "Nossa História" in section_titles
        assert "Nossa Missão" in section_titles
        assert "Nossos Valores" in section_titles


class TestAboutContentMobile:
    """Tests for about_content with mobile viewport"""
    
    def test_about_content_with_mobile_page(self, mobile_page):
        """Test about_content() with mobile_page fixture (400px width)"""
        result = about_content(mobile_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        
        # Verify responsive calculations were applied
        column = result.content.content
        title = column.controls[0]
        
        # Mobile should have smaller font sizes (scaled by 0.85)
        # Base title: 32 * 0.85 = 27.2 -> 27
        assert title.size == 27
    
    def test_about_content_mobile_has_responsive_spacing(self, mobile_page):
        """Test that mobile layout has appropriate spacing"""
        result = about_content(mobile_page)
        
        column = result.content.content
        
        # Mobile spacing should be scaled by 0.75
        # Base section_spacing: 20 * 0.75 = 15
        assert column.spacing == 15
        
        # Content container
        content_container = column.controls[1]
        inner_column = content_container.content
        
        # Base inner_spacing: 15 * 0.75 = 11.25 -> 11
        assert inner_column.spacing == 11
    
    def test_about_content_mobile_has_responsive_padding(self, mobile_page):
        """Test that mobile layout has appropriate padding"""
        result = about_content(mobile_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        # Mobile padding: 30 * 0.75 = 22.5 -> 22
        assert content_container.padding == 22
    
    def test_about_content_mobile_container_max_width(self, mobile_page):
        """Test that mobile layout has no max-width constraint (full width)"""
        result = about_content(mobile_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        # Mobile should have no max-width (None for full width)
        assert content_container.width is None


class TestAboutContentTablet:
    """Tests for about_content with tablet viewport"""
    
    def test_about_content_with_tablet_page(self, tablet_page):
        """Test about_content() with tablet_page fixture (768px width)"""
        result = about_content(tablet_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        
        # Verify responsive calculations for tablet
        column = result.content.content
        title = column.controls[0]
        
        # Tablet should have medium font sizes (scaled by 0.95)
        # Base title: 32 * 0.95 = 30.4 -> 30
        assert title.size == 30
    
    def test_about_content_tablet_has_responsive_spacing(self, tablet_page):
        """Test that tablet layout has appropriate spacing"""
        result = about_content(tablet_page)
        
        column = result.content.content
        
        # Tablet spacing should be scaled by 0.9
        # Base section_spacing: 20 * 0.9 = 18
        assert column.spacing == 18
        
        # Content container
        content_container = column.controls[1]
        inner_column = content_container.content
        
        # Base inner_spacing: 15 * 0.9 = 13.5 -> 13
        assert inner_column.spacing == 13
    
    def test_about_content_tablet_has_responsive_padding(self, tablet_page):
        """Test that tablet layout has appropriate padding"""
        result = about_content(tablet_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        # Tablet padding: 30 * 0.9 = 27
        assert content_container.padding == 27
    
    def test_about_content_tablet_container_max_width(self, tablet_page):
        """Test that tablet layout has 700px max-width"""
        result = about_content(tablet_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        # Tablet should have max-width of 700px
        assert content_container.width == 700


class TestAboutContentDesktop:
    """Tests for about_content with desktop viewport"""
    
    def test_about_content_with_desktop_page(self, desktop_page):
        """Test about_content() with desktop_page fixture (1920px width)"""
        result = about_content(desktop_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        
        # Verify responsive calculations for desktop
        column = result.content.content
        title = column.controls[0]
        
        # Desktop should have full font sizes (scaled by 1.0)
        # Base title: 32 * 1.0 = 32
        assert title.size == 32
    
    def test_about_content_desktop_has_responsive_spacing(self, desktop_page):
        """Test that desktop layout has full spacing"""
        result = about_content(desktop_page)
        
        column = result.content.content
        
        # Desktop spacing should be scaled by 1.0
        # Base section_spacing: 20 * 1.0 = 20
        assert column.spacing == 20
        
        # Content container
        content_container = column.controls[1]
        inner_column = content_container.content
        
        # Base inner_spacing: 15 * 1.0 = 15
        assert inner_column.spacing == 15
    
    def test_about_content_desktop_has_responsive_padding(self, desktop_page):
        """Test that desktop layout has full padding"""
        result = about_content(desktop_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        # Desktop padding: 30 * 1.0 = 30
        assert content_container.padding == 30
    
    def test_about_content_desktop_container_max_width(self, desktop_page):
        """Test that desktop layout has 800px max-width"""
        result = about_content(desktop_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        # Desktop should have max-width of 800px
        assert content_container.width == 800


class TestAboutContentBreakpoints:
    """Tests for container max-width on different breakpoints"""
    
    def test_container_max_width_mobile(self, mobile_page):
        """Test that mobile breakpoint has no max-width constraint"""
        result = about_content(mobile_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        # Mobile (width=400) should have no max-width
        assert content_container.width is None
    
    def test_container_max_width_tablet(self, tablet_page):
        """Test that tablet breakpoint has 700px max-width"""
        result = about_content(tablet_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        # Tablet (width=768) should have 700px max-width
        assert content_container.width == 700
    
    def test_container_max_width_desktop(self, desktop_page):
        """Test that desktop breakpoint has 800px max-width"""
        result = about_content(desktop_page)
        
        column = result.content.content
        content_container = column.controls[1]
        
        # Desktop (width=1920) should have 800px max-width
        assert content_container.width == 800
    
    def test_all_breakpoints_have_centered_alignment(self, mobile_page, tablet_page, desktop_page):
        """Test that content container is centered on all breakpoints"""
        for page in [mobile_page, tablet_page, desktop_page]:
            result = about_content(page)
            column = result.content.content
            content_container = column.controls[1]
            
            assert content_container.alignment == ft.Alignment.CENTER


class TestAboutContentTextSizes:
    """Tests for responsive text sizes across breakpoints"""
    
    def test_section_title_sizes_responsive(self, mobile_page, tablet_page, desktop_page):
        """Test that section titles have responsive font sizes"""
        # Mobile
        mobile_result = about_content(mobile_page)
        mobile_column = mobile_result.content.content
        mobile_content = mobile_column.controls[1].content
        mobile_section_title = mobile_content.controls[0]
        # Base: 24 * 0.85 = 20.4 -> 20
        assert mobile_section_title.size == 20
        
        # Tablet
        tablet_result = about_content(tablet_page)
        tablet_column = tablet_result.content.content
        tablet_content = tablet_column.controls[1].content
        tablet_section_title = tablet_content.controls[0]
        # Base: 24 * 0.95 = 22.8 -> 22
        assert tablet_section_title.size == 22
        
        # Desktop
        desktop_result = about_content(desktop_page)
        desktop_column = desktop_result.content.content
        desktop_content = desktop_column.controls[1].content
        desktop_section_title = desktop_content.controls[0]
        # Base: 24 * 1.0 = 24
        assert desktop_section_title.size == 24
    
    def test_body_text_sizes_responsive(self, mobile_page, tablet_page, desktop_page):
        """Test that body text has responsive font sizes"""
        # Mobile
        mobile_result = about_content(mobile_page)
        mobile_column = mobile_result.content.content
        mobile_content = mobile_column.controls[1].content
        mobile_body_text = mobile_content.controls[1]
        # Base: 16 * 0.85 = 13.6 -> 13
        assert mobile_body_text.size == 13
        
        # Tablet
        tablet_result = about_content(tablet_page)
        tablet_column = tablet_result.content.content
        tablet_content = tablet_column.controls[1].content
        tablet_body_text = tablet_content.controls[1]
        # Base: 16 * 0.95 = 15.2 -> 15
        assert tablet_body_text.size == 15
        
        # Desktop
        desktop_result = about_content(desktop_page)
        desktop_column = desktop_result.content.content
        desktop_content = desktop_column.controls[1].content
        desktop_body_text = desktop_content.controls[1]
        # Base: 16 * 1.0 = 16
        assert desktop_body_text.size == 16
