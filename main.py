from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/items")
async def read_all_items():
    return {"items": "nothing in stock yet!!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item": item_id}

@app.get("/name/{name}")
async def read_name(name: str):
    return {f"your name is {name}"}