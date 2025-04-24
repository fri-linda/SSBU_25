import logging
from typing import Optional


class Logger:
    """A utility class for setting up and managing logging."""

    def __init__(self, log_file: Optional[str] = None, log_level: int = logging.INFO):
        """
        Initialize the Logger instance.

        Parameters:
        - log_file: str, optional, the file to write logs to. If None, logs are only printed to the console.
        - log_level: int, the logging level (e.g., logging.INFO, logging.DEBUG).
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # create a formatter and set it for the console handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # add the console handler to the logger
        self.logger.addHandler(console_handler)

        # if a log file is specified, create a file handler
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(log_level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def info(self, message: str):
        """Log an informational message."""
        self.logger.info(message)

    def debug(self, message: str):
        """Log a debug message."""
        self.logger.debug(message)

    def warning(self, message: str):
        """Log a warning message."""
        self.logger.warning(message)

    def error(self, message: str):
        """Log an error message."""
        self.logger.error(message)

    def critical(self, message: str):
        """Log a critical message."""
        self.logger.critical(message)
