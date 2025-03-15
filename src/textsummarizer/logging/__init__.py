import os
import sys
import logging

# Define log directory and file path
log_dir = os.path.join(os.getcwd(), "logs")  # Absolute path for consistency
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)  # Ensure directory exists

# Define logging format
logging_str = '[%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s]'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),  # Save logs to file
        logging.StreamHandler(sys.stdout)   # Print logs to console
    ]
)

# Create a logger instance
logger = logging.getLogger(__name__)  # Dynamically set logger name

# Test logging
if __name__ == "__main__":
    logger.info("Logger setup is working correctly!")





