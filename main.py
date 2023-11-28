from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json
import logger

# TODO: Solve the problem with the invalid lines in the txt file.
# TODO: Solve the problem with the empty txt file.
# TODO: Solve the problem with unexistent id. 
# TODO: Context manager to open the file ('with') DONE.
# TODO: Use json for writing and reading of the file DONE.
# TODO: Side-quest: Use .json file instead of .txt file (Do not use 'ast').
# TODO: Do not write traceback to logger.log. 
# TODO: Try to import logging in the main.py and call logging.error() (or other method).
# TODO: Try to build front-end for this app (spoiler alert: use Javascript).

def read_and_eval(content_list: list[str], line_no: int):
    read_line = content_list[line_no]
    read_line_dict = json.loads(read_line)
    return read_line_dict

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()

file_name = 'first_api.txt'

@app.post("/items/")
async def create_item(item: Item): 
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    try:
        with open(file_name, 'r') as file_txt:
            content_list = file_txt.readlines()
        last_line_dict  = read_and_eval(content_list, -1)
        file_id = last_line_dict.get('file_id') + 1
    except FileNotFoundError:
        file_id = 0
        logger.log_warning(f'No such file or directory: {file_name}. New file created.' )
    item_dict.update({'file_id': file_id})
    item_json = json.dumps(item_dict)
    with open(file_name, mode = 'a') as file_txt:
        file_txt.write(item_json + '\n')
    logger.log_info(f'New line added to {file_name} file.')
    return json.dumps(item_dict)  

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    with open(file_name, 'r') as file_txt:
        content_list = file_txt.readlines()
    read_line_dict  = read_and_eval(content_list, item_id)

    return read_line_dict