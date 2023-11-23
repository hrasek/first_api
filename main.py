from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
import ast

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
    file_name = 'first_api.txt'
    try:
        file_txt = open(file_name, 'r')
        content_list = file_txt.readlines()
        last_line = content_list[-1]
        last_line_striped = last_line[0:-1] 
        last_line_dict = ast.literal_eval(last_line_striped)
        file_id = last_line_dict.get('file_id') + 1
        file_txt.close()
    except FileNotFoundError:
        file_id = 0
    file_txt = open(file_name, mode = 'a')
    item_dict.update({'file_id': file_id})
    file_txt.write(str(item_dict) + '\n')
    file_txt.close()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # TODO: Open the specific file and read the item defined by the item_id.
    return {"item_id": item_id}
# TODO: Implement logging for both the methods. 