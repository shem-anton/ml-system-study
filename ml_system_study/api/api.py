from fastapi import APIRouter

from api.endpoints import predictions

api_router = APIRouter()
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])