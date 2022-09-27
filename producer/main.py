from fastapi import FastAPI
from models import create_log_attempt
import dbconn

app = FastAPI()

@app.get("/failed/")
async def failed(host: str = "unknown"):
    sqlite_insert(host)


def sqlite_insert(host):
    data = create_log_attempt(host)
    dict(data)
    dbconn.db.users.insert_one(data)
    return {
        'statusCode': 200
    }

