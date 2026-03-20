import os
import logging

from logging.handlers import RotatingFileHandler
from app.core.config import settings

# Ensure log directory exists
os.makedirs(os.path.dirname(settings.LOG_PATH), exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Add file handler
file_handler = RotatingFileHandler(
    settings.LOG_PATH,
    maxBytes=5_000_000, # limit log file size to 5MB
    backupCount=3 # keep up to 3 old log files as backup
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)