import os
import sys
import time

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright


URL = os.environ.get("GMFTECH_E2E_URL", sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8080/")
PYODIDE_VERSION = os.environ.get("GMFTECH_EXPECTED_PYODIDE", "314.0.3")
TIMEOUT_SECONDS = int(os.environ.get("GMFTECH_E2E_TIMEOUT", "180"))
SCREENSHOT_PATH = os.environ.get("GMFTECH_E2E_SCREENSHOT", "/tmp/gmftech-playwright.png")
VIEWPORT_WIDTH = int(os.environ.get("GMFTECH_E2E_WIDTH", "1366"))
VIEWPORT_HEIGHT = int(os.environ.get("GMFTECH_E2E_HEIGHT", "900"))

ERROR_MARKERS = (
    "Python worker init error",
    "Unhandled error",
    "Traceback",
    "ModuleNotFoundError",
    "PythonError",
    "Can't find a pure Python",
)

IGNORED_CONSOLE_MARKERS = (
    "WEBGL_debug_renderer_info is deprecated",
    "unreachable code after return statement",
)


def relevant_console_errors(messages):
    errors = []
    for message_type, text in messages:
        if any(marker in text for marker in IGNORED_CONSOLE_MARKERS):
            continue
        if message_type == "error" or any(marker in text for marker in ERROR_MARKERS):
            errors.append((message_type, text))
    return errors


def launch_browser(playwright):
    requested = os.environ.get("PLAYWRIGHT_BROWSER")
    browser_names = [requested] if requested else ["chromium", "firefox", "webkit"]
    last_error = None
    for browser_name in browser_names:
        if not browser_name:
            continue
        browser_type = getattr(playwright, browser_name)
        try:
            launch_options = {"headless": True}
            if browser_name == "chromium":
                launch_options["chromium_sandbox"] = False
                launch_options["args"] = [
                    "--no-sandbox",
                    "--disable-setuid-sandbox",
                    "--disable-dev-shm-usage",
                    "--disable-gpu",
                ]
            return browser_name, browser_type.launch(**launch_options)
        except Exception as exc:  # noqa: BLE001
            last_error = exc
    raise RuntimeError(f"Nenhum browser Playwright disponivel. Ultimo erro: {last_error}")


def request_failure_text(request):
    failure = request.failure
    if callable(failure):
        failure = failure()
    if isinstance(failure, dict):
        return failure.get("errorText") or failure.get("error_text") or "unknown"
    if isinstance(failure, str):
        return failure
    return getattr(failure, "error_text", None) or "unknown"


def main():
    console_messages = []
    page_errors = []
    failed_requests = []

    with sync_playwright() as playwright:
        browser_name, browser = launch_browser(playwright)
        context = browser.new_context(
            viewport={"width": VIEWPORT_WIDTH, "height": VIEWPORT_HEIGHT},
            service_workers="block",
        )
        page = context.new_page()

        page.on("console", lambda msg: console_messages.append((msg.type, msg.text)))
        page.on("pageerror", lambda exc: page_errors.append(str(exc)))
        page.on(
            "requestfailed",
            lambda request: failed_requests.append(
                f"{request.url} :: {request_failure_text(request)}"
            ),
        )

        page.goto(URL, wait_until="domcontentloaded", timeout=120_000)

        bundle_files = page.evaluate(
            """async () => {
                const fetchText = (path) =>
                    fetch(new URL(path, document.baseURI), { cache: "no-store" })
                        .then((response) => response.text());
                const [pythonJs, indexHtml] = await Promise.all([
                    fetchText("python.js"),
                    fetchText("index.html"),
                ]);
                return { pythonJs, indexHtml };
            }"""
        )
        expected_urls = (
            f"https://cdn.jsdelivr.net/pyodide/v{PYODIDE_VERSION}/full/pyodide.js",
            f"https://cdn.jsdelivr.net/pyodide/v{PYODIDE_VERSION}/full/pyodide.mjs",
        )
        pyodide_source = next(
            (
                source_name
                for source_name, source in (
                    ("python.js", bundle_files["pythonJs"]),
                    ("index.html", bundle_files["indexHtml"]),
                )
                if any(expected_url in source for expected_url in expected_urls)
            ),
            None,
        )
        if pyodide_source is None:
            raise AssertionError(
                "Bundle nao aponta para uma URL Pyodide esperada: "
                + " ou ".join(expected_urls)
            )

        started_at = time.monotonic()
        initialized = False
        while time.monotonic() - started_at < TIMEOUT_SECONDS:
            if any("Python worker initialized" in text for _, text in console_messages):
                initialized = True
                break
            errors = relevant_console_errors(console_messages)
            if errors:
                break
            page.wait_for_timeout(1000)

        page.wait_for_timeout(2500)
        page.screenshot(path=SCREENSHOT_PATH, full_page=True)

        errors = relevant_console_errors(console_messages)
        if page_errors or errors or failed_requests:
            recent_console = "\n".join(f"[{kind}] {text}" for kind, text in console_messages[-30:])
            raise AssertionError(
                "Falha na validacao Playwright.\n"
                f"Browser: {browser_name}\n"
                f"Page errors: {page_errors}\n"
                f"Console errors: {errors}\n"
                f"Failed requests: {failed_requests}\n"
                f"Console recente:\n{recent_console}"
            )

        if not initialized:
            recent_console = "\n".join(f"[{kind}] {text}" for kind, text in console_messages[-30:])
            raise AssertionError(
                "Python worker nao inicializou dentro do timeout.\n"
                f"Browser: {browser_name}\n"
                f"Console recente:\n{recent_console}"
            )

        flutter_hosts = page.evaluate(
            "() => document.querySelectorAll('flt-glass-pane, flt-semantics-host').length"
        )
        if flutter_hosts < 1:
            raise AssertionError("Nenhum host Flutter/Flet foi renderizado.")

        print(f"OK: {URL} validado com Playwright/{browser_name}")
        print(f"OK: Pyodide {PYODIDE_VERSION} configurado em {pyodide_source}")
        print(f"OK: screenshot salvo em {SCREENSHOT_PATH}")

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
