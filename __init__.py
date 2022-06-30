from datetime import datetime
from dotenv import load_dotenv, main
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

load_dotenv()
# You can generate a Token from the "Tokens Tab" in the UI
token = os.getenv('TOKEN')
org = os.getenv('ORG')
bucket = os.getenv('BUCKET')

client = InfluxDBClient(url="http://localhost:8086", token=token)

