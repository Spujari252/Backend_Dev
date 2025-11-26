from typing import Union

from fastapi import FastAPI

app = FastAPI(title="My Test API")


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/status")
async def get_status():
    return {"message": "ok"}