from fastapi import FastAPI

from .routers import ping, heroes

app = FastAPI()
app.include_router(ping.router)
app.include_router(heroes.router)
