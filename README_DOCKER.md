# Deploy estático com Docker (EasyPanel)

Instruções rápidas para construir e rodar a imagem Docker localmente e no EasyPanel.

Build local:

```powershell
cd c:\Users\mnsmferr\portfolio
docker build -t portfolio-static:latest .
docker run -p 8000:80 portfolio-static:latest
# abrir http://localhost:8000
```

Enviar para o EasyPanel:

- No EasyPanel escolha criar um novo projeto a partir de um `Dockerfile`.
- Faça upload deste repositório (ou aponte o painel para a pasta com o `Dockerfile`).
- Configure a porta pública para 80 / HTTP.
- Opcional: configurar um certificado TLS/HTTPS no painel (Let's Encrypt disponível no EasyPanel).

Observações:
- O container usa `nginx` para servir arquivos estáticos; assegure que a pasta `images/` está incluída no build (já está no repositório).
- Se quiser adicionar cache, headers ou redirecionamentos, eu posso incluir um `nginx.conf` customizado.
