from fastapi import APIRouter

router = APIRouter()

@router.get("/CheckHeartBeat")
def check_heartbeat():
    return {"status": "ok", "message": "App is working"}