import psutil
import time
import curses

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

def display_speed(stdscr):
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent
    bytes_recv = net_io_counters.bytes_recv

    while True:
        time.sleep(1)

        net_io_counters = psutil.net_io_counters()
        bytes_sent_new = net_io_counters.bytes_sent
        bytes_recv_new = net_io_counters.bytes_recv

        upload_speed = (bytes_sent_new - bytes_sent) / 1024  # in KB/s
        download_speed = (bytes_recv_new - bytes_recv) / 1024  # in KB/s

        total_sent = get_size_unit(bytes_sent_new)
        total_recv = get_size_unit(bytes_recv_new)

        stdscr.clear()

        # Display title
        title = "Network Speed Monitor"
        stdscr.addstr(0, (curses.COLS - len(title)) // 2, title)

        # Display current speeds
        stdscr.addstr(2, 0, f"Current Download Speed: {get_speed_unit(download_speed)}")
        stdscr.addstr(2, curses.COLS // 2, f"Current Upload Speed: {get_speed_unit(upload_speed)}")

        # Display total data
        stdscr.addstr(3, 0, f"Total Data Downloaded: {total_recv}")
        stdscr.addstr(3, curses.COLS // 2, f"Total Data Sent: {total_sent}")

        # Display footer
        footer = "Made with ❤️  by Nishan"
        stdscr.addstr(curses.LINES - 1, (curses.COLS - len(footer)) // 2, footer)

        stdscr.refresh()

        bytes_sent = bytes_sent_new
        bytes_recv = bytes_recv_new

def main():
    curses.wrapper(display_speed)

if __name__ == "__main__":
    main()
