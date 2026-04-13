#Code to create API
#Imports
from fastapi import FastAPI
import uvicorn

#Grab routes
#Structure: folder.file
from routes.signup import signup
from routes.login import login
from routes.home import home


#Define App
app = FastAPI()

#Define routes in main
app.include_router(signup)
app.include_router(login)
app.include_router(home)


#Runs the model (starts on button submission)
#Important note: User Warning will appear

#Type in "fastapi dev main.py" in the console to start the application OR: 

#Click the "run python file" button
if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port=8000, reload = True)

#To access server http://127.0.0.1:8000
#To access documentation: http://127.0.0.1:8000/docs

