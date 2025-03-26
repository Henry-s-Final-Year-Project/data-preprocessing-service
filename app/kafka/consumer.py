import json
import logging
import signal
import sys
from kafka import KafkaConsumer
from app.services.preprocess import preprocess_transaction
from app.config import settings
from app.kafka.producer import get_producer, send_to_topic

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def start_kafka_consumer():
    consumer = KafkaConsumer(
        settings.KAFKA_RAW_TOPIC,
        bootstrap_servers=settings.KAFKA_BROKER,
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id=settings.KAFKA_CT_GROUP_ID,
    )

    producer = get_producer()

    def shutdown(signal, frame):
        logger.info("Shutting down consumer...")
        consumer.close()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    logger.info("Preprocessing service is listening for raw transactions...")

    for msg in consumer:
        raw_tx = msg.value
        try:
            features = preprocess_transaction(raw_tx)
            logger.info("Preprocessed Vector: %s", features)
            send_to_topic(producer, "card-preprocessed-data-topic", features)
        except Exception as e:
            logger.error("Error processing message: %s", e)
