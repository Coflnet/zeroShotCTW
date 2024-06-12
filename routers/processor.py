from fastapi import APIRouter, UploadFile, File
from util import files_to_pil
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
    pil_images = files_to_pil(images)
    embeddings = pipeline.process_images(pil_images)
    return embeddings.detach().cpu().tolist()
