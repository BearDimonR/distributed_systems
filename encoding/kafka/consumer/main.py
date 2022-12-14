from src.consumer import Consumer
import time

def main():
    consumer = Consumer()
    consumer.start()
    
    time.sleep(5)
    
    consumer.join()


if __name__ == "__main__":
    main()
