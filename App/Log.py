from datetime import datetime
import logging

def get_logger(logger_name):
    path_file_log=f'../Log/log_ge{datetime.now().strftime("%Y%m%d")}.log'
    logging.basicConfig(
        filename=path_file_log,
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s'"
    )
    logger = logging.getLogger(logger_name)
    File_Handler = logging.FileHandler(path_file_log)

    logger.addHandler(File_Handler)
    Stream_Handler = logging.StreamHandler()
    logger.addHandler(Stream_Handler)

    return logger
