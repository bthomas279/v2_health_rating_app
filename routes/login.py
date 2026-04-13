#This file is the routing for the login page
#Imports
from fastapi import APIRouter

#Define Route
#This is our "router"
login = APIRouter(prefix="/login")


@login.get("/")
def login_render():
    return {"placeholder"}

