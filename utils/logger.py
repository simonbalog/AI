import logging
import os

class ColorFormatter(logging.Formatter):
    """Custom formatter to add colors to logs."""
    RED = "\033[1;31m"
    RESET = "\033[0m"

    def format(self, record):
        # Make the entire log line red
        log_message = super().format(record)
        return f"{self.RED}{log_message}{self.RESET}"

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Simple format for Rick Prime logs
    formatter = ColorFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    
    # Remove existing handlers if any (to avoid duplicates)
    if logger.hasHandlers():
        logger.handlers.clear()
        
    logger.addHandler(ch)
    return logger

logger = setup_logger("RickAI")
