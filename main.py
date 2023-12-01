from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json
import logger

# TODO: Solve the problem with the invalid lines in the txt file DONE.
# TODO: Solve the problem with the empty txt file DONE.
# TODO: Solve the problem with unexistent id DONE. 
# TODO: Context manager to open the file ('with') DONE.
# TODO: Use json for writing and reading of the file DONE.
# TODO: Side-quest: Use .json file instead of .txt file (Do not use 'ast') DONE.
# TODO: Do not write traceback to logger.log DONE.
# TODO: Add items.json to .gitignore DONE.  
# TODO: Try to import logging in the main.py and call logging.error() (or other method).
# TODO: Try to build front-end for this app (spoiler alert: use Javascript).

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()

file_name = 'items.json'

@app.post("/items/")
async def create_item(item: Item): 
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    try:
        with open(file_name, 'r') as file_json:
            list_dict = json.load(file_json)
        last_line_dict = list_dict[-1]
        file_id = last_line_dict.get('file_id') + 1
    except FileNotFoundError:
        file_id = 0
        list_dict = []
        logger.log_warning(f'No such file or directory: {file_name}. New file created.' )
    except (json.decoder.JSONDecodeError, IndexError):
        file_id = 0
        list_dict = []
    item_dict.update({'file_id': file_id})
    list_dict.append(item_dict)
    item_json = json.dumps(list_dict, indent = '\t')

    with open(file_name, mode = 'w') as file_json:
        file_json.write(item_json)
    logger.log_info(f'New line added to {file_name} file.')
    return json.dumps(item_dict)  

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    try:
        with open(file_name, 'r') as file_json:
            content_list = json.load(file_json)
        return content_list[item_id]
    except FileNotFoundError:
        e = 'File not found.'    
        logger.log_error(e)
        return 'ERROR. ' +  e
    except json.decoder.JSONDecodeError:
        e = 'ID not found. Non JSON format of the line.'
        logger.log_error(e)
        return 'ERROR. ' +  e
    except IndexError:
        e = 'ID not found. Too high ID number.'    
        logger.log_error(e)
        return 'ERROR. ' +  e
    except Exception as e: 
        logger.log_error(e)
        return  e