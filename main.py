from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()


@app.get("/")
async def read_item():
    return {"message": "Hello World"}