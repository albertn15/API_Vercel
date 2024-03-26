from fastapi import FastAPI

app = FastAPI()

df = {
    1: {"name": "Hana", "age": 10},
    2: {"name": "Rifdah", "age": 18}
}

@app.get('/data')
def read_data():
    return df

@app.put("/items/{item_id}")
def update_item(item_id: int, update_data: dict):

    # Perform the update using the data from the request body
    df[item_id].update(update_data)

    return {"message": f"Item with ID {item_id} has been updated successfully."}