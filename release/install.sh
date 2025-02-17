#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root (sudo)"
    exit 1
fi

# Get Slack webhook URL
read -p "Enter your Slack webhook URL: " webhook_url

# Create directory
install_dir="/opt/pyalertec2"
mkdir -p $install_dir

# Copy files
cp monitor $install_dir/
chmod +x $install_dir/monitor

# Setup service
cp pyalertec2.service /etc/systemd/system/
sed -i "s|YOUR_SLACK_WEBHOOK_URL|$webhook_url|g" /etc/systemd/system/pyalertec2.service
sed -i "s|/home/ubuntu/PyAlertEC2/monitor.py|$install_dir/monitor|g" /etc/systemd/system/pyalertec2.service
sed -i "s|/usr/bin/python3||g" /etc/systemd/system/pyalertec2.service
sed -i "s|WorkingDirectory=.*|WorkingDirectory=$install_dir|g" /etc/systemd/system/pyalertec2.service

# Start service
systemctl daemon-reload
systemctl enable pyalertec2
systemctl start pyalertec2

echo "Installation complete! Service is running."
echo "Check status with: systemctl status pyalertec2"
echo "View logs with: journalctl -u pyalertec2 -f"
