from fastapi import APIRouter
from .processor import router as processor_router

master_router = APIRouter()

master_router.include_router(processor_router, prefix="/processor", tags=["processing"])