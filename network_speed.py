import sys
import psutil
import time
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from network_speed_gui import NetworkSpeedGUI

def get_size_unit(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes:.2f} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"

def get_speed_unit(speed_kbps): 
    if speed_kbps < 1024:
        return f"{speed_kbps:.2f} KB/s"
    else:
        return f"{speed_kbps / 1024:.2f} MB/s"

def update_gui():
    net_io_counters = psutil.net_io_counters()
    bytes_sent_new = net_io_counters.bytes_sent
    bytes_recv_new = net_io_counters.bytes_recv

    global bytes_sent, bytes_recv
    upload_speed = (bytes_sent_new - bytes_sent) / 1024  # in KB/s
    download_speed = (bytes_recv_new - bytes_recv) / 1024  # in KB/s

    total_sent = get_size_unit(bytes_sent_new)
    total_recv = get_size_unit(bytes_recv_new)

    gui.update_stats(get_speed_unit(download_speed), 
                     get_speed_unit(upload_speed),
                     total_recv,
                     total_sent)

    bytes_sent = bytes_sent_new
    bytes_recv = bytes_recv_new

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = NetworkSpeedGUI()
    gui.show()

    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv

    timer = QTimer()
    timer.timeout.connect(update_gui)
    timer.start(1000)  # update every 1 second

    sys.exit(app.exec_())
