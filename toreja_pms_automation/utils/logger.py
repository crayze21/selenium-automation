# utils/logger.py
# Central logger for the entire test suite.
# Import get_logger() in any file that needs logging.

import logging
import os
import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler

from utils.config import Config


# ── ANSI colour codes for console output ──────────────────────────────────────
class _Colours:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    GREY    = "\033[90m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    MAGENTA = "\033[95m"

    LEVEL = {
        "DEBUG":    GREY,
        "INFO":     CYAN,
        "WARNING":  YELLOW,
        "ERROR":    RED,
        "CRITICAL": MAGENTA + BOLD,
    }


class _ColouredFormatter(logging.Formatter):
    """Adds ANSI colour to the level name in console output."""

    FMT = "%(asctime)s  %(levelname)-8s  %(name)s  %(message)s"
    DATE = "%H:%M:%S"

    def format(self, record: logging.LogRecord) -> str:
        colour = _Colours.LEVEL.get(record.levelname, _Colours.RESET)
        record.levelname = f"{colour}{record.levelname}{_Colours.RESET}"
        formatter = logging.Formatter(self.FMT, datefmt=self.DATE)
        return formatter.format(record)


class _PlainFormatter(logging.Formatter):
    """Plain text formatter for file output (no ANSI codes)."""

    FMT  = "%(asctime)s  %(levelname)-8s  %(name)-30s  %(message)s"
    DATE = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        super().__init__(fmt=self.FMT, datefmt=self.DATE)


# ── Build the root logger once ────────────────────────────────────────────────
def _build_root_logger() -> logging.Logger:
    root = logging.getLogger("pms_tests")
    root.setLevel(logging.DEBUG)

    if root.handlers:           # already configured — skip
        return root

    # 1. Console handler — INFO and above, colour formatted
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console.setFormatter(_ColouredFormatter())
    root.addHandler(console)

    # 2. Rotating file handler — DEBUG and above, plain text
    log_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "logs"
    )
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file  = os.path.join(log_dir, f"test_run_{timestamp}.log")

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,   # 5 MB per file
        backupCount=10,              # keep last 10 log files
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(_PlainFormatter())
    root.addHandler(file_handler)

    root.info(f"Log file: {log_file}")
    return root


_ROOT_LOGGER = _build_root_logger()


def get_logger(name: str) -> logging.Logger:
    """
    Get a named child logger under 'pms_tests'.
    Use the module name as the name for easy filtering.

    Usage:
        from utils.logger import get_logger
        logger = get_logger(__name__)
        logger.info("Patient saved successfully")
    """
    return _ROOT_LOGGER.getChild(name)