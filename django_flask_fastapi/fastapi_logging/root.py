import logging
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get('/')
def read_root():
    return {"HELLO": "WORLD"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    handler = logging.handlers.RotatingFileHandler(
        "api.log", mode="a", maxBytes=100*1024, backupCount=3
    )
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %("
                                           "message)s"))
    logger.addHandler(handler)
