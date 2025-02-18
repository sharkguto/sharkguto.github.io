#!/bin/bash
SCRIPTPATH="$(
    cd "$(dirname "$0")"
    pwd -P
)"
echo $SCRIPTPATH
cd $SCRIPTPATH

export PATH=$PATH:/usr/local/bin

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

rm -rf dist/

flet publish --app-name gmf-tech app.py

#cp -r dist/** $SCRIPTPATH/

echo $SCRIPTPATH

cp -r dist/* $SCRIPTPATH

cp requirements.txt $SCRIPTPATH/requirements.txt