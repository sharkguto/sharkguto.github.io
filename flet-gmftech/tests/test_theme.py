"""
Unit tests for theme module.
Tests theme functions, button styles, text styles, shadows, and responsive utilities.
"""

import pytest
import flet as ft
from theme import (
    get_theme,
    get_button_style,
    get_text_style,
    get_shadow,
    get_responsive_font_size,
    get_responsive_padding,
    get_responsive_spacing,
    COLORS
)


class TestThemeBasics:
    """Tests for basic theme functions"""
    
    def test_get_theme_returns_valid_theme_object(self):
        """Test that get_theme() returns a valid Theme object"""
        theme = get_theme()
        
        assert isinstance(theme, ft.Theme)
        assert theme.font_family == "Roboto"
        assert theme.color_scheme is not None
        assert isinstance(theme.color_scheme, ft.ColorScheme)
    
    def test_get_theme_has_correct_colors(self):
        """Test that theme has correct color scheme"""
        theme = get_theme()
        
        assert theme.color_scheme.primary == COLORS["primary"]
        assert theme.color_scheme.secondary == COLORS["secondary"]
        assert theme.color_scheme.surface == COLORS["surface"]
        assert theme.color_scheme.background == COLORS["background"]


class TestButtonStyle:
    """Tests for button style function"""
    
    def test_get_button_style_returns_valid_button_style(self):
        """Test that get_button_style() returns ButtonStyle with correct properties"""
        button_style = get_button_style()
        
        assert isinstance(button_style, ft.ButtonStyle)
        assert button_style.shape is not None
        assert button_style.padding is not None
        assert button_style.overlay_color is not None
    
    def test_get_button_style_has_rounded_border(self):
        """Test that button style has rounded border with radius 8"""
        button_style = get_button_style()
        
        # Shape is stored as a dict with ControlState keys
        assert isinstance(button_style.shape, dict)
        default_shape = button_style.shape.get(ft.ControlState.DEFAULT)
        assert isinstance(default_shape, ft.RoundedRectangleBorder)
        assert default_shape.radius == 8
    
    def test_get_button_style_has_correct_padding(self):
        """Test that button style has correct padding values"""
        button_style = get_button_style()
        
        # Padding is stored as a dict with ControlState keys
        assert isinstance(button_style.padding, dict)
        default_padding = button_style.padding.get(ft.ControlState.DEFAULT)
        assert default_padding.left == 30
        assert default_padding.right == 30
        assert default_padding.top == 15
        assert default_padding.bottom == 15


class TestTextStyle:
    """Tests for text style function"""
    
    def test_get_text_style_with_default_parameters(self):
        """Test get_text_style() with default parameters"""
        text_style = get_text_style()
        
        assert isinstance(text_style, ft.TextStyle)
        assert text_style.font_family == "Roboto"
        assert text_style.size == 16
        assert text_style.color == COLORS["text_primary"]
        assert text_style.weight is None
    
    def test_get_text_style_with_custom_size(self):
        """Test get_text_style() with custom size"""
        text_style = get_text_style(size=24)
        
        assert text_style.size == 24
        assert text_style.font_family == "Roboto"
    
    def test_get_text_style_with_custom_color(self):
        """Test get_text_style() with custom color"""
        custom_color = "#FF0000"
        text_style = get_text_style(color=custom_color)
        
        assert text_style.color == custom_color
        assert text_style.size == 16
    
    def test_get_text_style_with_custom_weight(self):
        """Test get_text_style() with custom weight"""
        text_style = get_text_style(weight=ft.FontWeight.BOLD)
        
        assert text_style.weight == ft.FontWeight.BOLD
        assert text_style.size == 16
    
    def test_get_text_style_with_all_custom_parameters(self):
        """Test get_text_style() with custom size, color, and weight"""
        custom_color = COLORS["accent"]
        text_style = get_text_style(
            size=20,
            color=custom_color,
            weight=ft.FontWeight.W_500
        )
        
        assert text_style.size == 20
        assert text_style.color == custom_color
        assert text_style.weight == ft.FontWeight.W_500
        assert text_style.font_family == "Roboto"


class TestShadow:
    """Tests for shadow function"""
    
    def test_get_shadow_returns_valid_box_shadow(self):
        """Test that get_shadow() returns BoxShadow with correct properties"""
        shadow = get_shadow()
        
        assert isinstance(shadow, ft.BoxShadow)
        assert shadow.spread_radius == 1
        assert shadow.blur_radius == 15
        assert shadow.color is not None
        assert shadow.offset is not None
    
    def test_get_shadow_has_correct_offset(self):
        """Test that shadow has correct offset values"""
        shadow = get_shadow()
        
        assert isinstance(shadow.offset, ft.Offset)
        assert shadow.offset.x == 0
        assert shadow.offset.y == 0


class TestResponsiveFontSize:
    """Tests for responsive font size function"""
    
    def test_get_responsive_font_size_with_mobile_width(self):
        """Test get_responsive_font_size() with mobile width (400px)"""
        # Mobile breakpoint: <= 600px, scale = 0.85
        base_size = 20
        mobile_width = 400
        
        result = get_responsive_font_size(base_size, mobile_width)
        
        # Expected: 20 * 0.85 = 17
        assert result == 17
        assert isinstance(result, int)
    
    def test_get_responsive_font_size_with_tablet_width(self):
        """Test get_responsive_font_size() with tablet width (768px)"""
        # Tablet breakpoint: 601-900px, scale = 0.95
        base_size = 20
        tablet_width = 768
        
        result = get_responsive_font_size(base_size, tablet_width)
        
        # Expected: 20 * 0.95 = 19
        assert result == 19
        assert isinstance(result, int)
    
    def test_get_responsive_font_size_with_desktop_width(self):
        """Test get_responsive_font_size() with desktop width (1920px)"""
        # Desktop breakpoint: > 900px, scale = 1.0
        base_size = 20
        desktop_width = 1920
        
        result = get_responsive_font_size(base_size, desktop_width)
        
        # Expected: 20 * 1.0 = 20
        assert result == 20
        assert isinstance(result, int)
    
    def test_get_responsive_font_size_with_edge_case_widths(self):
        """Test get_responsive_font_size() with edge case widths"""
        base_size = 16
        
        # Test at mobile/tablet boundary (600px)
        result_600 = get_responsive_font_size(base_size, 600)
        assert result_600 == int(16 * 0.85)  # Mobile
        
        # Test at tablet/desktop boundary (900px)
        result_900 = get_responsive_font_size(base_size, 900)
        assert result_900 == int(16 * 0.95)  # Tablet
        
        # Test just above tablet boundary (901px)
        result_901 = get_responsive_font_size(base_size, 901)
        assert result_901 == 16  # Desktop
    
    def test_get_responsive_font_size_with_invalid_width(self):
        """Test get_responsive_font_size() with invalid width defaults to desktop"""
        base_size = 20
        
        # Test with None
        result_none = get_responsive_font_size(base_size, None)
        assert result_none == 20  # Desktop default
        
        # Test with zero
        result_zero = get_responsive_font_size(base_size, 0)
        assert result_zero == 20  # Desktop default
        
        # Test with negative
        result_negative = get_responsive_font_size(base_size, -100)
        assert result_negative == 20  # Desktop default


class TestResponsivePadding:
    """Tests for responsive padding function"""
    
    def test_get_responsive_padding_with_mobile_width(self):
        """Test get_responsive_padding() with mobile width"""
        base_padding = 40
        mobile_width = 400
        
        result = get_responsive_padding(base_padding, mobile_width)
        
        # Expected: 40 * 0.75 = 30
        assert result == 30
        assert isinstance(result, int)
    
    def test_get_responsive_padding_with_tablet_width(self):
        """Test get_responsive_padding() with tablet width"""
        base_padding = 40
        tablet_width = 768
        
        result = get_responsive_padding(base_padding, tablet_width)
        
        # Expected: 40 * 0.9 = 36
        assert result == 36
        assert isinstance(result, int)
    
    def test_get_responsive_padding_with_desktop_width(self):
        """Test get_responsive_padding() with desktop width"""
        base_padding = 40
        desktop_width = 1920
        
        result = get_responsive_padding(base_padding, desktop_width)
        
        # Expected: 40 * 1.0 = 40
        assert result == 40
        assert isinstance(result, int)
    
    def test_get_responsive_padding_with_different_widths(self):
        """Test get_responsive_padding() with various widths"""
        base_padding = 20
        
        # Mobile (400px)
        mobile_result = get_responsive_padding(base_padding, 400)
        assert mobile_result == 15  # 20 * 0.75
        
        # Tablet (750px)
        tablet_result = get_responsive_padding(base_padding, 750)
        assert tablet_result == 18  # 20 * 0.9
        
        # Desktop (1200px)
        desktop_result = get_responsive_padding(base_padding, 1200)
        assert desktop_result == 20  # 20 * 1.0


class TestResponsiveSpacing:
    """Tests for responsive spacing function"""
    
    def test_get_responsive_spacing_with_mobile_width(self):
        """Test get_responsive_spacing() with mobile width"""
        base_spacing = 24
        mobile_width = 400
        
        result = get_responsive_spacing(base_spacing, mobile_width)
        
        # Expected: 24 * 0.75 = 18
        assert result == 18
        assert isinstance(result, int)
    
    def test_get_responsive_spacing_with_tablet_width(self):
        """Test get_responsive_spacing() with tablet width"""
        base_spacing = 24
        tablet_width = 768
        
        result = get_responsive_spacing(base_spacing, tablet_width)
        
        # Expected: 24 * 0.9 = 21 (rounded down from 21.6)
        assert result == 21
        assert isinstance(result, int)
    
    def test_get_responsive_spacing_with_desktop_width(self):
        """Test get_responsive_spacing() with desktop width"""
        base_spacing = 24
        desktop_width = 1920
        
        result = get_responsive_spacing(base_spacing, desktop_width)
        
        # Expected: 24 * 1.0 = 24
        assert result == 24
        assert isinstance(result, int)
    
    def test_get_responsive_spacing_with_different_widths(self):
        """Test get_responsive_spacing() with various widths and base values"""
        # Test with base spacing of 30
        base_spacing = 30
        
        # Mobile (500px)
        mobile_result = get_responsive_spacing(base_spacing, 500)
        assert mobile_result == 22  # 30 * 0.75 = 22.5 -> 22
        
        # Tablet (800px)
        tablet_result = get_responsive_spacing(base_spacing, 800)
        assert tablet_result == 27  # 30 * 0.9 = 27
        
        # Desktop (1600px)
        desktop_result = get_responsive_spacing(base_spacing, 1600)
        assert desktop_result == 30  # 30 * 1.0 = 30
    
    def test_get_responsive_spacing_consistency_with_padding(self):
        """Test that spacing and padding use the same scaling logic"""
        base_value = 16
        width = 700  # Tablet
        
        spacing_result = get_responsive_spacing(base_value, width)
        padding_result = get_responsive_padding(base_value, width)
        
        # Both should use the same scaling factor
        assert spacing_result == padding_result
