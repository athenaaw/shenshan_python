import logging

logger = logging.Logger("sample_1_logger")

file_handler = logging.FileHandler("sample_1.log")

file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("Timestamp:%(asctime)s Line number: %(lineno)d Information:%(message)s ")

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


# Testing code
logger.info ("This is sample_1 information.")