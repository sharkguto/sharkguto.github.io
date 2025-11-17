"""
Test fixtures for GMF-tech application tests.
Provides reusable mock objects and test data for unit tests.
"""

import pytest
from unittest.mock import Mock, MagicMock
from theme import COLORS


@pytest.fixture
def mock_page():
    """
    Mock of ft.Page for general testing purposes.
    Provides a basic Page mock with common attributes and methods.
    """
    page = Mock()
    page.width = 1024
    page.height = 768
    page.route = "/"
    page.controls = []
    page.overlay = []
    page.appbar = None
    page.snack_bar = None
    page.title = ""
    page.bgcolor = ""
    page.scroll = "auto"
    page.padding = 0
    page.theme_mode = None
    page.theme = None
    
    # Mock methods
    page.go = Mock()
    page.update = Mock()
    page.run_task = Mock()
    page.close = Mock()
    page.add = Mock()
    
    return page


@pytest.fixture
def mobile_page():
    """
    Mock of ft.Page configured for mobile viewport (400px width).
    Simulates a typical mobile device screen size.
    """
    page = Mock()
    page.width = 400
    page.height = 800
    page.route = "/"
    page.controls = []
    page.overlay = []
    page.appbar = None
    page.snack_bar = None
    page.title = ""
    page.bgcolor = ""
    page.scroll = "auto"
    page.padding = 0
    page.theme_mode = None
    page.theme = None
    
    # Mock methods
    page.go = Mock()
    page.update = Mock()
    page.run_task = Mock()
    page.close = Mock()
    page.add = Mock()
    
    return page


@pytest.fixture
def tablet_page():
    """
    Mock of ft.Page configured for tablet viewport (768px width).
    Simulates a typical tablet device screen size.
    """
    page = Mock()
    page.width = 768
    page.height = 1024
    page.route = "/"
    page.controls = []
    page.overlay = []
    page.appbar = None
    page.snack_bar = None
    page.title = ""
    page.bgcolor = ""
    page.scroll = "auto"
    page.padding = 0
    page.theme_mode = None
    page.theme = None
    
    # Mock methods
    page.go = Mock()
    page.update = Mock()
    page.run_task = Mock()
    page.close = Mock()
    page.add = Mock()
    
    return page


@pytest.fixture
def desktop_page():
    """
    Mock of ft.Page configured for desktop viewport (1920px width).
    Simulates a typical desktop/large screen size.
    """
    page = Mock()
    page.width = 1920
    page.height = 1080
    page.route = "/"
    page.controls = []
    page.overlay = []
    page.appbar = None
    page.snack_bar = None
    page.title = ""
    page.bgcolor = ""
    page.scroll = "auto"
    page.padding = 0
    page.theme_mode = None
    page.theme = None
    
    # Mock methods
    page.go = Mock()
    page.update = Mock()
    page.run_task = Mock()
    page.close = Mock()
    page.add = Mock()
    
    return page


@pytest.fixture
def theme_colors():
    """
    Provides the COLORS dictionary from the theme module.
    Contains all color definitions used throughout the application.
    """
    return COLORS.copy()
