from PIL import Image
import io


def files_to_pil(files):
    return [Image.open(io.BytesIO(image.file.read())) for image in files]
