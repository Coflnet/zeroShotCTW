import torch
import open_clip
import time
from PIL import Image
from typing import List
import numpy as np

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
model.eval()

tokenizer = open_clip.get_tokenizer('ViT-B-32')

@torch.no_grad() 
@torch.autocast(device_type=device)
def process_images(images: List[Image.Image]) -> torch.Tensor:
    images = torch.stack([preprocess(image) for image in images], dim=0)
    return model.encode_image(images)


@torch.no_grad() 
@torch.autocast(device_type=device)
def process_texts(texts: List[str]) -> torch.Tensor:
    texts = tokenizer(texts)
    return model.encode_text(texts)

