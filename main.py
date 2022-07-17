from lib2to3.pytree import Base
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello World"}


@app.get("/hello")
async def index():
    return {"message": "Hello Guys"}


@app.get("/country/{country_name}")
async def country(country_name: str):
    if country_name == "Japan":
        return {"message": "This is Japan"}
    else:
        return {"message": f"This is {country_name}, not Japan"}


@app.get("/country/")
async def country(country_name: Optional[str] = None, country_no: Optional[int] = None):
    return {
        "country_name": country_name,
        "country_no": country_no,
    }


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Item {item.name}'s price is {item.price*(item.tax)}"}
