#This file is the routing for the signup page
#Imports
from fastapi import APIRouter

#Define Route
#This is our "router"
signup = APIRouter(prefix="/signup")

@signup.get("/")
def signup_render():
    return {"placeholder"}
