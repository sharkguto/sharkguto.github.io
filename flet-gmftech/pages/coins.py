#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# coins.py
# @Author : Gustavo (gustavo@gmf-tech.com)

import asyncio
import base64
import math
import re
from datetime import datetime, timedelta

import flet as ft
from flet_webview import WebView
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line
from pyecharts.globals import ThemeType

from theme import COLORS, get_responsive_font_size, get_responsive_padding, get_shadow
from utils.responsive import ResponsiveConfig

try:
    import pyodide
    from pyodide.http import pyfetch

    IS_PYODIDE = True
except ImportError:
    IS_PYODIDE = False
    import httpx


PAIR_USD_BRL = "USD-BRL"
PAIR_EUR_BRL = "EUR-BRL"
DEFAULT_MARKET = "FX"
DEFAULT_FX_SYMBOL = PAIR_USD_BRL
DEFAULT_FX_INPUT = "USD, BRL"
DEFAULT_FX_SYMBOLS = [PAIR_USD_BRL]
DEFAULT_STOCK_SYMBOL = "PETR4"
DEFAULT_PERIOD = "1M"
DEFAULT_VIEW = "BRL_USD"

MARKETS = {
    "FX": "Câmbio",
    "STOCK": "Ações",
}

PERIODS = {
    "5D": {"label": "5D", "points": 5, "brapi_range": "5d"},
    "1M": {"label": "1M", "points": 22, "brapi_range": "1mo"},
    "3M": {"label": "3M", "points": 66, "brapi_range": "3mo"},
    "6M": {"label": "6M", "points": 132, "brapi_range": "6mo"},
    "1A": {"label": "1A", "points": 252, "brapi_range": "1y"},
}

FX_ASSETS = {
    "USD-BRL": "Dólar / Real",
    "EUR-BRL": "Euro / Real",
    "USD-EUR": "Dólar / Euro",
    "EUR-USD": "Euro / Dólar",
    "GBP-BRL": "Libra / Real",
    "FX_COMPARE": "Dólar, Euro e Real",
}

CHART_VIEWS = {
    "BRL_USD": {"symbol": "USD-BRL", "label": "Real x Dólar"},
    "BRL_EUR": {"symbol": "EUR-BRL", "label": "Real x Euro"},
    "USD_EUR": {"symbol": "USD-EUR", "label": "Dólar x Euro"},
    "ALL": {"symbol": "FX_COMPARE", "label": "Comparar 3"},
}

_cached_data = {}
_last_update = {}
_is_fetching = {}


def _ensure_cache_maps():
    global _cached_data, _last_update, _is_fetching

    if isinstance(_cached_data, list):
        _cached_data = {f"fx:{PAIR_USD_BRL}:{DEFAULT_PERIOD}": _cached_data}
    elif not isinstance(_cached_data, dict):
        _cached_data = {}

    if isinstance(_last_update, datetime):
        _last_update = {f"fx:{PAIR_USD_BRL}:{DEFAULT_PERIOD}": _last_update}
    elif not isinstance(_last_update, dict):
        _last_update = {}

    if not isinstance(_is_fetching, dict):
        _is_fetching = {}


async def preload_data():
    try:
        await fetch_market_data(DEFAULT_MARKET, DEFAULT_FX_SYMBOL, DEFAULT_PERIOD, force_refresh=True)
    except Exception:
        pass


async def _fetch_json(url):
    if IS_PYODIDE:
        response = await pyfetch(url, method="GET")
        if response.status == 200:
            return await response.json()
        return None

    async with httpx.AsyncClient(timeout=8.0) as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()
    return None


async def _get_cached(key, fetcher, force_refresh=False):
    _ensure_cache_maps()

    while _is_fetching.get(key, False):
        await asyncio.sleep(0.1)

    now = datetime.now()
    if not force_refresh and key in _cached_data and key in _last_update:
        if (now - _last_update[key]).total_seconds() < 300:
            return _cached_data[key]

    _is_fetching[key] = True
    try:
        try:
            data = await fetcher()
        except Exception:
            data = None
        if data:
            _cached_data[key] = data
            _last_update[key] = now
            return data
        return _cached_data.get(key)
    finally:
        _is_fetching[key] = False


def _period_config(period):
    return PERIODS.get(period, PERIODS[DEFAULT_PERIOD])


async def fetch_currency_data(pair=PAIR_USD_BRL, force_refresh=False, period=DEFAULT_PERIOD):
    pair = pair.upper()
    points = _period_config(period)["points"]
    key = f"fx-raw:{pair}:{period}"

    async def fetcher():
        return await _fetch_json(f"https://economia.awesomeapi.com.br/json/daily/{pair}/{points}")

    data = await _get_cached(key, fetcher, force_refresh=force_refresh)
    return data or []


async def fetch_usd_brl_data(force_refresh=False):
    return await fetch_currency_data(PAIR_USD_BRL, force_refresh=force_refresh)


def normalize_fx_symbols(value):
    text = (value or DEFAULT_FX_INPUT).upper().strip()
    if not text:
        return DEFAULT_FX_SYMBOLS.copy()

    symbols = []
    for token in re.split(r"[,;\s]+", text):
        token = token.strip().replace("_", "-")
        if not token:
            continue

        if token in ("COMPARE", "COMPARAR", "3", "FX_COMPARE"):
            symbols.append("FX_COMPARE")
            continue

        parts = [part for part in re.split(r"[-/X]+", token) if part]
        if len(parts) >= 2:
            base, quote = parts[0], parts[1]
            if base == "BRL" and quote != "BRL":
                symbol = f"{quote}-BRL"
            elif quote == "BRL" or base != "BRL":
                symbol = f"{base}-{quote}"
            else:
                continue
        else:
            base = parts[0] if parts else token
            if base == "BRL":
                continue
            symbol = f"{base}-BRL"

        if symbol not in symbols:
            symbols.append(symbol)

    return (symbols or DEFAULT_FX_SYMBOLS.copy())[:4]


def _safe_float(entry, *keys, default=None):
    for key in keys:
        value = entry.get(key)
        if value in (None, ""):
            continue
        try:
            return float(value)
        except (TypeError, ValueError):
            continue
    return default


def _currency_points(data):
    points = []
    previous_close = None
    for entry in (data or [])[::-1]:
        try:
            timestamp = int(entry["timestamp"])
            date = datetime.fromtimestamp(timestamp).strftime("%d/%m")
        except (KeyError, TypeError, ValueError, OSError):
            continue

        close = _safe_float(entry, "bid", "ask")
        high = _safe_float(entry, "high", default=close)
        low = _safe_float(entry, "low", default=close)
        open_value = _safe_float(entry, "open", default=previous_close or close)
        pct = _safe_float(entry, "pctChange", default=0.0)

        if close is None:
            continue

        points.append(
            {
                "date": date,
                "timestamp": timestamp,
                "open": round(open_value if open_value is not None else close, 4),
                "high": round(high if high is not None else close, 4),
                "low": round(low if low is not None else close, 4),
                "close": round(close, 4),
                "volume": int(max(abs(pct), 0.18) * 1_250_000),
                "pct": round(pct, 2),
            }
        )
        previous_close = close
    return points


def _stock_points_from_brapi(data):
    result = ((data or {}).get("results") or [{}])[0]
    points = []
    for entry in result.get("historicalDataPrice") or []:
        timestamp = entry.get("date")
        if timestamp is None:
            continue
        try:
            date = datetime.fromtimestamp(int(timestamp)).strftime("%d/%m")
        except (TypeError, ValueError, OSError):
            continue

        close = _safe_float(entry, "close", "adjustedClose")
        if close is None:
            continue

        open_value = _safe_float(entry, "open", default=close)
        high = _safe_float(entry, "high", default=max(open_value, close))
        low = _safe_float(entry, "low", default=min(open_value, close))
        volume = int(_safe_float(entry, "volume", default=0) or 0)
        previous = points[-1]["close"] if points else close
        pct = ((close - previous) / previous * 100) if previous else 0

        points.append(
            {
                "date": date,
                "timestamp": int(timestamp),
                "open": round(open_value, 4),
                "high": round(high, 4),
                "low": round(low, 4),
                "close": round(close, 4),
                "volume": volume,
                "pct": round(pct, 2),
            }
        )
    return points


def _sample_stock_points(symbol, period):
    points = []
    count = min(_period_config(period)["points"], 80)
    seed = sum(ord(char) for char in symbol.upper()) or 1
    base = 24 + (seed % 45)
    current = datetime.now() - timedelta(days=count * 1.5)
    price = float(base)

    while len(points) < count:
        current += timedelta(days=1)
        if current.weekday() >= 5:
            continue

        wave = math.sin((len(points) + seed % 9) / 3) * 0.55
        drift = ((seed % 11) - 5) * 0.015
        open_value = price
        close = max(1.0, open_value + wave + drift)
        high = max(open_value, close) + 0.35 + (len(points) % 4) * 0.07
        low = min(open_value, close) - 0.28
        volume = int((1_800_000 + (seed % 19) * 120_000) * (1 + abs(close - open_value) / 8))
        pct = ((close - open_value) / open_value * 100) if open_value else 0

        points.append(
            {
                "date": current.strftime("%d/%m"),
                "timestamp": int(current.timestamp()),
                "open": round(open_value, 2),
                "high": round(high, 2),
                "low": round(low, 2),
                "close": round(close, 2),
                "volume": volume,
                "pct": round(pct, 2),
            }
        )
        price = close
    return points


async def fetch_stock_payload(symbol=DEFAULT_STOCK_SYMBOL, period=DEFAULT_PERIOD, force_refresh=False):
    symbol = (symbol or DEFAULT_STOCK_SYMBOL).strip().upper()
    key = f"stock:{symbol}:{period}"
    brapi_range = _period_config(period)["brapi_range"]

    async def fetcher():
        data = await _fetch_json(
            f"https://brapi.dev/api/quote/{symbol}?range={brapi_range}&interval=1d"
        )
        result = ((data or {}).get("results") or [{}])[0]
        points = _stock_points_from_brapi(data)
        if not points:
            return None
        return {
            "market": "STOCK",
            "symbol": result.get("symbol") or symbol,
            "name": result.get("shortName") or result.get("longName") or symbol,
            "currency": result.get("currency") or "BRL",
            "source": "brapi",
            "points": points,
        }

    payload = await _get_cached(key, fetcher, force_refresh=force_refresh)
    if payload:
        return payload

    return {
        "market": "STOCK",
        "symbol": symbol,
        "name": f"{symbol} - série demonstrativa",
        "currency": "BRL",
        "source": "demo",
        "points": _sample_stock_points(symbol, period),
    }


def _market_payload(market, symbol, name, currency, points, source):
    return {
        "market": market,
        "symbol": symbol,
        "name": name,
        "currency": currency,
        "source": source,
        "points": points,
    }


def _align_points(*series):
    common_dates = set(point["date"] for point in series[0])
    for points in series[1:]:
        common_dates &= set(point["date"] for point in points)
    ordered_dates = [point["date"] for point in series[0] if point["date"] in common_dates]
    aligned = []
    for points in series:
        by_date = {point["date"]: point for point in points}
        aligned.append([by_date[date] for date in ordered_dates])
    return ordered_dates, aligned


async def fetch_fx_payload(symbol=DEFAULT_FX_SYMBOL, period=DEFAULT_PERIOD, force_refresh=False):
    symbol = (symbol or DEFAULT_FX_SYMBOL).upper()

    if symbol == "FX_COMPARE":
        usd_raw, eur_raw = await asyncio.gather(
            fetch_currency_data(PAIR_USD_BRL, force_refresh=force_refresh, period=period),
            fetch_currency_data(PAIR_EUR_BRL, force_refresh=force_refresh, period=period),
        )
        usd_points = _currency_points(usd_raw)
        eur_points = _currency_points(eur_raw)
        dates, (usd_aligned, eur_aligned) = _align_points(usd_points, eur_points)
        brl_points = [
            {
                "date": date,
                "timestamp": usd_aligned[index]["timestamp"],
                "open": 1.0,
                "high": 1.0,
                "low": 1.0,
                "close": 1.0,
                "volume": 0,
                "pct": 0.0,
            }
            for index, date in enumerate(dates)
        ]
        return {
            "market": "FX",
            "symbol": "FX_COMPARE",
            "name": FX_ASSETS["FX_COMPARE"],
            "currency": "BRL",
            "source": "AwesomeAPI",
            "series": [
                {"name": "Dólar (USD)", "color": "#62A8F7", "points": usd_aligned},
                {"name": "Euro (EUR)", "color": COLORS["coral"], "points": eur_aligned},
                {"name": "Real (BRL)", "color": COLORS["primary"], "points": brl_points},
            ],
        }

    raw = await fetch_currency_data(symbol, force_refresh=force_refresh, period=period)
    name = (raw[0].get("name") if raw else None) or FX_ASSETS.get(symbol, symbol)
    currency = symbol.split("-")[-1] if "-" in symbol else "BRL"
    return _market_payload("FX", symbol, name, currency, _currency_points(raw), "AwesomeAPI")


async def fetch_fx_payloads(value=DEFAULT_FX_INPUT, period=DEFAULT_PERIOD, force_refresh=False):
    symbols = normalize_fx_symbols(value)
    payloads = await asyncio.gather(
        *[
            fetch_fx_payload(symbol, period=period, force_refresh=force_refresh)
            for symbol in symbols
        ]
    )
    return [
        payload
        for payload in payloads
        if payload.get("points") or payload.get("series")
    ]


async def fetch_market_data(market=DEFAULT_MARKET, symbol=DEFAULT_FX_SYMBOL, period=DEFAULT_PERIOD, force_refresh=False):
    if market == "STOCK":
        return await fetch_stock_payload(symbol, period, force_refresh=force_refresh)
    return await fetch_fx_payload(symbol, period, force_refresh=force_refresh)


async def fetch_chart_data(view_key=DEFAULT_VIEW, force_refresh=False):
    symbol = CHART_VIEWS.get(view_key, CHART_VIEWS[DEFAULT_VIEW])["symbol"]
    return await fetch_market_data("FX", symbol, DEFAULT_PERIOD, force_refresh=force_refresh)


def _format_price(value, currency="BRL"):
    if value is None:
        return "-"
    precision = 4 if abs(value) < 10 else 2
    prefix = "R$ " if currency == "BRL" else ("US$ " if currency == "USD" else ("€ " if currency == "EUR" else ""))
    return f"{prefix}{value:.{precision}f}"


def _format_volume(value):
    value = value or 0
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"
    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"
    if value >= 1_000:
        return f"{value / 1_000:.1f}K"
    return str(int(value))


def _latest_point(payload):
    points = payload.get("points") or []
    return points[-1] if points else None


def _summary_text(payload):
    if payload.get("series"):
        return f"{payload['symbol']} • {payload['name']} • {payload['source']}"

    point = _latest_point(payload)
    if not point:
        return f"{payload.get('symbol', '')} • sem dados"

    status = "Demonstração" if payload.get("source") == "demo" else "Mercado"
    return (
        f"{payload['symbol']} • Abr {_format_price(point['open'], payload['currency'])}  "
        f"Max {_format_price(point['high'], payload['currency'])}  "
        f"Min {_format_price(point['low'], payload['currency'])}  "
        f"Fch {_format_price(point['close'], payload['currency'])}  "
        f"Vol {_format_volume(point['volume'])} • {status}"
    )


def _display_fx_title(symbol):
    if symbol == "FX_COMPARE":
        return FX_ASSETS[symbol]
    parts = symbol.split("-")
    if len(parts) == 2 and parts[1] == "BRL":
        return f"BRL x {parts[0]}"
    if len(parts) == 2:
        return f"{parts[0]} x {parts[1]}"
    return symbol


def _bar_items(points):
    items = []
    for point in points:
        color = "#71E3B6" if point["close"] >= point["open"] else "#FF9B9B"
        items.append(
            opts.BarItem(
                name=point["date"],
                value=point["volume"],
                itemstyle_opts=opts.ItemStyleOpts(color=color, opacity=0.72),
            )
        )
    return items


def _chart_shell_html(chart):
    html = f"""
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            background: {COLORS["surface"]};
            font-family: Roboto, Arial, sans-serif;
        }}
        body > div {{
            width: 100% !important;
            height: 100% !important;
        }}
        canvas {{
            max-width: 100%;
        }}
    </style>
</head>
<body>
    {chart.render_embed()}
    <script>
        (function () {{
            function resizeCharts() {{
                if (!window.echarts) return;
                document.querySelectorAll("div[_echarts_instance_]").forEach(function (element) {{
                    var chart = window.echarts.getInstanceByDom(element);
                    if (chart) chart.resize();
                }});
            }}
            window.addEventListener("resize", resizeCharts);
            if (window.ResizeObserver) {{
                new ResizeObserver(resizeCharts).observe(document.body);
            }}
            setTimeout(resizeCharts, 120);
            setTimeout(resizeCharts, 600);
        }})();
    </script>
</body>
</html>
"""
    return base64.b64encode(html.encode("utf-8")).decode("utf-8")


def _create_compare_chart(payload, chart_height, chart_width=1024):
    is_mobile = chart_width <= ResponsiveConfig.MOBILE_MAX
    series = payload.get("series") or []
    if not series or not series[0]["points"]:
        return None

    dates = [point["date"] for point in series[0]["points"]]
    line = Line(
        init_opts=opts.InitOpts(
            width="100%",
            height=chart_height,
            theme=ThemeType.LIGHT,
            bg_color=COLORS["surface"],
            animation_opts=opts.AnimationOpts(animation=False),
            js_host="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/",
        )
    ).add_xaxis(dates)

    for item in series:
        line.add_yaxis(
            item["name"],
            [point["close"] for point in item["points"]],
            color=item["color"],
            is_smooth=True,
            symbol_size=5,
            linestyle_opts=opts.LineStyleOpts(width=3, color=item["color"]),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.06, color=item["color"]),
            label_opts=opts.LabelOpts(is_show=False),
        )

    line.set_global_opts(
        title_opts=opts.TitleOpts(
            title=f"{payload['name']} • D",
            subtitle=_summary_text(payload),
            pos_left="1%",
            pos_top="1%",
            title_textstyle_opts=opts.TextStyleOpts(font_size=14 if is_mobile else 16, color=COLORS["text_primary"]),
            subtitle_textstyle_opts=opts.TextStyleOpts(font_size=10 if is_mobile else 12, color=COLORS["text_secondary"]),
        ),
        legend_opts=opts.LegendOpts(type_="scroll", pos_top="12%", pos_left="center"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross", is_confine=True),
        xaxis_opts=opts.AxisOpts(
            boundary_gap=False,
            axislabel_opts=opts.LabelOpts(rotate=35 if is_mobile else 0, color=COLORS["text_secondary"]),
        ),
        yaxis_opts=opts.AxisOpts(
            is_scale=True,
            position="right",
            axislabel_opts=opts.LabelOpts(color=COLORS["text_secondary"]),
            splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=0.18)),
        ),
        datazoom_opts=[
            opts.DataZoomOpts(type_="inside", range_start=0, range_end=100),
            opts.DataZoomOpts(type_="slider", range_start=0, range_end=100, height=16, pos_bottom="1%"),
        ],
    )
    line.options["grid"] = opts.GridOpts(
        pos_left="4%",
        pos_right="6%",
        pos_top="22%" if is_mobile else "18%",
        pos_bottom="15%",
        is_contain_label=True,
    ).opts
    return line


def _create_market_chart(payload, chart_height, chart_width=1024):
    if payload.get("series"):
        return _create_compare_chart(payload, chart_height, chart_width)

    points = payload.get("points") or []
    if not points:
        return None

    is_mobile = chart_width <= ResponsiveConfig.MOBILE_MAX
    dates = [point["date"] for point in points]
    closes = [point["close"] for point in points]
    line_color = "#7DBCF5"
    latest = points[-1]

    line = (
        Line()
        .add_xaxis(dates)
        .add_yaxis(
            payload["symbol"],
            closes,
            color=line_color,
            is_smooth=True,
            symbol_size=4 if is_mobile else 6,
            linestyle_opts=opts.LineStyleOpts(width=2.6, color=line_color),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.25, color="#BFE4FF"),
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(y=latest["close"], name="Último")],
                symbol="none",
                linestyle_opts=opts.LineStyleOpts(type_="dotted", color="#336DFF", opacity=0.75),
                label_opts=opts.LabelOpts(position="end", color="#336DFF"),
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=f"{payload['symbol']} • D",
                subtitle=_summary_text(payload),
                pos_left="1%",
                pos_top="1%",
                title_textstyle_opts=opts.TextStyleOpts(font_size=14 if is_mobile else 16, color=COLORS["text_primary"]),
                subtitle_textstyle_opts=opts.TextStyleOpts(font_size=10 if is_mobile else 12, color=COLORS["text_secondary"]),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(
                trigger="axis",
                axis_pointer_type="cross",
                is_confine=True,
                background_color="rgba(7, 27, 44, 0.92)",
                border_width=0,
                textstyle_opts=opts.TextStyleOpts(color="#FFFFFF", font_size=11 if is_mobile else 12),
            ),
            toolbox_opts=opts.ToolboxOpts(is_show=not is_mobile, pos_right="2%", pos_top="1%"),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(is_show=False),
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color=COLORS["muted"])),
            ),
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                position="right",
                axislabel_opts=opts.LabelOpts(color=COLORS["text_secondary"]),
                splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=0.16)),
            ),
            datazoom_opts=[
                opts.DataZoomOpts(type_="inside", range_start=0, range_end=100, xaxis_index=[0, 1]),
                opts.DataZoomOpts(type_="slider", range_start=0, range_end=100, height=16, pos_bottom="0%", xaxis_index=[0, 1]),
            ],
        )
    )

    bar = (
        Bar()
        .add_xaxis(dates)
        .add_yaxis(
            "Volume",
            _bar_items(points),
            bar_width="55%",
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            tooltip_opts=opts.TooltipOpts(trigger="axis", is_confine=True),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=True,
                axislabel_opts=opts.LabelOpts(rotate=35 if is_mobile else 0, color=COLORS["text_secondary"]),
                axisline_opts=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color=COLORS["muted"])),
            ),
            yaxis_opts=opts.AxisOpts(
                position="right",
                axislabel_opts=opts.LabelOpts(color=COLORS["text_secondary"]),
                splitline_opts=opts.SplitLineOpts(is_show=False),
            ),
        )
    )

    grid = Grid(
        init_opts=opts.InitOpts(
            width="100%",
            height=chart_height,
            theme=ThemeType.LIGHT,
            bg_color=COLORS["surface"],
            animation_opts=opts.AnimationOpts(animation=False),
            js_host="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/",
        )
    )
    grid.add(
        line,
        grid_opts=opts.GridOpts(
            pos_left="4%",
            pos_right="6%",
            pos_top="18%" if is_mobile else "15%",
            height="56%" if is_mobile else "60%",
            is_contain_label=True,
        ),
    )
    grid.add(
        bar,
        grid_opts=opts.GridOpts(
            pos_left="4%",
            pos_right="6%",
            pos_top="78%",
            height="13%",
            is_contain_label=True,
        ),
        is_control_axis_index=True,
    )
    return grid


def _chart_webview(payload, chart_height, chart_width):
    encoded_html = create_chart(payload, chart_height, chart_width=chart_width)
    if not encoded_html:
        return None
    return WebView(
        url=f"data:text/html;base64,{encoded_html}",
        expand=True,
        bgcolor=COLORS["surface"],
        visible=True,
    )


def _fx_chart_card(payload, chart_height, chart_width):
    webview = _chart_webview(payload, chart_height, chart_width)
    if not webview:
        return None

    return ft.Container(
        content=webview,
        expand=True,
        height=chart_height,
        bgcolor=COLORS["surface"],
        border_radius=ft.BorderRadius.all(6),
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )


def _build_fx_grid(payloads, chart_height, chart_width):
    if not payloads:
        return None

    is_mobile = chart_width <= ResponsiveConfig.MOBILE_MAX
    if len(payloads) == 1:
        return _chart_webview(payloads[0], f"{chart_height}px", chart_width)

    card_height = chart_height if len(payloads) <= 2 and not is_mobile else max(320, min(430, chart_height // 2))
    cards = [
        _fx_chart_card(payload, f"{card_height}px", chart_width)
        for payload in payloads
    ]
    cards = [card for card in cards if card]
    if not cards:
        return None

    if is_mobile:
        return ft.Column(
            cards,
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

    rows = []
    for index in range(0, len(cards), 2):
        rows.append(
            ft.Row(
                cards[index:index + 2],
                spacing=10,
                expand=len(payloads) <= 2,
                vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            )
        )
    return ft.Column(
        rows,
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )


def create_chart(data, chart_height="520px", view_key=None, chart_width=1024):
    if not data:
        return None

    if isinstance(data, list):
        payload = _market_payload("FX", PAIR_USD_BRL, FX_ASSETS[PAIR_USD_BRL], "BRL", _currency_points(data), "AwesomeAPI")
    elif "points" in data or "series" in data:
        payload = data
    elif PAIR_USD_BRL in data or PAIR_EUR_BRL in data:
        if view_key == "ALL":
            usd_points = _currency_points(data.get(PAIR_USD_BRL, []))
            eur_points = _currency_points(data.get(PAIR_EUR_BRL, []))
            dates, (usd_aligned, eur_aligned) = _align_points(usd_points, eur_points)
            payload = {
                "market": "FX",
                "symbol": "FX_COMPARE",
                "name": FX_ASSETS["FX_COMPARE"],
                "currency": "BRL",
                "source": "AwesomeAPI",
                "series": [
                    {"name": "Dólar (USD)", "color": "#62A8F7", "points": usd_aligned},
                    {"name": "Euro (EUR)", "color": COLORS["coral"], "points": eur_aligned},
                    {
                        "name": "Real (BRL)",
                        "color": COLORS["primary"],
                        "points": [
                            {**usd_aligned[index], "open": 1.0, "high": 1.0, "low": 1.0, "close": 1.0, "volume": 0, "pct": 0.0}
                            for index, _date in enumerate(dates)
                        ],
                    },
                ],
            }
        else:
            payload = _market_payload("FX", PAIR_USD_BRL, FX_ASSETS[PAIR_USD_BRL], "BRL", _currency_points(data.get(PAIR_USD_BRL, [])), "AwesomeAPI")
    else:
        return None

    chart = _create_market_chart(payload, chart_height, chart_width)
    return _chart_shell_html(chart) if chart else None


def _loading_content(width):
    return ft.Column(
        [
            ft.Text(
                "Carregando mercado...",
                color=COLORS["text_secondary"],
                font_family="Roboto",
                size=get_responsive_font_size(15, width),
                text_align="center",
            ),
            ft.ProgressRing(width=32, height=32, stroke_width=4, color=COLORS["primary"]),
        ],
        alignment="center",
        horizontal_alignment="center",
        expand=True,
    )


def _error_content(message, error_button, width):
    return ft.Column(
        [
            ft.Text(
                message,
                color=COLORS["error"],
                size=get_responsive_font_size(15, width),
                font_family="Roboto",
                text_align="center",
            ),
            error_button,
        ],
        alignment="center",
        horizontal_alignment="center",
        spacing=20,
    )


async def load_chart(
    page,
    chart_container,
    error_button,
    chart_height,
    market=DEFAULT_MARKET,
    symbol=DEFAULT_FX_SYMBOL,
    period=DEFAULT_PERIOD,
    meta_text=None,
    title_text=None,
    force_refresh=False,
):
    width = page.width if page.width else 1024

    try:
        if market == "FX":
            payloads = await fetch_fx_payloads(symbol, period, force_refresh=force_refresh)
            if not payloads:
                chart_container.content = _error_content("Erro ao carregar dados", error_button, width)
                page.update()
                return None

            chart_content = _build_fx_grid(payloads, int(str(chart_height).replace("px", "")), width)
            if not chart_content:
                chart_container.content = _error_content("Erro ao renderizar gráfico", error_button, width)
                page.update()
                return None

            chart_container.content = chart_content
            symbols = [payload["symbol"] for payload in payloads]
            if title_text:
                title_text.value = "Gráficos Múltiplos de Moedas"
            if meta_text:
                meta_text.value = f"Câmbio • {', '.join(symbols)} • {period}"
            page.update()
            return payloads

        payload = await fetch_market_data(market, symbol, period, force_refresh=force_refresh)
        if not payload.get("points") and not payload.get("series"):
            chart_container.content = _error_content("Erro ao carregar dados", error_button, width)
            page.update()
            return None

        encoded_html = create_chart(payload, chart_height, chart_width=width)
        if not encoded_html:
            chart_container.content = _error_content("Erro ao renderizar gráfico", error_button, width)
            page.update()
            return None

        chart_container.content = WebView(
            url=f"data:text/html;base64,{encoded_html}",
            expand=True,
            bgcolor=COLORS["surface"],
            visible=True,
        )
        if title_text:
            title_text.value = payload["name"]
        if meta_text:
            meta_text.value = _summary_text(payload)
        page.update()
        return payload
    except Exception as exc:
        chart_container.content = _error_content(f"Erro inesperado: {str(exc)}", error_button, width)
        page.update()
        return None


def _market_button_style():
    return ft.ButtonStyle(
        padding=ft.Padding.symmetric(horizontal=12, vertical=10),
        shape=ft.RoundedRectangleBorder(radius=6),
    )


def currency_chart_content(page: ft.Page):
    width = page.width if page.width else 1024
    breakpoint = ResponsiveConfig.get_breakpoint(width)
    is_mobile = width <= ResponsiveConfig.MOBILE_MAX

    horizontal_padding = get_responsive_padding(28, width)
    panel_padding = get_responsive_padding(12, width)
    spacing = get_responsive_padding(12, width)
    chart_heights = {
        ResponsiveConfig.get_breakpoint(400): 430,
        ResponsiveConfig.get_breakpoint(768): 520,
        ResponsiveConfig.get_breakpoint(1920): 610,
    }
    chart_height = chart_heights.get(breakpoint, 520)
    chart_height_str = f"{chart_height}px"
    state = {
        "market": DEFAULT_MARKET,
        "fx_symbol": DEFAULT_FX_INPUT,
        "stock_symbol": DEFAULT_STOCK_SYMBOL,
        "period": DEFAULT_PERIOD,
    }

    title_text = ft.Text(
        "Gráficos Múltiplos de Moedas",
        size=get_responsive_font_size(24, width),
        weight="bold",
        color=COLORS["text_primary"],
    )
    meta_text = ft.Text(
        "Câmbio • USD-BRL • 1M",
        size=get_responsive_font_size(13, width),
        color=COLORS["text_secondary"],
    )

    error_button = ft.Button(
        "Tentar novamente",
        icon=ft.Icons.REFRESH,
        bgcolor=COLORS["primary"],
        color=ft.Colors.WHITE,
    )

    chart_container = ft.Container(
        expand=True,
        bgcolor=COLORS["surface"],
        border_radius=ft.BorderRadius.all(8),
        shadow=get_shadow(),
        padding=0,
        height=chart_height,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )
    chart_container.content = _loading_content(width)

    market_selector = ft.SegmentedButton(
        segments=[
            ft.Segment(value="FX", icon=ft.Icons.CURRENCY_EXCHANGE, label=ft.Text("Câmbio")),
            ft.Segment(value="STOCK", icon=ft.Icons.CANDLESTICK_CHART, label=ft.Text("Ações")),
        ],
        selected=[DEFAULT_MARKET],
        show_selected_icon=False,
        allow_empty_selection=False,
    )

    fx_field = ft.TextField(
        value=DEFAULT_FX_INPUT,
        dense=True,
        width=250 if not is_mobile else 260,
        prefix_icon=ft.Icons.CURRENCY_EXCHANGE,
        hint_text="USD, BRL, EUR ou USD/EUR",
        bgcolor=COLORS["surface"],
        border_radius=6,
        content_padding=ft.Padding.symmetric(horizontal=10, vertical=8),
    )

    stock_field = ft.TextField(
        value=DEFAULT_STOCK_SYMBOL,
        dense=True,
        width=150 if not is_mobile else 180,
        prefix_icon=ft.Icons.SEARCH,
        border_radius=6,
        bgcolor=COLORS["surface"],
        content_padding=ft.Padding.symmetric(horizontal=10, vertical=8),
        visible=False,
    )

    period_selector = ft.SegmentedButton(
        segments=[
            ft.Segment(value=key, label=ft.Text(config["label"]))
            for key, config in PERIODS.items()
        ],
        selected=[DEFAULT_PERIOD],
        show_selected_icon=False,
        allow_empty_selection=False,
    )

    async def refresh_chart(force_refresh=False):
        market = state["market"]
        symbol = (fx_field.value or DEFAULT_FX_INPUT).strip() if market == "FX" else (stock_field.value or DEFAULT_STOCK_SYMBOL).strip().upper()
        if market == "FX":
            state["fx_symbol"] = symbol
        if market == "STOCK":
            state["stock_symbol"] = symbol
            stock_field.value = symbol
        chart_container.content = _loading_content(width)
        title_text.value = MARKETS[market]
        meta_text.value = f"{MARKETS[market]} • {symbol} • {state['period']}"
        page.update()
        await load_chart(
            page,
            chart_container,
            error_button,
            chart_height_str,
            market=market,
            symbol=symbol,
            period=state["period"],
            meta_text=meta_text,
            title_text=title_text,
            force_refresh=force_refresh,
        )

    async def set_market(market):
        state["market"] = market if market in MARKETS else DEFAULT_MARKET
        market_selector.selected = [state["market"]]
        fx_field.visible = state["market"] == "FX"
        stock_field.visible = state["market"] == "STOCK"
        page.update()
        await refresh_chart()

    async def handle_market_change(e):
        selected = list(e.control.selected or [DEFAULT_MARKET])
        await set_market(selected[0])

    def market_tab_handler(market):
        async def handler(e):
            await set_market(market)
        return handler

    async def handle_fx_submit(e):
        await refresh_chart(force_refresh=True)

    async def handle_period_change(e):
        selected = list(e.control.selected or [DEFAULT_PERIOD])
        state["period"] = selected[0]
        await refresh_chart()

    async def handle_stock_submit(e):
        await refresh_chart(force_refresh=True)

    async def handle_retry(e):
        await refresh_chart(force_refresh=True)

    market_selector.on_change = handle_market_change
    fx_field.on_submit = handle_fx_submit
    stock_field.on_submit = handle_stock_submit
    period_selector.on_change = handle_period_change
    error_button.on_click = handle_retry

    search_button = ft.IconButton(
        icon=ft.Icons.SEARCH,
        tooltip="Buscar ativo",
        icon_color=COLORS["primary"],
        bgcolor=COLORS["surface"],
        on_click=handle_stock_submit,
    )
    refresh_button = ft.IconButton(
        icon=ft.Icons.REFRESH,
        tooltip="Atualizar",
        icon_color=COLORS["primary"],
        bgcolor=COLORS["surface"],
        on_click=handle_retry,
    )

    toolbar = ft.Container(
        content=ft.Row(
            [
                market_selector,
                fx_field,
                stock_field,
                search_button,
                period_selector,
                refresh_button,
            ],
            wrap=True,
            spacing=8,
            run_spacing=8,
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        bgcolor=COLORS["surface_alt"],
        border_radius=ft.BorderRadius.all(8),
        padding=panel_padding,
    )

    page.run_task(refresh_chart)

    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.TextButton("Popular", style=_market_button_style(), disabled=True),
                        ft.TextButton("Câmbio", style=_market_button_style(), on_click=market_tab_handler("FX")),
                        ft.TextButton("Ações", style=_market_button_style(), on_click=market_tab_handler("STOCK")),
                        ft.TextButton("Índices", style=_market_button_style(), disabled=True),
                        ft.TextButton("Futuros", style=_market_button_style(), disabled=True),
                        ft.TextButton("Cripto", style=_market_button_style(), disabled=True),
                    ],
                    wrap=True,
                    spacing=2,
                ),
                toolbar,
                ft.Container(
                    content=ft.Column(
                        [title_text, meta_text],
                        spacing=2,
                    ),
                    padding=ft.Padding.symmetric(horizontal=2, vertical=2),
                ),
                chart_container,
            ],
            expand=True,
            alignment="start",
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=spacing,
            scroll=ft.ScrollMode.AUTO,
        ),
        expand=True,
        height=max(page.height - 160 if page.height else chart_height + 260, chart_height + 260),
        padding=ft.Padding.symmetric(horizontal=horizontal_padding),
    )
