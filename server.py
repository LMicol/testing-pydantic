# FastAPI 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator

# Image handler
from PIL import Image

app = FastAPI()

class Capture(BaseModel):
    username: str
    capture: str
    x: int
    y: int

    # @validator("caputure")
    # def validate_capture(cls, value):
        
@app.post('/send_image')
async def send_image(data: Capture):
    print(data)
    #photo.capture.save("img.png")
    
