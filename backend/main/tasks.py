import requests

from datetime.datetime import timezone
from celery import shared_task

from .models import CeleryTask
from backend.settings import BASE_API_URL


now = timezone.now()


@shared_task
def run_first_script():
    CeleryTask.objects.create(name=f"Run first script at {now}", status="STARTED")
    response = requests.post(f"{BASE_API_URL}/api/v1/autostart/scripts", json={"part": 1})
    CeleryTask.objects.create(name=f"Run first script at {now}", status="SUCCESS")
    return response.json()


@shared_task
def run_third_script():
    CeleryTask.objects.create(name=f"Run third script at {now}", status="STARTED")
    response = requests.post(f"{BASE_API_URL}/api/v1/autostart/scripts", json={"part": 3})
    CeleryTask.objects.create(name=f"Run third script at {now}", status="SUCCESS")
    return response.json()


@shared_task
def run_fourth_script():
    CeleryTask.objects.create(name=f"Run fourth script at {now}", status="STARTED")
    response = requests.post(f"{BASE_API_URL}/api/v1/autostart/scripts", json={"part": 4})
    CeleryTask.objects.create(name=f"Run fourth script at {now}", status="SUCCESS")
    return response.json()


@shared_task
def run_fifth_script():
    CeleryTask.objects.create(name=f"Run fifth script at {now}", status="STARTED")
    response = requests.post(f"{BASE_API_URL}/api/v1/autostart/scripts", json={"part": 5})
    CeleryTask.objects.create(name=f"Run fifth script at {now}", status="SUCCESS")
    return response.json()


@shared_task
def run_sixth_script():
    CeleryTask.objects.create(name=f"Run sixth script at {now}", status="STARTED")
    response = requests.post(f"{BASE_API_URL}/api/v1/autostart/scripts", json={"part": 6})
    CeleryTask.objects.create(name=f"Run sixth script at {now}", status="SUCCESS")
    return response.json()
