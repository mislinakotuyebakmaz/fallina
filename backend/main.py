from fastapi import FastAPI
from config import settings
from routers import auth,fortune


app = FastAPI(title="Fallina API", version="1.0.0")
app.include_router(auth.router)
app.include_router(fortune.router)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Fallina API çalışıyor 🔮"
    }