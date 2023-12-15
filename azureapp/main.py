from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data import DataApp


app = FastAPI(
    title="deso scb", description="Retrieves data from scb ", version="0.1.0"
)


class Item(BaseModel):
    deso: str


data = DataApp()


@app.post("/send-data/")
async def send_data(item: Item):
    out: str = data.get(item.deso)
    if out == "No data found for this deso":
        raise HTTPException(status_code=422, detail="Unprocessable Entity")
    return data.get(item.deso)
