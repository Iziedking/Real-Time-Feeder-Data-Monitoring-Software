from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import Settings
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'feederapp.settings')

app = Celery('feederapp')
app.conf.enable_utc = False
app.conf.update(timezone = 'Africa/Lagos')
app.conf.broker_connection_retry_on_startup = True

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

#celery beat settings
app.conf.beat_schedule = {
    'update_iebdc_data_every_15mins': {
        'task': 'feeder_tracker.tasks.scheduled_process',
        'schedule': crontab(minute='*/15')
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')