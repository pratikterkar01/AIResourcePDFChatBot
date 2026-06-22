import logging
import os
import time

from datetime import datetime
import sys
logs_path = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,"app.log")
IST_OFFSET_SECONDS = 5.5 * 60 * 60  # IST = UTC + 5:30
def ist_time(*args):
    return time.gmtime(time.time() + IST_OFFSET_SECONDS)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def get_logger(name: str) -> logging.Logger:
    '''logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        ))
        handler
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)'''
    logger = logging.getLogger(name)
    if not logger.handlers:
        stream_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        stream_formatter.converter = ist_time

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(stream_formatter)

        logger.addHandler(stream_handler)
        logger.setLevel(logging.INFO)

    return logger