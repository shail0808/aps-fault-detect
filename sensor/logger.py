import logging
import os
from datatime import datatime
import os

LOG_FILE_NAME = f"{datatime.now().strftime('%m%d%Y_%H%M_%S')}.log"

#creating directory 
LOG_FILE_DIR = os.path.join(os.getcwd(),'logs')

# create folder if not available
os.makedirs(LOG_FILE_DIR, exist_ok = True)

# create logging file path
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR, LOG_FILE_NAME)

#log file path
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s-%(levelname)s - %(message)s",
    level=logging.INFO,
)