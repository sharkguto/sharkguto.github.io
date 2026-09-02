#!/bin/bash
set -euo pipefail

SCRIPTPATH="$(
    cd "$(dirname "$0")"
    pwd -P
)"
APP_DIR="$SCRIPTPATH/flet-gmftech"
WEB_DIR="$APP_DIR/build/web"
APP_EXCLUDES=(
    ".coverage"
    ".coveragerc"
    ".gitignore"
    ".pytest_cache"
    ".venv"
    "AGENTS.md"
    "README.md"
    "__pycache__"
    "images"
    "new2.py"
    "old.py"
    "pages/__pycache__"
    "pyproject.toml"
    "pytest.ini"
    "requirements-dev.txt"
    "requirements.txt"
    "tests"
    "tools"
    "utils/__pycache__"
    "uv.lock"
)

export PATH="$PATH:/usr/local/bin:$HOME/.local/bin:$HOME/flutter/3.41.7/bin"
PYODIDE_VERSION="${PYODIDE_VERSION:-314.0.3}"

if ! command -v uv >/dev/null 2>&1; then
    echo "uv nao encontrado no PATH"
    exit 1
fi

patch_pyodide_runtime() {
    local web_dir="$1"
    local index_html="$web_dir/index.html"
    local python_js="$web_dir/python.js"
    local pyodide_mjs_url="https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.mjs"
    local pyodide_js_url="https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js"
    local patched=0

    if [[ -f "$index_html" ]]; then
        sed -i -E "s#https://cdn\.jsdelivr\.net/pyodide/v[0-9]+\.[0-9]+\.[0-9]+/full/pyodide\.(mjs|js)#${pyodide_mjs_url}#g" "$index_html"

        if grep -Fq "$pyodide_mjs_url" "$index_html"; then
            patched=1
        fi
    fi

    if [[ -f "$python_js" ]]; then
        sed -i -E "s#https://cdn\.jsdelivr\.net/pyodide/v[0-9]+\.[0-9]+\.[0-9]+/full/pyodide\.js#${pyodide_js_url}#g" "$python_js"

        if grep -Fq "$pyodide_js_url" "$python_js"; then
            patched=1
        fi
    fi

    if [[ "$patched" -ne 1 ]]; then
        echo "Falha ao localizar ou aplicar Pyodide ${PYODIDE_VERSION} em $web_dir"
        exit 1
    fi
}

validate_app_bundle() {
    local app_zip="$1/assets/app/app.zip"

    if [[ ! -f "$app_zip" ]]; then
        echo "app.zip nao encontrado em $app_zip"
        exit 1
    fi

    (
        cd "$APP_DIR"
        uv run python - "$app_zip" <<'PY'
import sys
import zipfile
from pathlib import Path

app_zip = Path(sys.argv[1])
max_size = 100 * 1024 * 1024
forbidden_roots = {".pytest_cache", ".venv", "images", "tests", "tools"}
forbidden_files = {"new2.pyc", "old.pyc"}

with zipfile.ZipFile(app_zip) as archive:
    names = archive.namelist()

invalid = []
for name in names:
    parts = tuple(part for part in Path(name).parts if part not in {"", "."})
    if not parts:
        continue
    if parts[0] in forbidden_roots or "__pycache__" in parts or parts[0] in forbidden_files:
        invalid.append(name)

if app_zip.stat().st_size >= max_size:
    raise SystemExit(f"app.zip excede o limite de 100 MiB: {app_zip.stat().st_size} bytes")
if invalid:
    raise SystemExit(f"app.zip contem arquivos locais indevidos: {invalid[:10]}")
if not any(name.startswith("__pypackages__/flet/") for name in names):
    raise SystemExit("app.zip nao contem a dependencia flet")

print(f"app.zip validado: {app_zip.stat().st_size} bytes, {len(names)} arquivos")
PY
    )
}

echo "Gerando bundle web com uv em $APP_DIR"

# A limpeza integral evita que o cache do empacotador pule as dependencias.
rm -rf "$APP_DIR/build"

(
    cd "$APP_DIR"
    uv run flet build web --yes --exclude "${APP_EXCLUDES[@]}"
)

patch_pyodide_runtime "$WEB_DIR"

# O index usa o runtime pela CDN; nao publique a copia local gerada pelo Flet.
rm -rf "$WEB_DIR/pyodide"
validate_app_bundle "$WEB_DIR"

echo "Atualizando arquivos publicados em $SCRIPTPATH"

rm -rf "$SCRIPTPATH/icons"
rm -rf "$SCRIPTPATH/pyodide"
rm -f "$SCRIPTPATH/app.tar.gz"
rm -f "$SCRIPTPATH"/flutter*
rm -f "$SCRIPTPATH/main.dart.js"
rm -f "$SCRIPTPATH"/python*
rm -f "$SCRIPTPATH/version.json"
rm -f "$SCRIPTPATH/index.html"
rm -f "$SCRIPTPATH/favicon.png"
rm -f "$SCRIPTPATH/manifest.json"
rm -f "$SCRIPTPATH/bar_chart.html"
rm -f "$SCRIPTPATH/requirements.txt"

cp -a "$WEB_DIR"/. "$SCRIPTPATH"/

echo "Deploy preparado com Pyodide ${PYODIDE_VERSION}"
