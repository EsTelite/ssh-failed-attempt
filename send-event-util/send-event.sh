#!/bin/sh
curl -X GET http://PRODUCER_ADDR:8000/failed/?host=$(hostname)