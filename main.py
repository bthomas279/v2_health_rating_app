#Code to create API
#Imports
from fastapi import FastAPI
import uvicorn

#Grab routes

from routes import signup


#Define App
app = FastAPI(title="Mental Health Web-App")


#Define routes in main
app.include_router(signup.router, prefix="/users", tags=["Users"])
#app.include_router(login)
#app.include_router(home)

@app.get("/")
def root():
    return {"message": "Welcome to the API"}


#Runs the model (starts on button submission)
#Important note: User Warning will appear

#Type in "fastapi dev main.py" in the console to start the application OR: 

#Click the "run python file" button
if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port=8000, reload = True)

#To access server http://127.0.0.1:8000
#To access documentation: http://127.0.0.1:8000/docs

