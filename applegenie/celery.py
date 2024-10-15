# your_project/celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'applegenie.settings')  # Replace with your project name

app = Celery('applegenie')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
