FROM nginx:stable-alpine
LABEL maintainer="marciosferreira@yahoo.com.br"

COPY . /usr/share/nginx/html
RUN sed -i 's/listen\s*80;/listen 8000;/g' /etc/nginx/conf.d/default.conf

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]
