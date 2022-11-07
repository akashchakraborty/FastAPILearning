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

## Swagger, HTTP Request Methods and Status Codes Overview

### OAS

The Open API Specification, also called OAS, is a documentation on creating universal standard on how to create and handle APIs.
The OAS document defines:
1. The schema - Abstract definition of how an API should look like.
2. Data format - The format (JSON/YAML) in which the data should be handled.
3. Data types - The primitive data types which are handled throughout the requests and responses.
4. Path - Which is how to handle param if the specific API takes any.
5. Object - Tells how objects should be handled within the API.
6. Much more...

FastAPI generates the OpenAPI schema so that we can view the same at:  *http://127.0.0.1:8000/openapi.json*.

### Swagger - UI

When we create APIs, an interactive documentation is created using Swagger-UI. 
This can be used at: *http://127.0.0.1:8000/docs*

### HTTP Request Methods

REST APIs uses same requests methods as HTTP. It tells the server, what the request wants to do, that is coming in.
REST APIs typically include:
1. GET - Read method that retrieves data
2. POST - Create method to submit data
3. PUT - Update part of a resource
4. PATCH - Update entire resource
5. DELETE - Delete the resource

These operations are also known as the CRUD - Create, Read, Update, Delete
There are also some uncommon ones like:
1. TRACE - Performs a message loopback to the target
2. CONNECT - Creates a tunnel to the server based on the target
3. OPTIONS - Describes communication options to the target

### Status Codes

Some status codes are:
1. 1xx - Informational Response: Request Processing
2. 2xx - Success: Request Successfully Completed
3. 3xx - Redirection: Requires client to complete further action
4. 4xx - Client Error: Usually error caused by request from client
5. 5xx - Server Error: Error occurred on the server

### Async

In this course we use *async* in front of all our  functions:

Example: ```async def this_is_a_function():```

We use async in FastAPI, due to asynchronous code, concurrency, and parallelism.
Using async is not necessary when coding with FastAPI, we use ```def this_is_a_function():``` instead.
In any of the cases above, FastAPI will still work asynchronously and perform very fast.
Using async before the function, typically provides performance optimizations when handling asynchronous functions.
