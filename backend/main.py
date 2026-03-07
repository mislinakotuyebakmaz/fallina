from fastapi import FastAPI
from config import settings
from routers import auth


app = FastAPI(title="Fallina API", version="1.0.0")
app.include_router(auth.router)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Fallina API çalışıyor 🔮"
    }