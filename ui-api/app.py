from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CONFIG_PATH = "/delay-streamer/config.json"

class ConfigModel(BaseModel):
    delay_minutes: int
    output_rtmp: str

@app.get("/api/config")
def get_config():
    if not os.path.exists(CONFIG_PATH):
        return {"delay_minutes": 30, "output_rtmp": ""}
    with open(CONFIG_PATH) as f:
        return json.load(f)

@app.post("/api/config")
def update_config(data: ConfigModel):
    config = {}
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            config = json.load(f)
    config.update(data.dict())
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)
    return {"status": "ok"}

# Serve frontend
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def serve_index():
    return FileResponse("static/index.html")
