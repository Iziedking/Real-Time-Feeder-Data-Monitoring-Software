import json
from datetime import datetime, timedelta
import requests
import pandas as pd

def fetch_api_data():
    days = 0
    dt1 = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(
        days=days)
    dt1 = dt1.strftime("%Y-%m-%d %H:%M:%S")

    dt2 = datetime.now().replace(hour=23, minute=59, second=0, microsecond=0)
    dt2 = dt2.strftime("%Y-%m-%d %H:%M:%S")


    payload = {}


    url1 = "http://amiapi.ibedc.com:6568/comm/login?username=ibedc_nerc&password=19d5bd29fca20e07174a98ca3d253d35"
    headers = {}
    response = None


    try:
        response = requests.request("GET", url1, headers=headers, data=payload)

    except (TimeoutError, Exception):
        raise Exception("Ibadan API connection timed out. Retrying...")

    if response is None:
        print("Ibadan API request failed after 3 retries.")

    resp = None

    try:
        resp = response.json()
    except (TimeoutError, Exception):
        raise Exception("Ibadan API not available")

    sid = resp["sessionID"]
    credentials = [sid]

    # Declare all urls
    url2 = "http://amiapi.ibedc.com:6568/comm/getLoadProfile"
    url3 = "http://amiapi.ibedc.com:6568/comm/NERCSBTGetFeederName"
    url4 = "http://amiapi.ibedc.com:6568/comm/NERCSBTGetData"
    url5 = "http://amiapi.ibedc.com:6568/comm/logout?token={0}".format(*credentials)

    payload3 = json.dumps({"sessionId": sid, "startdate": dt1, "enddate": dt2})
    headers = {"Content-Type": "application/json"}

    r = requests.request("POST", url4, headers=headers, data=payload3)

    data = r.json()


    try:
        if r.status_code != 200:
            
            raise Exception(
                f"Ibadan API request failed with status code {r.status_code}"
            )
    except (TimeoutError, Exception):
        raise Exception("Ibadan API not available at this time")


    try:
        if not data:
            raise Exception("No data returned from Ibadan API.")
    except Exception as e:
        raise Exception(e)


    res = data.get("data")
    #df = pd.DataFrame(res)
    return res
    
   
