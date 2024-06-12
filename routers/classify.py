from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from ZeroShotCTW.pipeline import process_images, process_texts
from typing import List
from util import files_to_pil
import io

router = APIRouter()


@router.post('/')  # assuming the actual class exists in the query
def classify(captions: List[str], images: List[UploadFile] = File(...)) -> List[float]:
    images = files_to_pil(images)
    image_features = process_images(images)
    text_features = process_texts(captions)
