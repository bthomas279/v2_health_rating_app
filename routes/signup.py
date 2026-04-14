#This file is the routing for the signup page
#Imports
from fastapi import APIRouter, Request

#Imports for static templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

#Define Route
#This is our "router"
router = APIRouter(prefix="/signup")

#Connect public folder(css) to main
router.mount("/public", StaticFiles(directory="public"), name="public")
#Connect views folder(html) to main
views = Jinja2Templates(directory="views")

@router.get("/", response_class=HTMLResponse)
async def signup_render(request: Request):
    return views.TemplateResponse("signup.html", {"request": request})
