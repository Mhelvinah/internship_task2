from fastapi import FastAPI # Import FastAPI

app = FastAPI() # Create FastAPI app


@app.get("/greet") #defining the endpoint
def greeting(name: str ="MELVINA"): # Define greeting function
    return f"Hello, {name}! Welcome to our FastAPI application."


