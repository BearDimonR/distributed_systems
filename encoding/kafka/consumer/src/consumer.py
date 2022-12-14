from src.schemas import LanguageCreate
from src.service import create_language
import os
from json import loads
import threading
from kafka import KafkaConsumer

BOOTSTRAP_SERVER = os.environ.get('BOOTSTRAP_SERVER', 'localhost:9092')


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(
            'language',
            bootstrap_servers=[BOOTSTRAP_SERVER],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='1',
            value_deserializer=lambda x: loads(x.decode('utf-8'))
        )

        while not self.stop_event.is_set():
            for event in consumer:
                language_create = LanguageCreate(**event.value)
                language = create_language(language_create)
                print('created:', str(language))
                if self.stop_event.is_set():
                    break

        consumer.close()
