import logging
from pathlib import Path

HERE = Path(__file__).parent

LOG_FILE = HERE / "logger.log"


logging.basicConfig(filename=LOG_FILE,
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

def log_warning(e) -> None:
    logging.warning(e)

def log_info(info) -> None:
    logging.info(info)

def log_error(e) -> None:
    logging.error(e)