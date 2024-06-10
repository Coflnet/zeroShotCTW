import torch
import open_clip
import time

model, _, preprocess = open_clip.create_model_and_transforms('ViT-B-32', pretrained='laion2b_s34b_b79k')
tokenizer = open_clip.get_tokenizer('ViT-B-32')

def imageClassify(name, photo):
    image = preprocess(photo).unsqueeze(0)
    time.sleep(2)

    text = tokenizer([f'a photo of a {name}'])

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text)
        image_features /= image_features.norm(dim=-1, keepdim=True)
        cos_sim = torch.cosine_similarity(text_features, image_features, dim=-1)
        print(cos_sim)
