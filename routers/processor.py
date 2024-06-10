from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from typing import List

router = APIRouter()

@router.post('/text')
async def process_text(texts: List[str]) -> List[List[float]]:
    return [[1., .2]]

@router.post('/image')
async def process_image(images: List[UploadFile] = File(...)) -> List[List[float]]:
    return [[1., .2]]