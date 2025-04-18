from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello FastAPI"}

@app.get("/items")
async def read_all_items(start: int = 0, total_items: int = 50, page_limit: int = 10, page: int = 1):
    items = [{"name": f"Item {i}"} for i in range(start + ((page - 1) * page_limit), (start + ((page - 1) * page_limit)) + page_limit)]
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item": item_id}

@app.get("/name/{name}")
async def read_name(name: str):
    return {f"your name is {name}"}