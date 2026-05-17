"""
Unit tests for coins page module.
Tests currency_chart_content function, chart creation, data fetching, and cache mechanism.
"""

import pytest
from unittest.mock import Mock, AsyncMock, patch, MagicMock
import flet as ft
from pages.coins import (
    currency_chart_content,
    create_chart,
    fetch_usd_brl_data,
    load_chart,
)
from theme import COLORS
from datetime import datetime, timedelta


class TestCurrencyChartContent:
    """Tests for currency_chart_content function"""
    
    def test_currency_chart_content_returns_valid_container(self, mock_page):
        """Test that currency_chart_content() returns a valid Container"""
        result = currency_chart_content(mock_page)
        
        assert isinstance(result, ft.Container)
        assert result.expand is True
        assert result.content is not None
    
    def test_currency_chart_content_has_correct_structure(self, mock_page):
        """Test that currency_chart_content has the correct nested structure"""
        result = currency_chart_content(mock_page)
        
        # Outer container
        assert isinstance(result, ft.Container)
        assert result.expand is True
        
        # Stack
        stack = result.content
        assert isinstance(stack, ft.Stack)
        assert stack.expand is True
        
        # Column inside stack
        column = stack.controls[0]
        assert isinstance(column, ft.Column)
        assert column.expand is True
    
    def test_currency_chart_content_has_title_and_subtitle(self, mock_page):
        """Test that currency_chart_content contains title and subtitle"""
        result = currency_chart_content(mock_page)
        
        stack = result.content
        column = stack.controls[0]
        
        # Title
        title = column.controls[0]
        assert isinstance(title, ft.Text)
        assert title.value == "Cotação USD/BRL"
        assert title.weight == "bold"
        assert title.color == COLORS["text_primary"]
        assert title.text_align == "center"
        
        # Subtitle
        subtitle = column.controls[1]
        assert isinstance(subtitle, ft.Text)
        assert "últimos 15 dias" in subtitle.value
        assert subtitle.color == COLORS["text_secondary"]
        assert subtitle.text_align == "center"
    
    def test_currency_chart_content_has_chart_container(self, mock_page):
        """Test that currency_chart_content contains chart container"""
        result = currency_chart_content(mock_page)
        
        stack = result.content
        column = stack.controls[0]
        
        # Chart container
        chart_container = column.controls[2]
        assert isinstance(chart_container, ft.Container)
        assert chart_container.expand is True
        assert chart_container.bgcolor == COLORS["surface"]
        assert chart_container.border_radius is not None
        assert chart_container.shadow is not None
    
    def test_currency_chart_content_shows_loading_state(self, mock_page):
        """Test that currency_chart_content initially shows loading state"""
        result = currency_chart_content(mock_page)
        
        stack = result.content
        column = stack.controls[0]
        chart_container = column.controls[2]
        
        # Loading state
        loading_column = chart_container.content
        assert isinstance(loading_column, ft.Column)
        assert loading_column.alignment == "center"
        assert loading_column.horizontal_alignment == "center"
        
        # Should have loading text and progress ring
        assert len(loading_column.controls) == 2
        
        loading_text = loading_column.controls[0]
        assert isinstance(loading_text, ft.Text)
        assert "Carregando" in loading_text.value
        
        progress_ring = loading_column.controls[1]
        assert isinstance(progress_ring, ft.ProgressRing)


class TestCurrencyChartContentMobile:
    """Tests for currency_chart_content with mobile viewport"""
    
    def test_currency_chart_content_mobile_responsive_font_sizes(self, mobile_page):
        """Test that mobile layout has scaled font sizes"""
        result = currency_chart_content(mobile_page)
        
        stack = result.content
        column = stack.controls[0]
        
        # Title font size (32 * 0.85 = 27.2 -> 27)
        title = column.controls[0]
        assert title.size == 27
        
        # Subtitle font size (16 * 0.85 = 13.6 -> 13)
        subtitle = column.controls[1]
        assert subtitle.size == 13
    
    def test_currency_chart_content_mobile_chart_height(self, mobile_page):
        """Test that mobile layout has correct chart height (300px)"""
        result = currency_chart_content(mobile_page)
        
        stack = result.content
        column = stack.controls[0]
        chart_container = column.controls[2]
        
        # Mobile chart height should be 300px
        assert chart_container.height == 300
    
    def test_currency_chart_content_mobile_responsive_padding(self, mobile_page):
        """Test that mobile layout has scaled padding"""
        result = currency_chart_content(mobile_page)
        
        stack = result.content
        column = stack.controls[0]
        chart_container = column.controls[2]
        
        # Container padding (20 * 0.75 = 15)
        assert chart_container.padding == 15


class TestCurrencyChartContentTablet:
    """Tests for currency_chart_content with tablet viewport"""
    
    def test_currency_chart_content_tablet_responsive_font_sizes(self, tablet_page):
        """Test that tablet layout has scaled font sizes"""
        result = currency_chart_content(tablet_page)
        
        stack = result.content
        column = stack.controls[0]
        
        # Title font size (32 * 0.95 = 30.4 -> 30)
        title = column.controls[0]
        assert title.size == 30
        
        # Subtitle font size (16 * 0.95 = 15.2 -> 15)
        subtitle = column.controls[1]
        assert subtitle.size == 15
    
    def test_currency_chart_content_tablet_chart_height(self, tablet_page):
        """Test that tablet layout has correct chart height (350px)"""
        result = currency_chart_content(tablet_page)
        
        stack = result.content
        column = stack.controls[0]
        chart_container = column.controls[2]
        
        # Tablet chart height should be 350px
        assert chart_container.height == 350


class TestCurrencyChartContentDesktop:
    """Tests for currency_chart_content with desktop viewport"""
    
    def test_currency_chart_content_desktop_responsive_font_sizes(self, desktop_page):
        """Test that desktop layout has full font sizes"""
        result = currency_chart_content(desktop_page)
        
        stack = result.content
        column = stack.controls[0]
        
        # Title font size (32 * 1.0 = 32)
        title = column.controls[0]
        assert title.size == 32
        
        # Subtitle font size (16 * 1.0 = 16)
        subtitle = column.controls[1]
        assert subtitle.size == 16
    
    def test_currency_chart_content_desktop_chart_height(self, desktop_page):
        """Test that desktop layout has correct chart height (400px)"""
        result = currency_chart_content(desktop_page)
        
        stack = result.content
        column = stack.controls[0]
        chart_container = column.controls[2]
        
        # Desktop chart height should be 400px
        assert chart_container.height == 400


class TestCreateChart:
    """Tests for create_chart function"""
    
    def test_create_chart_with_valid_data(self):
        """Test that create_chart() returns a native Flet chart with valid data"""
        # Sample data matching API structure
        data = [
            {
                "timestamp": "1700000000",
                "high": "5.10",
                "low": "5.00",
                "pctChange": "0.5"
            },
            {
                "timestamp": "1700086400",
                "high": "5.15",
                "low": "5.05",
                "pctChange": "0.8"
            },
            {
                "timestamp": "1700172800",
                "high": "5.20",
                "low": "5.10",
                "pctChange": "1.0"
            }
        ]
        
        result = create_chart(data, "400px")
        
        assert result is not None
        assert isinstance(result, ft.Container)
        assert result.expand is True
        assert result.bgcolor == COLORS["surface"]
        assert result.data["high"] == 5.20
        assert result.data["low"] == 5.00
        assert len(result.data["points"]) == 3
    
    def test_create_chart_with_empty_data(self):
        """Test that create_chart() returns None with empty data"""
        result = create_chart([], "400px")
        
        assert result is None
    
    def test_create_chart_with_none_data(self):
        """Test that create_chart() returns None with None data"""
        result = create_chart(None, "400px")
        
        assert result is None
    
    def test_create_chart_is_deterministic_for_same_data(self):
        """Test that create_chart() renders the same point data for same input"""
        data = [
            {
                "timestamp": "1700000000",
                "high": "5.10",
                "low": "5.00",
                "pctChange": "0.5"
            }
        ]
        
        # First call
        result1 = create_chart(data, "400px")
        
        # Second call with same data
        result2 = create_chart(data, "400px")
        
        # Both should be valid native Flet charts with same point data
        assert result1 is not None
        assert result2 is not None
        assert isinstance(result1, ft.Container)
        assert isinstance(result2, ft.Container)
        assert result1.data == result2.data


@pytest.mark.asyncio
class TestFetchUsdBrlData:
    """Tests for fetch_usd_brl_data function"""
    
    async def test_fetch_usd_brl_data_with_mocked_httpx(self):
        """Test fetch_usd_brl_data() with mocked httpx client"""
        # Clear cache
        import pages.coins as coins_module
        coins_module._cached_data = None
        coins_module._last_update = None
        coins_module._is_fetching = False
        
        mock_data = [
            {
                "timestamp": "1700000000",
                "high": "5.10",
                "low": "5.00",
                "pctChange": "0.5"
            }
        ]
        
        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json = Mock(return_value=mock_data)
            
            mock_client_instance = AsyncMock()
            mock_client_instance.get = AsyncMock(return_value=mock_response)
            mock_client_instance.__aenter__ = AsyncMock(return_value=mock_client_instance)
            mock_client_instance.__aexit__ = AsyncMock(return_value=None)
            
            mock_client.return_value = mock_client_instance
            
            result = await fetch_usd_brl_data(force_refresh=True)
            
            assert result == mock_data
            assert coins_module._cached_data == mock_data
            assert coins_module._last_update is not None
    
    async def test_fetch_usd_brl_data_cache_mechanism(self):
        """Test that cache mechanism prevents refetch within 5 minutes"""
        # Setup cache with recent data
        import pages.coins as coins_module
        
        cached_data = [{"timestamp": "1700000000", "high": "5.10", "low": "5.00", "pctChange": "0.5"}]
        coins_module._cached_data = cached_data
        coins_module._last_update = datetime.now()
        coins_module._is_fetching = False
        
        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            # This should not be called due to cache
            result = await fetch_usd_brl_data(force_refresh=False)
            
            # Should return cached data without making HTTP request
            assert result == cached_data
            mock_client.assert_not_called()
    
    async def test_fetch_usd_brl_data_cache_expires_after_5_minutes(self):
        """Test that cache expires and refetches after 5 minutes"""
        # Setup cache with old data (6 minutes ago)
        import pages.coins as coins_module
        
        old_data = [{"timestamp": "1700000000", "high": "5.00", "low": "4.90", "pctChange": "0.3"}]
        new_data = [{"timestamp": "1700000360", "high": "5.10", "low": "5.00", "pctChange": "0.5"}]
        
        coins_module._cached_data = old_data
        coins_module._last_update = datetime.now() - timedelta(minutes=6)
        coins_module._is_fetching = False
        
        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json = Mock(return_value=new_data)
            
            mock_client_instance = AsyncMock()
            mock_client_instance.get = AsyncMock(return_value=mock_response)
            mock_client_instance.__aenter__ = AsyncMock(return_value=mock_client_instance)
            mock_client_instance.__aexit__ = AsyncMock(return_value=None)
            
            mock_client.return_value = mock_client_instance
            
            result = await fetch_usd_brl_data(force_refresh=False)
            
            # Should fetch new data
            assert result == new_data
            assert coins_module._cached_data == new_data
            mock_client.assert_called_once()
    
    async def test_fetch_usd_brl_data_handles_http_error(self):
        """Test that fetch_usd_brl_data handles HTTP errors gracefully"""
        # Setup with existing cache
        import pages.coins as coins_module
        
        cached_data = [{"timestamp": "1700000000", "high": "5.10", "low": "5.00", "pctChange": "0.5"}]
        coins_module._cached_data = cached_data
        coins_module._last_update = datetime.now() - timedelta(minutes=6)
        coins_module._is_fetching = False
        
        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            mock_response = Mock()
            mock_response.status_code = 500
            
            mock_client_instance = AsyncMock()
            mock_client_instance.get = AsyncMock(return_value=mock_response)
            mock_client_instance.__aenter__ = AsyncMock(return_value=mock_client_instance)
            mock_client_instance.__aexit__ = AsyncMock(return_value=None)
            
            mock_client.return_value = mock_client_instance
            
            result = await fetch_usd_brl_data(force_refresh=True)
            
            # Should return cached data on error
            assert result == cached_data
    
    async def test_fetch_usd_brl_data_returns_empty_on_error_without_cache(self):
        """Test that fetch_usd_brl_data returns empty list on error without cache"""
        # Clear cache
        import pages.coins as coins_module
        coins_module._cached_data = None
        coins_module._last_update = None
        coins_module._is_fetching = False
        
        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            mock_response = Mock()
            mock_response.status_code = 500
            
            mock_client_instance = AsyncMock()
            mock_client_instance.get = AsyncMock(return_value=mock_response)
            mock_client_instance.__aenter__ = AsyncMock(return_value=mock_client_instance)
            mock_client_instance.__aexit__ = AsyncMock(return_value=None)
            
            mock_client.return_value = mock_client_instance
            
            result = await fetch_usd_brl_data(force_refresh=True)
            
            # Should return empty list
            assert result == []


@pytest.mark.asyncio
class TestLoadChart:
    """Tests for load_chart function"""
    
    async def test_load_chart_displays_error_on_empty_data(self, mock_page):
        """Test that load_chart displays error message when data is empty"""
        chart_container = ft.Container()
        error_button = ft.Button("Retry")
        
        with patch("pages.coins.fetch_usd_brl_data", new_callable=AsyncMock) as mock_fetch:
            mock_fetch.return_value = []
            
            await load_chart(mock_page, chart_container, error_button, "400px")
            
            # Should display error message
            assert isinstance(chart_container.content, ft.Column)
            error_column = chart_container.content
            assert error_column.alignment == "center"
            
            # Should have error text and button
            error_text = error_column.controls[0]
            assert isinstance(error_text, ft.Text)
            assert "Erro ao carregar dados" in error_text.value
            assert error_text.color == COLORS["error"]
    
    async def test_load_chart_displays_chart_on_success(self, mock_page):
        """Test that load_chart displays native Flet chart on success"""
        chart_container = ft.Container()
        error_button = ft.Button("Retry")
        
        mock_data = [
            {
                "timestamp": "1700000000",
                "high": "5.10",
                "low": "5.00",
                "pctChange": "0.5"
            }
        ]
        
        with patch("pages.coins.fetch_usd_brl_data", new_callable=AsyncMock) as mock_fetch:
            mock_fetch.return_value = mock_data
            
            await load_chart(mock_page, chart_container, error_button, "400px")
            
            # Should display native chart
            assert chart_container.content is not None
            assert isinstance(chart_container.content, ft.Container)
            assert chart_container.content.expand is True
            assert chart_container.content.bgcolor == COLORS["surface"]
            assert chart_container.content.data["points"][0]["high"] == 5.10
    
    async def test_load_chart_displays_error_on_exception(self, mock_page):
        """Test that load_chart displays error message on exception"""
        chart_container = ft.Container()
        error_button = ft.Button("Retry")
        
        # Mock page.update to prevent errors
        mock_page.update = Mock()
        
        # The exception occurs after error_font_size is defined, so we need to
        # let fetch succeed first, then have create_chart fail
        mock_data = [{"timestamp": "1700000000", "high": "5.10", "low": "5.00", "pctChange": "0.5"}]
        
        with patch("pages.coins.fetch_usd_brl_data", new_callable=AsyncMock) as mock_fetch:
            with patch("pages.coins.create_chart") as mock_create:
                mock_fetch.return_value = mock_data
                mock_create.side_effect = Exception("Chart rendering error")
                
                await load_chart(mock_page, chart_container, error_button, "400px")
                
                # Should display error message
                assert isinstance(chart_container.content, ft.Column)
                error_column = chart_container.content
                
                error_text = error_column.controls[0]
                assert isinstance(error_text, ft.Text)
                assert "Erro inesperado" in error_text.value
                assert error_text.color == COLORS["error"]
    
    async def test_load_chart_displays_error_when_chart_creation_fails(self, mock_page):
        """Test that load_chart displays error when create_chart returns None"""
        chart_container = ft.Container()
        error_button = ft.Button("Retry")
        
        mock_data = [{"timestamp": "1700000000", "high": "5.10", "low": "5.00", "pctChange": "0.5"}]
        
        with patch("pages.coins.fetch_usd_brl_data", new_callable=AsyncMock) as mock_fetch:
            with patch("pages.coins.create_chart") as mock_create_chart:
                mock_fetch.return_value = mock_data
                mock_create_chart.return_value = None
                
                await load_chart(mock_page, chart_container, error_button, "400px")
                
                # Should display error message
                assert isinstance(chart_container.content, ft.Column)
                error_column = chart_container.content
                
                error_text = error_column.controls[0]
                assert isinstance(error_text, ft.Text)
                assert "Erro ao renderizar gráfico" in error_text.value
                assert error_text.color == COLORS["error"]
