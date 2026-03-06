from fastapi import FastAPI
from config import settings

app = FastAPI(title="Fallina API", version="1.0.0")

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Fallina API çalışıyor 🔮"
    }