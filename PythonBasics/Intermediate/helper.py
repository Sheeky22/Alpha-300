import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# logger.info("Hi From Helper!")

# fileHandler = logging.FileHandler("PythonBasics/Intermediate/file.log")

# fileHandler.setLevel(logging.ERROR)

# logger.addHandler(fileHandler)

# logger.error("Hi File!")

# handler = RotatingFileHandler('PythonBasics/Intermediate/app.log',maxBytes=2000,backupCount=5)
# logger.addHandler(handler)

# for _ in range(500):
#     logger.info("Hello")