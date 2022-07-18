from fastapi import FastAPI
from sql_app import User, Room, Booking


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
