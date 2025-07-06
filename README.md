# Log-Analyzer-with-Alerts
# Log Analyzer with Alerts

Analyzes Linux system logs (e.g., `/var/log/auth.log`) for suspicious activity like failed SSH logins and unauthorized access attempts.

## Features
- Detects failed login attempts
- Flags suspicious IPs
- Customizable patterns

## Usage
1. Place your log file in the same directory (e.g., `auth.log`)
2. Run: `python log_analyzer.py`
3. View flagged IPs in the output
