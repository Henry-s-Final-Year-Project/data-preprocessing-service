from kafka import KafkaProducer
import json
from app.config import settings


def start_kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers=settings.KAFKA_BROKER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )
    return producer


def send_to_topic(producer, topic, data):
    try:
        producer.send(topic, value=data)
        producer.flush()
        print(f"Produced to {topic}: {data}")
    except Exception as e:
        print(f"Error producing to {topic}: {e}")


_producer_instance = None


def get_producer():
    global _producer_instance
    if _producer_instance is None:
        _producer_instance = start_kafka_producer()
    return _producer_instance
