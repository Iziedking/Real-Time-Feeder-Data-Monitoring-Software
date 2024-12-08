from celery import shared_task
from .utils.api_call import fetch_api_data
from .utils.update_database import update_ibedc_data

@shared_task
def scheduled_process():
    try:
        print("Task Started: Fetching API")
        api_data = fetch_api_data()

        if api_data:
            print("API data fetched")
            update_ibedc_data(api_data)
            print('Database updated sucessfully')
            return "Database updated sucessfully"

        else:
            print("API data not available at this time")
            return "API data not available"
    except Exception as e:
        print(f"API data unavailable now. wait for next retry: {e}")
        return "Error: {e}"
        



