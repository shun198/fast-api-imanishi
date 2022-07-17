import datetime
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field


class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    booked_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime


class User(BaseModel):
    user_id: int
    username: str = Field(min_length=3, max_length=12)


class Room(BaseModel):
    room_id: int
    room_name: str = Field(min_length=3, max_length=12)
    capacity: int


app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Success"}


@app.post("/users")
async def create_user(user: User):
    return {"user": user}


@app.post("/rooms")
async def create_booking(room: Room):
    return {"rooms": room}


@app.post("/bookings")
async def create_booking(booking: Booking):
    return {"bookings": booking}
