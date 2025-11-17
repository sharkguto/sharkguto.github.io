"""
Unit tests for responsive utilities module.
Tests breakpoint detection, font sizing, spacing, grid columns, and container padding.
"""

import pytest
from utils.responsive import Breakpoint, ResponsiveConfig


class TestBreakpointDetection:
    """Tests for breakpoint detection based on screen width"""
    
    def test_get_breakpoint_with_mobile_width_400px(self):
        """Test get_breakpoint() with mobile width (400px)"""
        width = 400
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        assert result == Breakpoint.MOBILE
        assert isinstance(result, Breakpoint)
    
    def test_get_breakpoint_with_tablet_width_768px(self):
        """Test get_breakpoint() with tablet width (768px)"""
        width = 768
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        assert result == Breakpoint.TABLET
        assert isinstance(result, Breakpoint)
    
    def test_get_breakpoint_with_desktop_width_1920px(self):
        """Test get_breakpoint() with desktop width (1920px)"""
        width = 1920
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        assert result == Breakpoint.DESKTOP
        assert isinstance(result, Breakpoint)
    
    def test_get_breakpoint_with_edge_case_600px(self):
        """Test get_breakpoint() with edge case at mobile/tablet boundary (600px)"""
        width = 600
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        # 600px is the MOBILE_MAX, so it should be MOBILE
        assert result == Breakpoint.MOBILE
    
    def test_get_breakpoint_with_edge_case_601px(self):
        """Test get_breakpoint() with edge case just above mobile boundary (601px)"""
        width = 601
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        # 601px is TABLET_MIN, so it should be TABLET
        assert result == Breakpoint.TABLET
    
    def test_get_breakpoint_with_edge_case_900px(self):
        """Test get_breakpoint() with edge case at tablet/desktop boundary (900px)"""
        width = 900
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        # 900px is the TABLET_MAX, so it should be TABLET
        assert result == Breakpoint.TABLET
    
    def test_get_breakpoint_with_edge_case_901px(self):
        """Test get_breakpoint() with edge case just above tablet boundary (901px)"""
        width = 901
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        # 901px is DESKTOP_MIN, so it should be DESKTOP
        assert result == Breakpoint.DESKTOP
    
    def test_get_breakpoint_with_very_small_mobile_width(self):
        """Test get_breakpoint() with very small mobile width (320px)"""
        width = 320
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        assert result == Breakpoint.MOBILE
    
    def test_get_breakpoint_with_very_large_desktop_width(self):
        """Test get_breakpoint() with very large desktop width (2560px)"""
        width = 2560
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        assert result == Breakpoint.DESKTOP
    
    def test_get_breakpoint_with_none_defaults_to_desktop(self):
        """Test get_breakpoint() with None defaults to DESKTOP"""
        width = None
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        assert result == Breakpoint.DESKTOP
    
    def test_get_breakpoint_with_zero_defaults_to_desktop(self):
        """Test get_breakpoint() with zero defaults to DESKTOP"""
        width = 0
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        assert result == Breakpoint.DESKTOP
    
    def test_get_breakpoint_with_negative_defaults_to_desktop(self):
        """Test get_breakpoint() with negative value defaults to DESKTOP"""
        width = -100
        
        result = ResponsiveConfig.get_breakpoint(width)
        
        assert result == Breakpoint.DESKTOP


class TestFontSize:
    """Tests for responsive font size calculation"""
    
    def test_get_font_size_for_mobile_breakpoint(self):
        """Test get_font_size() for MOBILE breakpoint"""
        base_size = 20
        breakpoint = Breakpoint.MOBILE
        
        result = ResponsiveConfig.get_font_size(base_size, breakpoint)
        
        # Mobile scale is 0.85: 20 * 0.85 = 17
        assert result == 17
        assert isinstance(result, int)
    
    def test_get_font_size_for_tablet_breakpoint(self):
        """Test get_font_size() for TABLET breakpoint"""
        base_size = 20
        breakpoint = Breakpoint.TABLET
        
        result = ResponsiveConfig.get_font_size(base_size, breakpoint)
        
        # Tablet scale is 0.95: 20 * 0.95 = 19
        assert result == 19
        assert isinstance(result, int)
    
    def test_get_font_size_for_desktop_breakpoint(self):
        """Test get_font_size() for DESKTOP breakpoint"""
        base_size = 20
        breakpoint = Breakpoint.DESKTOP
        
        result = ResponsiveConfig.get_font_size(base_size, breakpoint)
        
        # Desktop scale is 1.0: 20 * 1.0 = 20
        assert result == 20
        assert isinstance(result, int)
    
    def test_get_font_size_with_different_base_sizes(self):
        """Test get_font_size() with various base sizes"""
        # Test with base size 16
        mobile_16 = ResponsiveConfig.get_font_size(16, Breakpoint.MOBILE)
        assert mobile_16 == int(16 * 0.85)  # 13
        
        tablet_16 = ResponsiveConfig.get_font_size(16, Breakpoint.TABLET)
        assert tablet_16 == int(16 * 0.95)  # 15
        
        desktop_16 = ResponsiveConfig.get_font_size(16, Breakpoint.DESKTOP)
        assert desktop_16 == 16
        
        # Test with base size 24
        mobile_24 = ResponsiveConfig.get_font_size(24, Breakpoint.MOBILE)
        assert mobile_24 == int(24 * 0.85)  # 20
        
        tablet_24 = ResponsiveConfig.get_font_size(24, Breakpoint.TABLET)
        assert tablet_24 == int(24 * 0.95)  # 22
        
        desktop_24 = ResponsiveConfig.get_font_size(24, Breakpoint.DESKTOP)
        assert desktop_24 == 24
    
    def test_get_font_size_returns_integer(self):
        """Test that get_font_size() always returns an integer"""
        # Test with a size that would produce a decimal
        base_size = 17
        
        mobile_result = ResponsiveConfig.get_font_size(base_size, Breakpoint.MOBILE)
        tablet_result = ResponsiveConfig.get_font_size(base_size, Breakpoint.TABLET)
        desktop_result = ResponsiveConfig.get_font_size(base_size, Breakpoint.DESKTOP)
        
        assert isinstance(mobile_result, int)
        assert isinstance(tablet_result, int)
        assert isinstance(desktop_result, int)


class TestSpacing:
    """Tests for responsive spacing calculation"""
    
    def test_get_spacing_for_mobile_breakpoint(self):
        """Test get_spacing() for MOBILE breakpoint"""
        base_spacing = 24
        breakpoint = Breakpoint.MOBILE
        
        result = ResponsiveConfig.get_spacing(base_spacing, breakpoint)
        
        # Mobile scale is 0.75: 24 * 0.75 = 18
        assert result == 18
        assert isinstance(result, int)
    
    def test_get_spacing_for_tablet_breakpoint(self):
        """Test get_spacing() for TABLET breakpoint"""
        base_spacing = 24
        breakpoint = Breakpoint.TABLET
        
        result = ResponsiveConfig.get_spacing(base_spacing, breakpoint)
        
        # Tablet scale is 0.9: 24 * 0.9 = 21.6 -> 21
        assert result == 21
        assert isinstance(result, int)
    
    def test_get_spacing_for_desktop_breakpoint(self):
        """Test get_spacing() for DESKTOP breakpoint"""
        base_spacing = 24
        breakpoint = Breakpoint.DESKTOP
        
        result = ResponsiveConfig.get_spacing(base_spacing, breakpoint)
        
        # Desktop scale is 1.0: 24 * 1.0 = 24
        assert result == 24
        assert isinstance(result, int)
    
    def test_get_spacing_with_different_base_values(self):
        """Test get_spacing() with various base spacing values"""
        # Test with base spacing 30
        mobile_30 = ResponsiveConfig.get_spacing(30, Breakpoint.MOBILE)
        assert mobile_30 == int(30 * 0.75)  # 22
        
        tablet_30 = ResponsiveConfig.get_spacing(30, Breakpoint.TABLET)
        assert tablet_30 == int(30 * 0.9)  # 27
        
        desktop_30 = ResponsiveConfig.get_spacing(30, Breakpoint.DESKTOP)
        assert desktop_30 == 30
        
        # Test with base spacing 16
        mobile_16 = ResponsiveConfig.get_spacing(16, Breakpoint.MOBILE)
        assert mobile_16 == int(16 * 0.75)  # 12
        
        tablet_16 = ResponsiveConfig.get_spacing(16, Breakpoint.TABLET)
        assert tablet_16 == int(16 * 0.9)  # 14
        
        desktop_16 = ResponsiveConfig.get_spacing(16, Breakpoint.DESKTOP)
        assert desktop_16 == 16
    
    def test_get_spacing_returns_integer(self):
        """Test that get_spacing() always returns an integer"""
        # Test with a value that would produce a decimal
        base_spacing = 25
        
        mobile_result = ResponsiveConfig.get_spacing(base_spacing, Breakpoint.MOBILE)
        tablet_result = ResponsiveConfig.get_spacing(base_spacing, Breakpoint.TABLET)
        desktop_result = ResponsiveConfig.get_spacing(base_spacing, Breakpoint.DESKTOP)
        
        assert isinstance(mobile_result, int)
        assert isinstance(tablet_result, int)
        assert isinstance(desktop_result, int)


class TestGridColumns:
    """Tests for grid columns per breakpoint"""
    
    def test_get_grid_columns_returns_correct_columns_for_mobile(self):
        """Test get_grid_columns() returns 1 column for MOBILE breakpoint"""
        breakpoint = Breakpoint.MOBILE
        
        result = ResponsiveConfig.get_grid_columns(breakpoint)
        
        assert result == 1
        assert isinstance(result, int)
    
    def test_get_grid_columns_returns_correct_columns_for_tablet(self):
        """Test get_grid_columns() returns 2 columns for TABLET breakpoint"""
        breakpoint = Breakpoint.TABLET
        
        result = ResponsiveConfig.get_grid_columns(breakpoint)
        
        assert result == 2
        assert isinstance(result, int)
    
    def test_get_grid_columns_returns_correct_columns_for_desktop(self):
        """Test get_grid_columns() returns 3 columns for DESKTOP breakpoint"""
        breakpoint = Breakpoint.DESKTOP
        
        result = ResponsiveConfig.get_grid_columns(breakpoint)
        
        assert result == 3
        assert isinstance(result, int)
    
    def test_get_grid_columns_for_all_breakpoints(self):
        """Test get_grid_columns() returns correct values for all breakpoints"""
        mobile_columns = ResponsiveConfig.get_grid_columns(Breakpoint.MOBILE)
        tablet_columns = ResponsiveConfig.get_grid_columns(Breakpoint.TABLET)
        desktop_columns = ResponsiveConfig.get_grid_columns(Breakpoint.DESKTOP)
        
        # Verify progression: mobile < tablet < desktop
        assert mobile_columns < tablet_columns < desktop_columns
        assert mobile_columns == 1
        assert tablet_columns == 2
        assert desktop_columns == 3


class TestContainerPadding:
    """Tests for container padding per breakpoint"""
    
    def test_get_container_padding_returns_correct_padding_for_mobile(self):
        """Test get_container_padding() returns correct padding dict for MOBILE breakpoint"""
        breakpoint = Breakpoint.MOBILE
        
        result = ResponsiveConfig.get_container_padding(breakpoint)
        
        assert isinstance(result, dict)
        assert result["left"] == 20
        assert result["right"] == 20
        assert result["top"] == 20
        assert result["bottom"] == 20
    
    def test_get_container_padding_returns_correct_padding_for_tablet(self):
        """Test get_container_padding() returns correct padding dict for TABLET breakpoint"""
        breakpoint = Breakpoint.TABLET
        
        result = ResponsiveConfig.get_container_padding(breakpoint)
        
        assert isinstance(result, dict)
        assert result["left"] == 30
        assert result["right"] == 30
        assert result["top"] == 30
        assert result["bottom"] == 30
    
    def test_get_container_padding_returns_correct_padding_for_desktop(self):
        """Test get_container_padding() returns correct padding dict for DESKTOP breakpoint"""
        breakpoint = Breakpoint.DESKTOP
        
        result = ResponsiveConfig.get_container_padding(breakpoint)
        
        assert isinstance(result, dict)
        assert result["left"] == 40
        assert result["right"] == 40
        assert result["top"] == 40
        assert result["bottom"] == 40
    
    def test_get_container_padding_has_all_required_keys(self):
        """Test that get_container_padding() returns dict with all required keys"""
        for breakpoint in [Breakpoint.MOBILE, Breakpoint.TABLET, Breakpoint.DESKTOP]:
            result = ResponsiveConfig.get_container_padding(breakpoint)
            
            assert "left" in result
            assert "right" in result
            assert "top" in result
            assert "bottom" in result
            assert len(result) == 4
    
    def test_get_container_padding_values_are_integers(self):
        """Test that all padding values are integers"""
        for breakpoint in [Breakpoint.MOBILE, Breakpoint.TABLET, Breakpoint.DESKTOP]:
            result = ResponsiveConfig.get_container_padding(breakpoint)
            
            assert isinstance(result["left"], int)
            assert isinstance(result["right"], int)
            assert isinstance(result["top"], int)
            assert isinstance(result["bottom"], int)
    
    def test_get_container_padding_progression(self):
        """Test that padding increases from mobile to tablet to desktop"""
        mobile_padding = ResponsiveConfig.get_container_padding(Breakpoint.MOBILE)
        tablet_padding = ResponsiveConfig.get_container_padding(Breakpoint.TABLET)
        desktop_padding = ResponsiveConfig.get_container_padding(Breakpoint.DESKTOP)
        
        # Verify progression: mobile < tablet < desktop
        assert mobile_padding["left"] < tablet_padding["left"] < desktop_padding["left"]
        assert mobile_padding["left"] == 20
        assert tablet_padding["left"] == 30
        assert desktop_padding["left"] == 40
