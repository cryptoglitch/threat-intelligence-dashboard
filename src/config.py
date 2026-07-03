"""
Configuration module.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_PATH = PROJECT_ROOT / ".env"

print(f"Looking for .env at: {ENV_PATH}")

load_dotenv(ENV_PATH)

ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")


def validate_configuration():
    if not ABUSEIPDB_API_KEY:
        return False, "API key NOT FOUND"

    return True, "API key loaded successfully"