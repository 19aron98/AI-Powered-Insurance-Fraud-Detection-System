import os
import sys
import logging
from from_root import from_root
from datetime import datetime

# Constants for log configurations
logging_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_file = f"{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"

# log directory
log_dir = "logs"
log_dir_path = os.path.join(from_root(), log_dir)
os.makedirs(log_dir_path, exist_ok=True)

# log file 
log_file_path = os.path.join(log_dir_path, log_file)

logging.basicConfig(
    level=logging.DEBUG,
    format=logging_format,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger()
