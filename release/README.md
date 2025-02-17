# PyAlertEC2 - Bản build

## Cài đặt nhanh

1. Giải nén file và vào thư mục:
```bash
tar xzf pyalertec2.tar.gz
cd pyalertec2
```

2. Chạy script cài đặt:
```bash
sudo ./install.sh
```

3. Nhập Slack webhook URL của bạn khi được yêu cầu.

Xong! Service sẽ tự động chạy và khởi động cùng hệ thống.

## Kiểm tra trạng thái

```bash
sudo systemctl status pyalertec2
```

## Xem logs

```bash
sudo journalctl -u pyalertec2 -f
```
