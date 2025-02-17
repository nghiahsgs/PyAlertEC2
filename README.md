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

## Cài đặt như một Service (Ubuntu)

1. Clone repository về máy:
```bash
git clone https://github.com/nghiahsgs/PyAlertEC2.git
cd PyAlertEC2
```

2. Cài đặt các dependencies:
```bash
pip3 install -r requirements.txt
```

3. Sao chép file service vào thư mục systemd:
```bash
sudo cp pyalertec2.service /etc/systemd/system/
```

4. Chỉnh sửa file service để thêm Slack Webhook URL của bạn:
```bash
sudo nano /etc/systemd/system/pyalertec2.service
```
Thay `YOUR_SLACK_WEBHOOK_URL` bằng URL webhook thực tế của bạn.

5. Reload systemd và enable service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable pyalertec2
sudo systemctl start pyalertec2
```

6. Kiểm tra trạng thái service:
```bash
sudo systemctl status pyalertec2
```

7. Xem logs:
```bash
sudo journalctl -u pyalertec2 -f
```

## Cài đặt nhanh từ bản build (Ubuntu)

1. Tải bản build mới nhất từ [Releases](https://github.com/nghiahsgs/PyAlertEC2/releases)
2. Giải nén và cài đặt:
```bash
tar xzf pyalertec2.tar.gz
cd pyalertec2
sudo ./install.sh
```
3. Nhập Slack webhook URL của bạn khi được yêu cầu

Xong! Service sẽ tự động chạy và khởi động cùng hệ thống.

## Build từ source

Nếu bạn muốn tự build:

1. Clone repository:
```bash
git clone https://github.com/nghiahsgs/PyAlertEC2.git
cd PyAlertEC2
```

2. Chạy script build:
```bash
chmod +x build.sh
./build.sh
```

File build sẽ được tạo tại `pyalertec2.tar.gz`

## Requirements
- Python 3.6+
- psutil
- requests

## License
MIT License
