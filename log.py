import logging
import datetime

# I assume decorators or something would improve this module


def config_log():
	logging.basicConfig(filename=f"results{filename_timestamp()}.log", level=logging.DEBUG,
		format='%(asctime)s - %(message)s')

def timestamp():
	now = datetime.datetime.now()
	return f"{now.month}/{now.day} at {now.hour}:{now.minute}"

def filename_timestamp():
	now = datetime.datetime.now()
	return f"{now.month}-{now.day}-{now.hour}-{now.minute}"

def log_result(message):
	print(f"{message}")
	logging.debug(f"(RESULT){message}")

def log_debug(message, source='', display=True):
	if display:
		print(f"(DEBUG){timestamp()}{source} -- {message}")
	logging.debug(message)

def log_only(message, source='', display=False):
	if display:
		print(f"(WARNING){timestamp()}{source} -- {message}")
	logging.warning(message)

def log_data(name, trump_votes, biden_votes, expected_biden_total, expected_trump_total, percent_reporting):
	logging.info(f"county name: {name}")
	logging.info(f"current biden votes: {biden_votes}")
	logging.info(f"expected biden total: {expected_biden_total}")
	logging.info(f"current trump votes: {trump_votes}")
	logging.info(f"expected trump total: {expected_trump_total}")

config_log()
