__author__ = "Sachin Verma"
__description__ = "This script contains static methods used across the project"


## import libraries
import logging

## logging setup

@staticmethod
def setup_logger(log_file_path="log_output.txt"):
    """Setup logger to save logs to a text file and console."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler(log_file_path, mode='w', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )