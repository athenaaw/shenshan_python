import logging

logger = logging.Logger("sample_1_logger")

formatter = logging.Formatter("Timestamp:%(asctime)s Line number: %(lineno)d Information:%(message)s ")

# create file handler to send the log to file
file_handler = logging.FileHandler("sample_2.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)


# create stream handler to send the log to console.
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Testing code
logger.info ("This is sample_2...")