from datetime import datetime
import os


def save_report(result):
    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"reports/threat_report_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("Threat Intelligence Report\n")
        file.write("==========================\n\n")
        file.write(f"IOC: {result['ioc']}\n")
        file.write(f"Type: {result['type']}\n")
        file.write(f"Status: {result['status']}\n")
        file.write(f"Risk Score: {result['risk_score']}\n")
        file.write(f"Summary: {result['summary']}\n")

    return filename