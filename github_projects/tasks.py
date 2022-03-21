from typing import Dict, List

import requests

from django_example_site.celery import app
from .models import WebhookConfig, ProjectEntry
from .serializers import ProjectSerializer


@app.task
def invoke_all_webhooks(entry_id: int):
    def get_webhooks() -> List[WebhookConfig]:
        return list(WebhookConfig.objects.all())

    data = ProjectSerializer(ProjectEntry.objects.get(pk=entry_id)).data
    for wh in get_webhooks():
        send_webhook.apply_async(args=(wh.url, wh.method, data))


@app.task
def send_webhook(url: str, method: str, data: Dict) -> int:
    if method == 'GET':
        return requests.get(
            url=url,
            params=data,
            timeout=5
        ).status_code
    elif method == 'POST':
        return requests.post(
            url=url,
            json=data,
            timeout=5
        ).status_code
    else:
        raise ValueError(f'Unknown request method: {method}')
