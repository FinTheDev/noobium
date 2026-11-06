import sys

from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QAction, QKeySequence

class Noobium(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Noobium")
        self.resize(1200, 800)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.example.com"))

        self.setCentralWidget(self.browser)

        close_shortcut = QAction(self)
        close_shortcut.setShortcut(QKeySequence("Ctrl+Q"))
        close_shortcut.triggered.connect(self.close)
        self.addAction(close_shortcut)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Noobium")

    window = Noobium()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
