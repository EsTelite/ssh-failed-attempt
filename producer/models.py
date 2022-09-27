from bson import ObjectId
from schematics.models import Model
from schematics.types import StringType
from datetime import datetime


class FailedAttempts(Model):
    log_id = ObjectId()
    host = StringType(required=True)
    date = StringType(required=True)

newattempts = FailedAttempts()


def create_log_attempt(host):
    newattempts.log_id = ObjectId()
    newattempts.host = host
    newattempts.date = datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
    return dict(newattempts)
