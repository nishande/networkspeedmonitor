from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy, QFrame
from PyQt5.QtGui import QFont, QMovie, QPalette, QColor
from PyQt5.QtCore import Qt, QTimer

class NetworkSpeedGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Network Speed Monitor')
        self.setGeometry(100, 100, 400, 250)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        title_label = QLabel('Current Speed')
        title_label.setFont(QFont('Arial', 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #4a4a4a")
        layout.addWidget(title_label)

        speed_layout = QHBoxLayout()
        speed_layout.setSpacing(20)
        
        self.download_label = QLabel('Download: -')
        self.download_label.setFont(QFont('Arial', 18))
        self.download_label.setStyleSheet("color: #4a4a4a; background-color: #f2f2f2; padding: 10px; border-radius: 5px")
        speed_layout.addWidget(self.download_label)

        self.upload_label = QLabel('Upload: -')
        self.upload_label.setFont(QFont('Arial', 18))
        self.upload_label.setStyleSheet("color: #4a4a4a; background-color: #f2f2f2; padding: 10px; border-radius: 5px")
        speed_layout.addWidget(self.upload_label)

        layout.addLayout(speed_layout)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        total_title_label = QLabel('Total Data Usage')
        total_title_label.setFont(QFont('Arial', 24, QFont.Bold))
        total_title_label.setAlignment(Qt.AlignCenter)
        total_title_label.setStyleSheet("color: #4a4a4a")
        layout.addWidget(total_title_label)

        total_layout = QHBoxLayout()
        total_layout.setSpacing(20)

        self.total_download_label = QLabel('Download: -')
        self.total_download_label.setFont(QFont('Arial', 14))
        self.total_download_label.setStyleSheet("color: #4a4a4a; background-color: #f2f2f2; padding: 10px; border-radius: 5px")
        total_layout.addWidget(self.total_download_label)

        self.total_upload_label = QLabel('Upload: -') 
        self.total_upload_label.setFont(QFont('Arial', 14))
        self.total_upload_label.setStyleSheet("color: #4a4a4a; background-color: #f2f2f2; padding: 10px; border-radius: 5px")
        total_layout.addWidget(self.total_upload_label)

        layout.addLayout(total_layout)

        footer_layout = QHBoxLayout()
        footer_layout.addStretch(1)

        footer_label = QLabel('Made with ')
        footer_label.setFont(QFont('Arial', 12, italic=True))
        footer_label.setStyleSheet("color: #888888")
        footer_layout.addWidget(footer_label)

        self.heart_label = QLabel()
        self.heart_movie = QMovie('heart.gif')
        self.heart_label.setMovie(self.heart_movie)
        self.heart_movie.start()
        self.heart_label.setScaledContents(True)
        self.heart_label.setFixedSize(20, 20)
        footer_layout.addWidget(self.heart_label)

        footer_label2 = QLabel(' by Nishan')
        footer_label2.setFont(QFont('Arial', 12, italic=True))
        footer_label2.setStyleSheet("color: #888888")
        footer_layout.addWidget(footer_label2)

        footer_layout.addStretch(1)
        footer_layout.setAlignment(Qt.AlignCenter)

        layout.addLayout(footer_layout)

        self.setLayout(layout)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('#ffffff'))
        self.setPalette(palette)

    def update_stats(self, download_speed, upload_speed, total_download, total_upload):
        self.download_label.setText(f"Download: {download_speed}")
        self.upload_label.setText(f"Upload: {upload_speed}")
        self.total_download_label.setText(f"Download: {total_download}")
        self.total_upload_label.setText(f"Upload: {total_upload}")
