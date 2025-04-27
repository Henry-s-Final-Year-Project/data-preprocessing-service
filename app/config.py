import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
    KAFKA_RAW_TOPIC = os.getenv("KAFKA_RAW_TOPIC", "card-raw-data-topic")
    KAFKA_PREPROCESSED_TOPIC = os.getenv(
        "KAFKA_PROCESSED_TOPIC", "card-processed-data-topic"
    )
    KAFKA_CT_GROUP_ID = os.getenv("KAFKA_CT_GROUP_ID", "card-transaction-group")


settings = Settings()
