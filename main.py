from fastapi import FastAPI
from pydantic import BaseModel

import requests


# TODO: Добавить Flake8
# TODO: Добавить нормальную архитектуру
app = FastAPI()

from environs import Env

env = Env()
env.read_env()

token=env.str("BOT_TOKEN")


class Video(BaseModel):
    file_path: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/video')
async def createVideo(video: Video):
    file_path = video.file_path
    url = f'https://api.telegram.org/file/bot{token}/{file_path}'

    response = requests.get(url)

    with open('video.mp4', 'wb') as f: 
        f.write(response.content)

    return {"message": "success"}
