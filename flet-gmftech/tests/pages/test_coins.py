"""
Unit tests for the market chart page.
"""

import base64
from datetime import datetime, timedelta
from unittest.mock import AsyncMock, Mock, patch

import flet as ft
import pytest

from pages.coins import (
    DEFAULT_FX_INPUT,
    DEFAULT_FX_SYMBOL,
    DEFAULT_FX_SYMBOLS,
    DEFAULT_MARKET,
    DEFAULT_PERIOD,
    FX_ASSETS,
    PAIR_EUR_BRL,
    PAIR_USD_BRL,
    _sample_stock_points,
    create_chart,
    currency_chart_content,
    fetch_chart_data,
    fetch_currency_data,
    fetch_fx_payloads,
    fetch_stock_payload,
    fetch_usd_brl_data,
    load_chart,
    normalize_fx_symbols,
)
from theme import COLORS


def market_column(result):
    return result.content


def toolbar(result):
    return market_column(result).controls[1]


def toolbar_row(result):
    return toolbar(result).content


def chart_container(result):
    return market_column(result).controls[3]


def sample_currency_data():
    return [
        {"timestamp": "1700000000", "bid": "5.00", "ask": "5.01", "high": "5.10", "low": "4.95", "pctChange": "0.5"},
        {"timestamp": "1700086400", "bid": "5.10", "ask": "5.11", "high": "5.20", "low": "5.00", "pctChange": "2.0"},
        {"timestamp": "1700172800", "bid": "5.05", "ask": "5.06", "high": "5.18", "low": "5.01", "pctChange": "-0.9"},
    ]


class TestCurrencyChartContent:
    def test_returns_valid_container(self, mock_page):
        result = currency_chart_content(mock_page)

        assert isinstance(result, ft.Container)
        assert result.expand is True
        assert isinstance(result.content, ft.Column)

    def test_has_market_toolbar(self, mock_page):
        result = currency_chart_content(mock_page)

        row = toolbar_row(result)
        market_selector = row.controls[0]
        fx_field = row.controls[1]
        stock_field = row.controls[2]
        period_selector = row.controls[4]

        assert isinstance(market_selector, ft.SegmentedButton)
        assert market_selector.selected == [DEFAULT_MARKET]
        assert isinstance(fx_field, ft.TextField)
        assert fx_field.value == DEFAULT_FX_INPUT
        assert isinstance(stock_field, ft.TextField)
        assert stock_field.visible is False
        assert isinstance(period_selector, ft.SegmentedButton)
        assert period_selector.selected == [DEFAULT_PERIOD]

    def test_has_investing_style_tabs(self, mock_page):
        result = currency_chart_content(mock_page)

        tabs = market_column(result).controls[0]
        labels = [button.content for button in tabs.controls if isinstance(button.content, str)]

        assert "Câmbio" in labels
        assert "Ações" in labels

    def test_has_chart_container_and_loading_state(self, mock_page):
        result = currency_chart_content(mock_page)

        chart = chart_container(result)
        assert isinstance(chart, ft.Container)
        assert chart.bgcolor == COLORS["surface"]
        assert chart.border_radius is not None
        assert chart.shadow is not None
        assert isinstance(chart.content, ft.Column)
        assert "Carregando" in chart.content.controls[0].value

    def test_mobile_chart_height(self, mobile_page):
        result = currency_chart_content(mobile_page)

        assert chart_container(result).height == 430

    def test_desktop_chart_height(self, desktop_page):
        result = currency_chart_content(desktop_page)

        assert chart_container(result).height == 610


class TestNormalizeFxSymbols:
    def test_default_symbols(self):
        assert normalize_fx_symbols("") == DEFAULT_FX_SYMBOLS

    def test_single_currency_becomes_brl_pair(self):
        assert normalize_fx_symbols("gbp") == ["GBP-BRL"]

    def test_pair_and_multiple_values(self):
        assert normalize_fx_symbols("brl/usd, eur-usd") == ["USD-BRL", "EUR-USD"]


class TestCreateChart:
    def test_create_chart_with_currency_data(self):
        result = create_chart(sample_currency_data(), "520px")

        assert result is not None
        decoded = base64.b64decode(result).decode("utf-8")
        assert "<!doctype html>" in decoded
        assert "echarts" in decoded
        assert "Volume" in decoded
        assert "resizeCharts" in decoded
        assert PAIR_USD_BRL in decoded

    def test_create_chart_with_stock_payload(self):
        payload = {
            "market": "STOCK",
            "symbol": "PETR4",
            "name": "PETR4",
            "currency": "BRL",
            "source": "demo",
            "points": _sample_stock_points("PETR4", "1M"),
        }

        result = create_chart(payload, "520px")

        decoded = base64.b64decode(result).decode("utf-8")
        assert "PETR4" in decoded
        assert "Volume" in decoded
        assert "Último" in decoded or "\\u00daltimo" in decoded

    def test_create_chart_with_three_currency_comparison(self):
        result = create_chart(
            {PAIR_USD_BRL: sample_currency_data(), PAIR_EUR_BRL: sample_currency_data()},
            "520px",
            view_key="ALL",
        )

        decoded = base64.b64decode(result).decode("utf-8")
        assert "Dólar" in decoded or "D\\u00f3lar" in decoded
        assert "Euro" in decoded
        assert "Real" in decoded

    def test_create_chart_with_empty_data(self):
        assert create_chart([], "520px") is None
        assert create_chart(None, "520px") is None


@pytest.mark.asyncio
class TestFetchCurrencyData:
    async def test_fetch_usd_brl_data_with_mocked_httpx(self):
        import pages.coins as coins_module

        coins_module._cached_data = {}
        coins_module._last_update = {}
        coins_module._is_fetching = {}

        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json = Mock(return_value=sample_currency_data())

            mock_client_instance = AsyncMock()
            mock_client_instance.get = AsyncMock(return_value=mock_response)
            mock_client_instance.__aenter__ = AsyncMock(return_value=mock_client_instance)
            mock_client_instance.__aexit__ = AsyncMock(return_value=None)
            mock_client.return_value = mock_client_instance

            result = await fetch_usd_brl_data(force_refresh=True)

        assert result == sample_currency_data()
        assert coins_module._cached_data[f"fx-raw:{PAIR_USD_BRL}:1M"] == sample_currency_data()

    async def test_currency_cache_prevents_refetch(self):
        import pages.coins as coins_module

        cached_data = sample_currency_data()
        coins_module._cached_data = {f"fx-raw:{PAIR_USD_BRL}:1M": cached_data}
        coins_module._last_update = {f"fx-raw:{PAIR_USD_BRL}:1M": datetime.now()}
        coins_module._is_fetching = {}

        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            result = await fetch_currency_data(PAIR_USD_BRL)

        assert result == cached_data
        mock_client.assert_not_called()

    async def test_currency_cache_expires(self):
        import pages.coins as coins_module

        old_key = f"fx-raw:{PAIR_USD_BRL}:1M"
        coins_module._cached_data = {old_key: [{"timestamp": "1", "bid": "4.9"}]}
        coins_module._last_update = {old_key: datetime.now() - timedelta(minutes=6)}
        coins_module._is_fetching = {}

        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json = Mock(return_value=sample_currency_data())

            mock_client_instance = AsyncMock()
            mock_client_instance.get = AsyncMock(return_value=mock_response)
            mock_client_instance.__aenter__ = AsyncMock(return_value=mock_client_instance)
            mock_client_instance.__aexit__ = AsyncMock(return_value=None)
            mock_client.return_value = mock_client_instance

            result = await fetch_currency_data(PAIR_USD_BRL)

        assert result == sample_currency_data()
        mock_client.assert_called_once()

    async def test_fetch_chart_data_returns_fx_payload(self):
        with patch("pages.coins.fetch_market_data", new_callable=AsyncMock) as mock_fetch:
            mock_fetch.return_value = {"market": "FX", "symbol": "FX_COMPARE", "series": []}

            result = await fetch_chart_data("ALL", force_refresh=True)

        assert result["symbol"] == "FX_COMPARE"
        mock_fetch.assert_called_once()

    async def test_fetch_fx_payloads_uses_typed_currency_list(self):
        payloads = [
            {"market": "FX", "symbol": "USD-BRL", "points": [{"close": 5}]},
            {"market": "FX", "symbol": "EUR-BRL", "points": [{"close": 6}]},
        ]

        async def fake_payload(symbol, period=DEFAULT_PERIOD, force_refresh=False):
            return payloads[0] if symbol == "USD-BRL" else payloads[1]

        with patch("pages.coins.fetch_fx_payload", new=fake_payload):
            result = await fetch_fx_payloads("usd, eur", DEFAULT_PERIOD, force_refresh=True)

        assert [payload["symbol"] for payload in result] == ["USD-BRL", "EUR-BRL"]


@pytest.mark.asyncio
class TestFetchStockPayload:
    async def test_fetch_stock_payload_with_brapi_shape(self):
        import pages.coins as coins_module

        coins_module._cached_data = {}
        coins_module._last_update = {}
        coins_module._is_fetching = {}

        brapi_data = {
            "results": [
                {
                    "symbol": "PETR4",
                    "shortName": "PETR4",
                    "currency": "BRL",
                    "historicalDataPrice": [
                        {"date": 1700000000, "open": 45.0, "high": 46.0, "low": 44.8, "close": 45.5, "volume": 1000000},
                        {"date": 1700086400, "open": 45.5, "high": 47.0, "low": 45.2, "close": 46.5, "volume": 1200000},
                    ],
                }
            ]
        }

        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json = Mock(return_value=brapi_data)

            mock_client_instance = AsyncMock()
            mock_client_instance.get = AsyncMock(return_value=mock_response)
            mock_client_instance.__aenter__ = AsyncMock(return_value=mock_client_instance)
            mock_client_instance.__aexit__ = AsyncMock(return_value=None)
            mock_client.return_value = mock_client_instance

            result = await fetch_stock_payload("PETR4", "1M", force_refresh=True)

        assert result["market"] == "STOCK"
        assert result["symbol"] == "PETR4"
        assert result["source"] == "brapi"
        assert len(result["points"]) == 2

    async def test_fetch_stock_payload_falls_back_to_demo(self):
        import pages.coins as coins_module

        coins_module._cached_data = {}
        coins_module._last_update = {}
        coins_module._is_fetching = {}

        with patch("pages.coins.httpx.AsyncClient") as mock_client:
            mock_response = Mock()
            mock_response.status_code = 500

            mock_client_instance = AsyncMock()
            mock_client_instance.get = AsyncMock(return_value=mock_response)
            mock_client_instance.__aenter__ = AsyncMock(return_value=mock_client_instance)
            mock_client_instance.__aexit__ = AsyncMock(return_value=None)
            mock_client.return_value = mock_client_instance

            result = await fetch_stock_payload("TEST3", "1M", force_refresh=True)

        assert result["market"] == "STOCK"
        assert result["source"] == "demo"
        assert result["points"]


@pytest.mark.asyncio
class TestLoadChart:
    async def test_load_chart_displays_webview_on_success(self, mock_page):
        payload = {
            "market": "STOCK",
            "symbol": "PETR4",
            "name": "PETR4",
            "currency": "BRL",
            "source": "demo",
            "points": _sample_stock_points("PETR4", "1M"),
        }
        chart = ft.Container()
        error_button = ft.Button("Retry")
        meta = ft.Text("")
        title = ft.Text("")

        with patch("pages.coins.fetch_market_data", new_callable=AsyncMock) as mock_fetch:
            mock_fetch.return_value = payload

            result = await load_chart(
                mock_page,
                chart,
                error_button,
                "520px",
                market="STOCK",
                symbol="PETR4",
                period="1M",
                meta_text=meta,
                title_text=title,
            )

        assert result == payload
        assert type(chart.content).__name__ == "WebView"
        assert chart.content.url.startswith("data:text/html;base64,")
        assert "PETR4" in meta.value
        assert title.value == "PETR4"

    async def test_load_chart_displays_error_without_data(self, mock_page):
        chart = ft.Container()
        error_button = ft.Button("Retry")

        with patch("pages.coins.fetch_fx_payloads", new_callable=AsyncMock) as mock_fetch:
            mock_fetch.return_value = []

            await load_chart(mock_page, chart, error_button, "520px")

        assert isinstance(chart.content, ft.Column)
        assert "Erro ao carregar dados" in chart.content.controls[0].value

    async def test_load_chart_displays_multiple_fx_charts(self, mock_page):
        chart = ft.Container()
        error_button = ft.Button("Retry")
        meta = ft.Text("")
        title = ft.Text("")
        payloads = [
            {
                "market": "FX",
                "symbol": "USD-BRL",
                "name": "Dólar / Real",
                "currency": "BRL",
                "source": "AwesomeAPI",
                "points": _sample_stock_points("USD", "1M"),
            },
            {
                "market": "FX",
                "symbol": "EUR-BRL",
                "name": "Euro / Real",
                "currency": "BRL",
                "source": "AwesomeAPI",
                "points": _sample_stock_points("EUR", "1M"),
            },
        ]

        with patch("pages.coins.fetch_fx_payloads", new_callable=AsyncMock) as mock_fetch:
            mock_fetch.return_value = payloads

            result = await load_chart(
                mock_page,
                chart,
                error_button,
                "520px",
                market="FX",
                symbol="USD, EUR",
                period="1M",
                meta_text=meta,
                title_text=title,
            )

        assert result == payloads
        assert isinstance(chart.content, ft.Column)
        assert "USD-BRL" in meta.value
        assert "EUR-BRL" in meta.value
        assert title.value == "Gráficos Múltiplos de Moedas"
