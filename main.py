from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item): 
    # TODO: Upgrade the function so it creates the file and writes the data into it.
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict



@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # TODO: Open the specific file and read the item defined by the item_id.
    return {"item_id": item_id}
# TODO: Implement logging for both the methods. 