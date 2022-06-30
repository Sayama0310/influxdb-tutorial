from datetime import datetime
from dotenv import load_dotenv, main
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxClient:
    def __init__(self, token, org, bucket):
        self._org = org
        self._bucket = bucket
        self._client = InfluxDBClient(url="http://localhost:8086", token=token)

    def write_data(self, data, write_option=SYNCHRONOUS):
        write_api = self._client.write_api(write_option)
        write_api.write(self._bucket, self._org, data)


load_dotenv()
# You can generate a Token from the "Tokens Tab" in the UI
TOKEN = os.getenv('TOKEN')
ORG = os.getenv('ORG')
BUCKET = os.getenv('BUCKET')

client = InfluxClient(TOKEN, ORG, BUCKET)

client.write_data(
    [
        Point('sample_stock')
            .tag("stock", "sample")
            .field("Open", 65)
            .field("High", 63.38)
            .field("Low", 62.13)
            .time(int(datetime.strptime('2021-11-07', '%Y-%m-%d').timestamp())),
        Point('sample_stock')
            .tag("stock", "sample")
            .field("Open", 70)
            .field("High", 64.52)
            .field("Low", 63.73)
            .time(int(datetime.strptime('2021-11-08', '%Y-%m-%d').timestamp()))
    ]
)
