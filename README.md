# Network Speed Monitor 📊 For Windows/MACOS/Linux

A simple Python script that displays real-time network speed and data usage statistics in the terminal. It shows the current download and upload speeds, as well as the total data downloaded and uploaded. The script uses the `psutil` library to retrieve network information and the `curses` library for terminal-based UI rendering.

## Features ✨

- Real-time monitoring of network speed and data usage
- Displays current download and upload speeds in KB/s or MB/s
- Shows total data downloaded and uploaded
- Updates the display in-place for a clean and responsive UI
- Minimal dependencies: `psutil` and `curses`

## Installation 🚀

1. Clone the repository:
git clone https://github.com/nishande/networkspeedmonitor.git

2. Navigate to the project directory:
cd networkspeedmonitor

3. Install the required dependencies:
pip install psutil curses

## Usage 💻

Run the script using the following command:
python network_speed_monitor.py
OR
python3 network_speed_monitor.py

The script will start monitoring your network speed and data usage. The display will update in real-time, showing the current download and upload speeds, as well as the total data downloaded and uploaded.


## Contributing 🤝

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License 📄

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements 🙏

- [psutil](https://github.com/giampaolo/psutil) - Cross-platform library for retrieving information on running processes and system utilization
- [curses](https://docs.python.org/3/library/curses.html) - Terminal-based UI library for Python

Made with ❤️ by Nishan
