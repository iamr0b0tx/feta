from fastapi import FastAPI

from router import router as main_router
from routers import router as social_router

app = FastAPI(title="Main")
app.include_router(main_router)
app.include_router(social_router)


@app.get("/ping")
async def ping():
    return "pong"
