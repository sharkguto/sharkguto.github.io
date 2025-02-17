#!/bin/bash
SCRIPTPATH="$(
    cd "$(dirname "$0")"
    pwd -P
)"
echo $SCRIPTPATH
cd $SCRIPTPATH

export PATH=$PATH:/usr/local/bin

cd gmftech/

rm -rf build/

briefcase build web

cd build/gmftech/web/static

mv app/ $SCRIPTPATH/app/

ls

cp requirements.txt $SCRIPTPATH/
cp briefcase.toml $SCRIPTPATH/

cd www

cp pyscript.toml $SCRIPTPATH/
cp index.html $SCRIPTPATH/

mv static/ $SCRIPTPATH/static/

cd ..

cp $SCRIPTPATH/sharkguto/src/assets/logo.png $SCRIPTPATH/static/logo-32.png
