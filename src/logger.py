import logging
import os
import sys
import exception

from datetime import datetime





LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%H_%S')}.log"
log_path= os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(log_path,exist_ok=True) 

LOG_FILE_PATH =os.path.join(log_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[%(asctime)s]  %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

if __name__ == "__main__":


    #TESTING EXCEPTIONS AND LOGGERS
    try :
        a=1/0
    except Exception as e:
        logging.info("divided by zeo:  "+ str(exception.CustomException(e,sys))+ "")
        raise exception.CustomException(e,sys)
       