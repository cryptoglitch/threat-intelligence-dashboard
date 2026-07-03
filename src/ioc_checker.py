"""
Threat Intelligence Checker
Queries AbuseIPDB for IP reputation.
"""

import ipaddress
import requests

from config import ABUSEIPDB_API_KEY


def check_ip(ip_address):

    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        return {
            "status": "Invalid IP Address"
        }

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Accept": "application/json",
        "Key": ABUSEIPDB_API_KEY
    }

    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()["data"]

    score = data["abuseConfidenceScore"]

    if score >= 75:
        risk_level = "Critical"
    elif score >= 40:
        risk_level = "High"
    elif score >= 10:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "ip": data["ipAddress"],
        "country": data["countryCode"],
        "isp": data["isp"],
        "domain": data["domain"],
        "score": score,
        "risk_level": risk_level,
        "reports": data["totalReports"],
        "whitelisted": data["isWhitelisted"]
    }