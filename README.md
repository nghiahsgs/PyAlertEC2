# PyAlertEC2 - System Resource Monitor with Slack Alerts

A simple Python-based system monitoring tool that sends alerts to Slack when CPU or RAM usage exceeds specified thresholds.

## Features
- Real-time monitoring of CPU, RAM, and Disk usage
- Configurable warning and critical thresholds
- Slack notifications for high resource usage
- Lists top CPU-intensive processes when alerts are triggered
- Easy to install and use

## Quick Start

1. **One-line installation (Linux/Mac):**
```bash
wget https://raw.githubusercontent.com/nghiahsgs/PyAlertEC2/main/monitor.py && pip install -r requirements.txt
```

2. **Get your Slack Webhook URL:**
- Go to https://api.slack.com/apps
- Create a new app (or use existing)
- Enable "Incoming Webhooks"
- Create a new webhook URL for your workspace
- Copy the webhook URL

3. **Run the monitor:**
```bash
python monitor.py --webhook "YOUR_SLACK_WEBHOOK_URL"
```

## Usage Options

```bash
python monitor.py --help
```

Available options:
- `--webhook`: Slack Webhook URL (required)
- `--cpu-warning`: CPU warning threshold % (default: 50)
- `--cpu-critical`: CPU critical threshold % (default: 80)
- `--ram-warning`: RAM warning threshold % (default: 80)
- `--interval`: Check interval in seconds (default: 10)

Example with custom thresholds:
```bash
python monitor.py --webhook "YOUR_SLACK_WEBHOOK_URL" --cpu-warning 70 --ram-warning 90 --interval 30
```

## Requirements
- Python 3.6+
- psutil
- requests

## License
MIT License
