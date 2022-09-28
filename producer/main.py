from fastapi import FastAPI
from models import create_log_attempt
import dbconn
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson.son import SON

app = FastAPI()


@app.get("/failed/")
async def failed(host: str = "unknown"):
    sqlite_insert(host)


@app.get("/metric/failed/{host}")
async def metric_failed(host):
    log_attempt = dbconn.db.log_attempt
    data = {"host":host, "failed_attempts_count":log_attempt.count_documents({"host": host})}
    json_compatible_item_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/metric/failed/")
async def metric_failed():
    log_attempt = dbconn.db.log_attempt
    pipeline = [
        {"$group": {"_id": "$host", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1), ("_id", -1)])}
    ]
    data = list(log_attempt.aggregate(pipeline))
    json_compatible_item_data = jsonable_encoder(data)
    return JSONResponse(content=json_compatible_item_data)

def sqlite_insert(host):
    data = create_log_attempt(host)
    dict(data)
    dbconn.db.log_attempt.insert_one(data)
    return {"detail": "success"}
