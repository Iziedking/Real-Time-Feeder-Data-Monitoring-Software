from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from .tasks import scheduled_process
from .utils.api_call import fetch_api_data
from .utils.update_database import update_ibedc_data


def fetch_and_update_data(request):
  try:
    data = fetch_api_data()

    matched_feeders, unmatched_feeders = update_ibedc_data(data)

    message = {
      "status": "success",
      "matched_feeders_count": len(matched_feeders),
      "matched_feeders": matched_feeders,
      "unmatched_feeders-count": len(unmatched_feeders),
      "unmatched_feeders": unmatched_feeders
    }

    return JsonResponse(message)
  
  except Exception as e:
    return JsonResponse({"status": "Error", "message": str(e)})

def test_task(request):
  scheduled_process.delay()
  return HttpResponse("Celery Performing background task!")
  


  


