import json
import requests  
from fastapi import FastAPI 
from pydantic import BaseModel 
from typing import Union

app = FastAPI()

# Body content Type
class Request(BaseModel):
    key: str
    prompt: str
    negative_prompt: None
    init_image: str
    width: str
    height: str
    samples: str
    num_inference_steps: str
    guidance_scale: float
    safety_checker: str
    strength: float
    seed: None
    webhook: None
    track_id: None


class Response(BaseModel):        
    status: str
    generationTime: float
    id: int
    output: list
    meta = {
        "H": int,
        "W": int,
        "enable_attention_slicing": str,
        "file_prefix": str,
        "guidance_scale": float,
        "model": str,
        "n_samples": int,
        "negative_prompt": str,
        "outdir": str, 
        "prompt": str, 
        "revision": str, 
        "safety_checker": str, 
        "seed": int,
        "steps": int,
        "vae": str,
    }

headers = {
    "Authorization": "TB8pbRjDOHnXm93eNI08ft33DbD3lf7Ez3eahzqk3sSWemUmCIJID45fQQbi",
    "Content-Type": "application/json"
}

@app.get("/")
def read_root():
    return {"message": "Hello from Koyeb"}

@app.post("/response")  
def image_to_image(request: Request): 
    print(request)

    url = "https://stablediffusionapi.com/api/v3/img2img"  
    response = requests.post(url, json=request.dict(), headers=headers)
    
    if response.status_code == 200:
        try:
            result = Response(**response.json())
            print(result)
            if result.status == "success" :
                print(result.output)
                return result.output
        except (json.JSONDecodeError, TypeError, ValueError, AttributeError, KeyError) as e:
            print(f"Error creating Response object: {e}")
    else:
        return "failed to generate result of images"
    
