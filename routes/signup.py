#This file is the routing for the signup page
#Imports
from fastapi import APIRouter

#Define Route
router = APIRouter()

@router.get("/signup")
def get_signup():
    return {"placeholder"}
