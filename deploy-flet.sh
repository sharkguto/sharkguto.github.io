#!/bin/bash
set -euo pipefail

SCRIPTPATH="$(
    cd "$(dirname "$0")"
    pwd -P
)"
echo $SCRIPTPATH
cd $SCRIPTPATH

export PATH=$PATH:/usr/local/bin:$HOME/.local/bin:$HOME/flutter/3.41.7/bin

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

cd "$SCRIPTPATH"

echo $SCRIPTPATH

cp -r flet-gmftech/build/web/* "$SCRIPTPATH"

# cp requirements.txt $SCRIPTPATH/requirements.txt
