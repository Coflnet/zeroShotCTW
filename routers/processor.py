from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from typing import List
from PIL import Image
from ZeroShotCTW import pipeline
import io

router = APIRouter()


@router.post('/texts', tags=[''])
async def process_texts(texts: List[str]) -> List[List[float]]:
    embeddings = pipeline.process_texts(texts)
    return embeddings.detach().cpu().tolist()


@router.post('/images')
async def process_images(images: List[UploadFile] = File(...)) -> List[List[float]]:
    pil_images = [Image.open(io.BytesIO(image.file.read())) for image in images]
    embeddings = pipeline.process_images(pil_images)
    return embeddings.detach().cpu().tolist()
