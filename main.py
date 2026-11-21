import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtWebEngineWidgets import QWebEngineView


class SandBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Sand Browser")
        self.resize(1024, 720)

        # Central container widget required by QMainWindow
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layouts
        main_layout = QVBoxLayout()
        nav_layout = QHBoxLayout()

        # Navigation controls
        self.back_btn = QPushButton("<")
        self.back_btn.setFixedHeight(30)
        self.back_btn.setFixedWidth(36)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setFixedHeight(30)
        self.forward_btn.setFixedWidth(36)

        self.url_bar = QLineEdit()
        self.url_bar.setFixedHeight(30)
        self.url_bar.setPlaceholderText("Enter a URL and press Enter or click Go...")

        self.go_btn = QPushButton("Go")
        self.go_btn.setFixedHeight(30)

        nav_layout.addWidget(self.back_btn)
        nav_layout.addWidget(self.forward_btn)
        nav_layout.addWidget(self.url_bar)
        nav_layout.addWidget(self.go_btn)

        # Web engine view
        self.browser = QWebEngineView()
        start_url = "https://duckduckgo.com/"
        self.url_bar.setText(start_url)
        self.browser.setUrl(QUrl(start_url))

        # Assemble main layout
        main_layout.addLayout(nav_layout)
        main_layout.addWidget(self.browser)
        central_widget.setLayout(main_layout)

        # Connect signals to slots (make controls actually work)
        self.go_btn.clicked.connect(self.navigate_to_url)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.browser.urlChanged.connect(self.update_url_bar)

    def navigate_to_url(self):
        raw_text = self.url_bar.text().strip()
        if not raw_text:
            return
        if not raw_text.startswith(("http://", "https://")):
            raw_text = "https://" + raw_text
        self.browser.setUrl(QUrl(raw_text))

    def update_url_bar(self, qurl: QUrl):
        self.url_bar.setText(qurl.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SandBrowser()
    window.show()
    sys.exit(app.exec_())
