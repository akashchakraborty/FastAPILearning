# FAST API Tutorial

## Running our first app

1. Create a new file called *books.py**
2. Then write the following code:
    ```python
    # importing FAST API
    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    # create an asynchronous function
    @app.get("/")  # adding a descriptor
    async def first_api():
        return {"message": "Hello eric"}
    ```
    Here, first we say app=FastAPI()
    Then we create an asynchronous function which will return a dictionary, having the message as: Hello world.
    
    The ```@app.get('/')``` is the descriptor that is used in order to give the path.

3. Then, we need to run the server by:
   ```
   uvicorn books:app --reload
   ```
This will our first API that gives in return a dict object containing a message.

