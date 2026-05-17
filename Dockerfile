FROM nginx:1.27-alpine

ARG PYODIDE_VERSION=0.29.4

COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY flet-gmftech/build/web/ /usr/share/nginx/html/

RUN test -f /usr/share/nginx/html/index.html \
    && test -f /usr/share/nginx/html/python.js \
    && test -f /usr/share/nginx/html/assets/app/app.zip \
    && sed -i -E "s#https://cdn\\.jsdelivr\\.net/pyodide/v[0-9]+\\.[0-9]+\\.[0-9]+/full/pyodide\\.js#https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js#g" /usr/share/nginx/html/python.js \
    && grep -F "https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js" /usr/share/nginx/html/python.js

EXPOSE 80
