from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from typing import List
from PIL import Image
from ZeroShotCTW.pipeline import process_images, process_texts
import io

router = APIRouter()


@router.post('/texts')
async def process_text(texts: List[str]) -> List[List[float]]:
    embeddings = process_texts(texts)
    return embeddings.detach().cpu().tolist()


@router.post('/images')
async def process_image(images: List[UploadFile] = File(...)) -> List[List[float]]:
    pil_images = [Image.open(io.BytesIO(image.file.read())) for image in images]
    embeddings = process_images(pil_images)
    return embeddings.detach().cpu().tolist()
