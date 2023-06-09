from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSlider, QLabel, QVBoxLayout, QDialogButtonBox

class UiRangeSlider:
    def setup_ui(self, Dialog):
        Dialog.resize(289, 72)
        self.slider_max = QSlider(Qt.Horizontal)
        self.slider_max.setMinimum(0)
        self.slider_max.setMaximum(255)
        self.slider_max.setValue(127)

        self.label_max = QLabel()
        self.label_max.setText("Max: 127")
        self.label_image = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.slider_max)
        layout.addWidget(self.label_max)
        layout.addWidget(self.label_image)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

        layout.addWidget(self.buttons)
        self.setLayout(layout)

