import logging

import os

from datetime import datetime





LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%H_%S')}.log"
log_path= os.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(log_path,exsist_ok=True) 

LOG_FILE_PATH =os.join(log_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s]  %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)