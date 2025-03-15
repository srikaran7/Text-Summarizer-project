import sys
import os

sys.path.append(os.path.abspath("src"))  # ✅ Add 'src' to system path

from textsummarizer.logging.logger import logger

logger.info("Welcome to the log file successfully!")
