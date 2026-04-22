# =============================================================================
# utils/config.py
# Central configuration loaded from .env
# =============================================================================

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Application
    BASE_URL   = os.getenv("BASE_URL",   "http://torejamedicalclinic.wuaze.com")
    USERNAME   = os.getenv("ADMIN_USERNAME", "admin")
    PASSWORD   = os.getenv("ADMIN_PASSWORD", "admin123")

    # Browser
    BROWSER             = os.getenv("BROWSER",           "chrome")
    HEADLESS            = os.getenv("HEADLESS",          "false").lower() == "true"
    IMPLICIT_WAIT       = int(os.getenv("IMPLICIT_WAIT", "10"))
    EXPLICIT_WAIT       = int(os.getenv("EXPLICIT_WAIT", "15"))
    PAGE_LOAD_TIMEOUT   = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))

    # Directories
    SCREENSHOT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
    REPORT_DIR     = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")
