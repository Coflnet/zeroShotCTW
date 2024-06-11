from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from ZeroShotCTW.pipeline import process_images, process_texts
from typing import List
from PIL import Image
import io

router = APIRouter()

@router.post('/')
def classify(captions: List[str], images: List[UploadFile] = File(...)) -> List[float]:
    
    images = [Image.open(io.BytesIO(image.file.read())) for image in images]
    image_features = process_images(images)
    text_features = process_texts(captions)

    
