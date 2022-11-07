# importing FAST API
from fastapi import FastAPI

app = FastAPI()


# create an asynchronous function
@app.get("/")  # adding a descriptor
async def first_api():
    return {"message": "Hello eric"}
