from fastapi import FastAPI
from routers.auth import router as login_router

app = FastAPI(title="Dhatri API", version="0.1.0")

app.include_router(login_router)
@app.get("/")
def read_root():
    return {"message": "Hello from Dhatri API"}



@app.get("/health")
def health_check():
    return {"status": "ok"}