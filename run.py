import uvicorn

if __name__ == "__main__":
    print("Servidor rodando em http://127.0.0.1:8000  |  Ctrl+C para parar")
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="warning",
    )
