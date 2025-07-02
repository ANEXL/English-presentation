from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QEvent
from PyQt6.QtGui import QKeySequence
import sys
import socket

def send_udp_message(message):
    udp_rec = "led-box.bbrouter"
    try:
        udp_ip = socket.gethostbyname(udp_rec)
    except socket.gaierror:
        udp_ip = "localhost"  # Fallback to localhost if DNS resolution fails
    print(f"Sending message to {udp_ip}")
    udp_port = 5000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (udp_ip, udp_port))
    sock.close()

class KeyCaptureWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Key Capture Window")
        self.setGeometry(100, 100, 400, 300)

    def keyPressEvent(self, event):
        if event.type() == QEvent.Type.KeyPress:
            key = event.key()
            key_name = QKeySequence(event.key()).toString()
            send_udp_message(key_name)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyCaptureWindow()
    window.show()
    sys.exit(app.exec())