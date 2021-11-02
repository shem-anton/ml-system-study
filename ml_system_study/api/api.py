from fastapi import APIRouter

from api.endpoints import predictions
from api.endpoints import logging

api_router = APIRouter()
api_router.include_router(predictions.router, prefix="/predict", tags=["predictions"])
api_router.include_router(logging.router, prefix="/log", tags=["logs"])
