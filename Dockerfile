FROM nginx:stable-alpine
LABEL maintainer="marciosferreira@yahoo.com.br"

COPY . /usr/share/nginx/html

RUN printf 'server {\n  listen 8000;\n  root /usr/share/nginx/html;\n  index index.html;\n  location / { try_files $uri $uri/ /index.html; }\n}\n' \
    > /etc/nginx/conf.d/default.conf

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]
