# utils/test_step.py
# Context manager for logging test steps with consistent formatting.
# Wraps an action: logs START, SUCCESS, or FAILURE with timing.

import time
import logging
from contextlib import contextmanager
from typing import Generator

from utils.logger import get_logger

logger = get_logger("step")


@contextmanager
def step(description: str, level: int = logging.INFO) -> Generator:
    """
    Log a named test step with its outcome and duration.

    Usage:
        from utils.test_step import step

        with step("Fill patient name field"):
            driver.find_element(*L.PATIENT_NAME).send_keys("Juan")

        with step("Save patient form"):
            page.click_save()

    Output in log:
        INFO  ┌─ Fill patient name field
        INFO  └─ PASS  Fill patient name field  (0.12s)

        INFO  ┌─ Save patient form
        ERROR └─ FAIL  Save patient form  (1.03s)
               TimeoutException: element not found after 20s
    """
    start = time.time()
    logger.log(level, f"┌─ {description}")
    try:
        yield
        elapsed = time.time() - start
        logger.log(level, f"└─ PASS  {description}  ({elapsed:.2f}s)")
    except Exception as exc:
        elapsed = time.time() - start
        logger.error(f"└─ FAIL  {description}  ({elapsed:.2f}s)")
        logger.error(f"   {type(exc).__name__}: {exc}")
        raise   # re-raise so the test still fails