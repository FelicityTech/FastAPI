from fastapi import FastAPI
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str
    description: str

# Define items at application start
items = {"bananas": "Yellow fruit."}

app = FastAPI()


@app.put("/items")
def update_item(item: Item):
    name = item.name
    # Update the description
    items[item.name] = item.description
    return item

#     curl -X PUT \
#   -H 'Content-Type: application/json' \
#   -d '{"name": "bananas", "description": "Delicious!"}' \
#   http://localhost:8000/items