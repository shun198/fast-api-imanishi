from typing import Optional
from fastapi import FastAPI

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
async def country(country_name: str, country_no: int):
    return {
        "country_name": country_name,
        "country_no": country_no,
    }
