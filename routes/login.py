#This file is the routing for the login page
#Imports
from fastapi import APIRouter

#Define Route
router = APIRouter()

@router.get("/login")
def get_login():
    return {"placeholder"}