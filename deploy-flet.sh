#!/bin/bash
set -euo pipefail

SCRIPTPATH="$(
    cd "$(dirname "$0")"
    pwd -P
)"
echo $SCRIPTPATH
cd $SCRIPTPATH

export PATH=$PATH:/usr/local/bin:$HOME/.local/bin:$HOME/flutter/3.41.7/bin
PYODIDE_VERSION="${PYODIDE_VERSION:-0.29.4}"

patch_pyodide_runtime() {
    local web_dir="$1"
    local python_js="$web_dir/python.js"
    local pyodide_url="https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js"

    if [[ ! -f "$python_js" ]]; then
        echo "python.js nao encontrado em $web_dir"
        exit 1
    fi

    sed -i -E "s#https://cdn\.jsdelivr\.net/pyodide/v[0-9]+\.[0-9]+\.[0-9]+/full/pyodide\.js#${pyodide_url}#g" "$python_js"

    if ! grep -Fq "$pyodide_url" "$python_js"; then
        echo "Falha ao aplicar Pyodide ${PYODIDE_VERSION} em $python_js"
        exit 1
    fi
}

rm -rf icons/
rm -f app.tar.gz
rm -f flutter*
rm -f main.dart.js
rm -f python*
rm -f version.json
rm -f index.html
rm -f favicon.png
rm -f manifest.json
rm -f bar_chart.html
rm -f requirements.txt

# exit 2

cd flet-gmftech/

rm -rf build/web/
rm -rf build/flutter/.dart_tool
rm -rf build/flutter/build
rm -f build/flutter/.flutter-plugins-dependencies

flet build web --yes
patch_pyodide_runtime "build/web"

cd "$SCRIPTPATH"

echo $SCRIPTPATH

cp -r flet-gmftech/build/web/* "$SCRIPTPATH"

# cp requirements.txt $SCRIPTPATH/requirements.txt
