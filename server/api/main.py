from fastapi import FastAPI

from controllers.image_search import get_images

app = FastAPI()


@app.get("/")
def index():
    return "OK"


@app.get("/images")
async def images():
    results = get_images("monty python and the holy grail")

    return results
