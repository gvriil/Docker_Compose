import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myconfig.settings')

app = Celery('myconfig')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()