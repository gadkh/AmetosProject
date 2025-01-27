from celery import Celery
import os

RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")


celery_app = Celery(
    "ingestion_service",
    # broker=RABBITMQ_URL
    broker="amqp://guest:guest@rabbitmq:5672/"
)

celery_app.conf.task_routes = {
    'tasks.process_event': {'queue': 'events'}
}


@celery_app.task(name="tasks.process_event")
def process_event(event_data):
    print(f"Processing event: {event_data}")
    return f"Processed event {event_data['device_id']}"




