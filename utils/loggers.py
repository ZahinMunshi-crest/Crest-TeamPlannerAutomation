import os
import logging
from logging.handlers import RotatingFileHandler

def get_loggers(name: str) -> logging.Logger:
    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger
    
    # Set logging level
    logger.setLevel(logging.DEBUG)

    # Create log directory
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    #Path to log file
    log_file = os.path.join(log_dir, "tp_loggers.log")

    # Rotate when log file reaches 5 MB, keep 3 backups
    file_handler = RotatingFileHandler(
        log_file, maxBytes=3*1024*1024, backupCount=3, encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)

    # Print logs on console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s",datefmt="%H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
