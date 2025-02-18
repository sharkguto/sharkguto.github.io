#!/bin/bash
SCRIPTPATH="$(
    cd "$(dirname "$0")"
    pwd -P
)"
echo $SCRIPTPATH
cd $SCRIPTPATH

export PATH=$PATH:/usr/local/bin

cd flet-gmftech/

flet publish --app-name gmf-tech app.py

#cp -r dist/** $SCRIPTPATH/