FROM nginx:stable-alpine
LABEL maintainer="marciosferreira@yahoo.com.br"

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]
