#This file is the routing for the home page
#Imports
from fastapi import APIRouter

#Define Route
#This is our "router"
home = APIRouter(prefix="/home")

@home.get("/")
def home_render():
    return {"placeholder"}