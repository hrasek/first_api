from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json
import logger
from fastapi.middleware.cors import CORSMiddleware

# TODO: Try to build front-end for this app (spoiler alert: use Javascript).
# TODO: When reading the json file actually read the ID of the object DONE.
# TODO: Add the update and delete functionality.
# TODO: Build Get_gifts JavaScript function Partly done.
# TODO: Build Add_gifts JavaScript function.
# TODO: Build input field for ID.
# TODO: Build read all items functionality.
# TODO: Requirements.txt
# TODO: Commits DONE.


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()

#origins = ["http://localhost:5500", "http://localhost:8000"]
origins = ["*"]
# You can adjust the list of origins based on your needs

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can specify the HTTP methods you want to allow
    allow_headers=["*"],  # You can specify the HTTP headers you want to allow
)


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
        item_id = (list_dict[-1])['item_id'] + 1
    except FileNotFoundError:
        item_id = 0
        list_dict = []
        logger.log_warning(f'No such file or directory: {file_name}. New file created.' )
    except json.decoder.JSONDecodeError:
        item_id = 0
        list_dict = []
        logger.log_warning(f'Non valid data in: {file_name}. The old data deleted.' )
    item_dict.update({'item_id': item_id})
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
        for item in content_list:
            if item['item_id'] == item_id:
                return item
        else:
            raise IndexError
    except FileNotFoundError as e:
 #       e = 'File not found.'    
        logger.log_error(e)
        return 'ERROR. ' +  str(e)
    except json.decoder.JSONDecodeError:
        e = 'ID not found. Non JSON format of the line.'
        logger.log_error(e)
        return 'ERROR. ' +  e
    except IndexError:
        e = 'ID not found.'    
        logger.log_error(e)
        return 'ERROR. ' +  e
    except Exception as e: 
        logger.log_error(e)
        return  e