from datetime import datetime, timedelta
from .api_call import fetch_api_data
from .dbClient import feeder_collection
from .dbClient import new_collection
from pymongo.collection import Collection


def update_ibedc_data(api_data):
    matched_feeders = []
    unmatched_feeders = []
    
    now = datetime.now()
    time_interval = now - timedelta(minutes=15)

    # Loop through API data
    recent_time_data = []
    for feeder_data in api_data:
        time_field = feeder_data.get('time') or feeder_data.get('Time') or feeder_data.get('TIME')
        
        
        if time_field:
            try:
                
                time_obj = datetime.strptime(time_field, "%H%M").time()
                feeder_data_datetime = datetime.combine(now.date(), time_obj)

                # Check if the time is within the last 15 minutes
                if time_interval <= feeder_data_datetime < now:
                    recent_time_data.append(feeder_data)

            except ValueError:
                print(f"Invalid time format in record: {feeder_data}")
           
    # Process only latest 15 minutes of data
    for feeder_data in recent_time_data:
        feeder_33 = feeder_data.get('feeder_33', '').lower()
        feeder_11 = feeder_data.get('feeder_11', '').lower()

        # Check if feeder already exists in the database
        query = {
            
            "feeder_33": {"$regex": f"^{feeder_33}$", "$options": "i"},
            "feeder_11": {"$regex": f"^{feeder_11}$", "$options": "i"},   
                }
        existing_feeder = feeder_collection.find_one(query)

        if existing_feeder:
            matched_feeders.append((feeder_33, feeder_11))
        else:
            unmatched_feeders.append((feeder_33, feeder_11))

    
        new_collection.insert_one(feeder_data)

    print(f"Matched feeders: {len(matched_feeders)}")
    print(f"Unmatched feeders: {len(unmatched_feeders)}")

    return matched_feeders, unmatched_feeders


