import logging
import time

logging.basicConfig(filename="logging/start.txt",level=logging.DEBUG, format='%(asctime)s %(message)s' ,datefmt='%B %Y-%m-%d (%A) %I:%M:%s ->')
a=0
while True:
    a+=1
    logging.info(f"This is info test {a}.")
    time.sleep(1)
    logging.info(f"This is warning test {a}.")
    time.sleep(1)
    logging.info(f"This is error test {a}.")
    time.sleep(1)
    logging.info(f"This is debug test {a}.")
    time.sleep(1)
    logging.info("-"*100)
    logging.shutdown()