from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
dbPassword = os.getenv('DB_PASSWORD')


def get_db_client():
    url = f'''mongodb+srv://patrickisraeldominic:{dbPassword}@feedermonitoringsystem.64wrk.mongodb.net/?retryWrites=true&w=majority&appName=feederMonitoringSystem'''
    client = MongoClient(url, server_api=ServerApi('1'))

    try:
        client.admin.command('ping')
        print("Pinged your deployment Successful!")
    except Exception as e:
        print(e)
        print("Failed to connect to MongoDB. Please check your connection string and try again")
    return client


client = get_db_client()
db = client['Feeder_db']
feeder_collection = db['ibedc_feeder']
collection_name = f"ibedc_feeder_{datetime.now().strftime('%Y%m%d_%H%M')}"
new_collection = db[collection_name]
