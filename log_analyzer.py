import re

def analyze_logs(log_file):
    alerts = []
    with open(log_file, "r") as f:
        for line in f:
            if "Failed password" in line or "unauthorized" in line.lower():
                match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3})', line)
                if match:
                    ip = match.group(0)
                    alerts.append(f"🚨 Suspicious activity from IP: {ip}")
    return alerts

# Sample usage
if __name__ == "__main__":
    results = analyze_logs("auth.log")  # Replace with your actual log path
    for alert in results:
        print(alert)
