"""
Responsive utilities module for GMF-tech application.
Provides breakpoint detection and responsive scaling for fonts, spacing, and layouts.
"""

from enum import Enum
from typing import Dict


class Breakpoint(Enum):
    """Screen size breakpoints for responsive design"""
    MOBILE = "mobile"      # <= 600px
    TABLET = "tablet"      # 601-900px
    DESKTOP = "desktop"    # > 900px


class ResponsiveConfig:
    """Centralized responsive configuration and utilities"""
    
    # Breakpoint thresholds
    MOBILE_MAX = 600
    TABLET_MIN = 601
    TABLET_MAX = 900
    DESKTOP_MIN = 901
    
    # Scaling factors for each breakpoint
    FONT_SCALE = {
        Breakpoint.MOBILE: 0.85,
        Breakpoint.TABLET: 0.95,
        Breakpoint.DESKTOP: 1.0
    }
    
    SPACING_SCALE = {
        Breakpoint.MOBILE: 0.75,
        Breakpoint.TABLET: 0.9,
        Breakpoint.DESKTOP: 1.0
    }
    
    # Grid columns per breakpoint
    GRID_COLUMNS = {
        Breakpoint.MOBILE: 1,
        Breakpoint.TABLET: 2,
        Breakpoint.DESKTOP: 3
    }
    
    # Container padding per breakpoint
    CONTAINER_PADDING = {
        Breakpoint.MOBILE: 20,
        Breakpoint.TABLET: 30,
        Breakpoint.DESKTOP: 40
    }
    
    @staticmethod
    def get_breakpoint(width: int) -> Breakpoint:
        """
        Detect breakpoint based on screen width.
        
        Args:
            width: Screen width in pixels
            
        Returns:
            Breakpoint enum value (MOBILE, TABLET, or DESKTOP)
        """
        if width is None or width <= 0:
            # Default to desktop for invalid values
            return Breakpoint.DESKTOP
            
        if width <= ResponsiveConfig.MOBILE_MAX:
            return Breakpoint.MOBILE
        elif width <= ResponsiveConfig.TABLET_MAX:
            return Breakpoint.TABLET
        else:
            return Breakpoint.DESKTOP
    
    @staticmethod
    def get_font_size(base_size: int, breakpoint: Breakpoint) -> int:
        """
        Calculate responsive font size based on breakpoint.
        
        Args:
            base_size: Base font size in pixels
            breakpoint: Current breakpoint
            
        Returns:
            Scaled font size as integer
        """
        scale = ResponsiveConfig.FONT_SCALE.get(breakpoint, 1.0)
        return int(base_size * scale)
    
    @staticmethod
    def get_spacing(base_spacing: int, breakpoint: Breakpoint) -> int:
        """
        Calculate responsive spacing based on breakpoint.
        
        Args:
            base_spacing: Base spacing in pixels
            breakpoint: Current breakpoint
            
        Returns:
            Scaled spacing as integer
        """
        scale = ResponsiveConfig.SPACING_SCALE.get(breakpoint, 1.0)
        return int(base_spacing * scale)
    
    @staticmethod
    def get_grid_columns(breakpoint: Breakpoint) -> int:
        """
        Get number of grid columns for the current breakpoint.
        
        Args:
            breakpoint: Current breakpoint
            
        Returns:
            Number of columns (1 for mobile, 2 for tablet, 3 for desktop)
        """
        return ResponsiveConfig.GRID_COLUMNS.get(breakpoint, 3)
    
    @staticmethod
    def get_container_padding(breakpoint: Breakpoint) -> Dict[str, int]:
        """
        Get container padding for the current breakpoint.
        
        Args:
            breakpoint: Current breakpoint
            
        Returns:
            Dictionary with padding values
        """
        padding_value = ResponsiveConfig.CONTAINER_PADDING.get(breakpoint, 40)
        return {
            "left": padding_value,
            "right": padding_value,
            "top": padding_value,
            "bottom": padding_value
        }
