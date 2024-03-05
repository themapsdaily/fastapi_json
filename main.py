from fastapi import FastAPI
app = FastAPI()

from databases import Database
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@localhost/dbname"
database = Database(DATABASE_URL)

@app.on_event("startup")
async def startup_db():
    await database.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await database.disconnect()

from fastapi.responses import JSONResponse

@app.get("/get_data/{item_id}")
async def read_data(item_id: int):
    query = example_table.select().where(example_table.c.id == item_id)
    result = await database.fetch_one(query)

    if result:
        return JSONResponse(content=dict(result))
    else:
        return JSONResponse(content={"message": "Item not found"}, status_code=404)
