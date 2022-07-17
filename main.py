from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel, Field

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


class ShopInfo(BaseModel):
    name: str
    location: str


class Item(BaseModel):
    name: str = Field(min_length=4, max_length=12)
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


class Data(BaseModel):
    shop_info: Optional[ShopInfo]
    items: List[Item]


@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Item {item.name}'s price is {item.price*(item.tax)}"}


@app.post("/data/")
async def create_data(data: Data):
    return {"data": data}
