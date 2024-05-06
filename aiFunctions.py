import open_clip
import torch
from PIL import Image
import open_clip

from transformers import pipeline
import torchvision.transforms as transforms

classifier = pipeline(task="image-classification")

model, preprocess, _ = open_clip.create_model_and_transforms(model_name='ViT-B/32', pretrained='openai')
image = Image.open('./images/something.jpg')
image_input = preprocess(image).unsqueeze(0)

import open_clip
import torch
import torchvision.transforms as transforms
from PIL import Image

import torch
from PIL import Image
import open_clip
import time

model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')

# image = preprocess(Image.open("./images/teddybear.jpg")).unsqueeze(0)
# text = tokenizer(["a photo of  a teddybear"])



def imageClassify(name, photo):
    image = preprocess(photo).unsqueeze(0)
    time.sleep(2)
    
    text = tokenizer([f'a photo of a {name}'])
    
    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        cosi = torch.nn.CosineSimilarity(dim=-1) 
        text_probs = cosi(image_features, text_features)
        print(text_probs)



def imageClass(image) -> list[int, str]:
    preds = classifier(image)
    print(preds["score"][0])