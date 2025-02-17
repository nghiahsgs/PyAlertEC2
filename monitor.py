#!/usr/bin/env python3
import psutil
import time
from datetime import datetime
import requests
import os
import argparse

class SystemMonitor:
    def __init__(self, slack_webhook_url, cpu_warning=50, cpu_critical=80, ram_warning=80, check_interval=10):
        self.slack_webhook_url = slack_webhook_url
        self.cpu_warning = cpu_warning
        self.cpu_critical = cpu_critical
        self.ram_warning = ram_warning
        self.check_interval = check_interval

    def get_system_info(self):
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        return {
            'cpu': cpu,
            'ram': ram.percent,
            'disk': disk.percent
        }

    def get_top_processes(self, limit=5):
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                processes.append({
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu': proc.info['cpu_percent'],
                    'ram': proc.info['memory_percent']
                })
            except:
                pass
        return sorted(processes, key=lambda x: x['cpu'], reverse=True)[:limit]

    def send_slack_alert(self, message):
        try:
            payload = {'text': message}
            requests.post(self.slack_webhook_url, json=payload)
        except Exception as e:
            print(f"Error sending Slack notification: {str(e)}")

    def format_message(self, metrics, processes=None):
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"🕐 *Time:* {time_now}\n"
        message += f"🖥 *CPU:* {metrics['cpu']}%\n"
        message += f"💾 *RAM:* {metrics['ram']}%\n"
        message += f"💿 *Disk:* {metrics['disk']}%\n"

        if processes:
            message += "\n*Top 5 CPU-intensive processes:*\n"
            for proc in processes:
                message += f"- {proc['name']} (PID: {proc['pid']}): CPU {proc['cpu']}%, RAM {proc['ram']:.1f}%\n"

        return message

    def start_monitoring(self):
        print(f"🚀 Monitor started...")
        print(f"⚡ Alert thresholds:")
        print(f"   - CPU Warning: {self.cpu_warning}%")
        print(f"   - CPU Critical: {self.cpu_critical}%")
        print(f"   - RAM Warning: {self.ram_warning}%")
        print(f"   - Check interval: {self.check_interval} seconds")

        while True:
            try:
                metrics = self.get_system_info()
                
                # Check CPU Critical
                if metrics['cpu'] > self.cpu_critical:
                    processes = self.get_top_processes()
                    message = "🚨 *CRITICAL ALERT - CPU OVERLOAD*\n" + self.format_message(metrics, processes)
                    self.send_slack_alert(message)
                
                # Check CPU Warning
                elif metrics['cpu'] > self.cpu_warning:
                    processes = self.get_top_processes()
                    message = "⚠️ *Warning - High CPU Usage*\n" + self.format_message(metrics, processes)
                    self.send_slack_alert(message)
                
                # Check RAM
                if metrics['ram'] > self.ram_warning:
                    message = "⚠️ *Warning - High RAM Usage*\n" + self.format_message(metrics)
                    self.send_slack_alert(message)

                # Console logging
                print(f"[{datetime.now().strftime('%H:%M:%S')}] CPU: {metrics['cpu']}% | RAM: {metrics['ram']}% | Disk: {metrics['disk']}%")
                
            except Exception as e:
                print(f"Error: {str(e)}")
            
            time.sleep(self.check_interval)

def main():
    parser = argparse.ArgumentParser(description='System Resource Monitor with Slack Alerts')
    parser.add_argument('--webhook', required=True, help='Slack Webhook URL')
    parser.add_argument('--cpu-warning', type=float, default=75, help='CPU warning threshold (default: 50)')
    parser.add_argument('--cpu-critical', type=float, default=85, help='CPU critical threshold (default: 80)')
    parser.add_argument('--ram-warning', type=float, default=85, help='RAM warning threshold (default: 80)')
    parser.add_argument('--interval', type=int, default=10, help='Check interval in seconds (default: 10)')
    
    args = parser.parse_args()
    
    monitor = SystemMonitor(
        slack_webhook_url=args.webhook,
        cpu_warning=args.cpu_warning,
        cpu_critical=args.cpu_critical,
        ram_warning=args.ram_warning,
        check_interval=args.interval
    )
    
    monitor.start_monitoring()

if __name__ == "__main__":
    main()
