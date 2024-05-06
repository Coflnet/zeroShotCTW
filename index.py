from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import aiFunctions as aiFunctions
import base64
from PIL import Image
from io import BytesIO

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ApiResult(BaseModel):
    image: str
    name: str


@app.post("/api/ctw/proccess")
async def process(data: ApiResult):
    image_bytes = base64.b64decode(data.image)
    image = Image.open(BytesIO(image_bytes))

    
    aiFunctions.imageClassify(data.name, image)
    
    return {"xp": 25}

@app.get("/")
async def gen():
    return {"message": "Hello World"}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="0.0.0.0", port=6969)
    


