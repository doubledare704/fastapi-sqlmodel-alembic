from fastapi import APIRouter

router = APIRouter(tags=["ping"])


@router.get("/ping")
async def pong():
    return {"ping": "pong!"}
