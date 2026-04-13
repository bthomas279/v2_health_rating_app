#This file is the routing for the home page
#Imports
from fastapi import APIRouter

#Define Route
router = APIRouter()

@router.get("/home")
def get_home():
    return {"placeholder"}