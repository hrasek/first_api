from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import ast
import logger


def read_and_eval(content_list: list[str], line_no: int):
    read_line = content_list[line_no]
    read_line_striped = read_line[0:-1]   
    read_line_dict = ast.literal_eval(read_line_striped)
    return read_line_dict

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item): 
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    file_name = 'first_api.txt'
    try:
        file_txt = open(file_name, 'r')
        content_list = file_txt.readlines()
        last_line_dict  = read_and_eval(content_list, -1)
        file_id = last_line_dict.get('file_id') + 1
        file_txt.close()
    except FileNotFoundError:
        file_id = 0
        logger.log_exception(f'No such file or directory: {file_name}. New file created.' )
    file_txt = open(file_name, mode = 'a')
    item_dict.update({'file_id': file_id})
    file_txt.write(str(item_dict) + '\n')
    logger.log_info(f'New line added to {file_name} file.')
    file_txt.close()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    file_name = 'first_api.txt'
    file_txt = open(file_name, 'r')
    content_list = file_txt.readlines()
    read_line_dict  = read_and_eval(content_list, item_id)
    file_txt.close()

    return read_line_dict