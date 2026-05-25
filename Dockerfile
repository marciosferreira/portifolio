FROM nginx:stable-alpine
LABEL maintainer="marciosferreira@yahoo.com.br"

# Copia todo o conteúdo do projeto para o diretório padrão do nginx
COPY . /usr/share/nginx/html

EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]
