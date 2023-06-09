from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget


class ui_combo_boxes:
    def setup_ui(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 205)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.comboBoxTypes = QtWidgets.QComboBox(Dialog)
        self.comboBoxTypes.setGeometry(QtCore.QRect(70, 40, 141, 22))
        self.comboBoxTypes.setObjectName("comboBox")
        self.comboBoxKernelSize = QtWidgets.QComboBox(Dialog)
        self.comboBoxKernelSize.setGeometry(QtCore.QRect(300, 40, 61, 22))
        self.comboBoxKernelSize.setObjectName("comboBox_2")
        self.labelType = QtWidgets.QLabel(Dialog)
        self.labelType.setGeometry(QtCore.QRect(10, 40, 49, 16))
        self.labelType.setObjectName("label_type")
        self.label_kernel_size = QtWidgets.QLabel(Dialog)
        self.label_kernel_size.setGeometry(QtCore.QRect(220, 40, 71, 16))
        self.label_kernel_size.setObjectName("label_kernel_size")
        self.label_image = QtWidgets.QLabel(Dialog)
        self.label_image.setGeometry(QtCore.QRect(180, 80, 49, 16))
        self.label_image.setObjectName("label_3")

        layout_combo_box = QHBoxLayout()

        layout_combo_box.addWidget(self.labelType)
        layout_combo_box.addWidget(self.comboBoxTypes)
        layout_combo_box.addWidget(self.label_kernel_size)
        layout_combo_box.addWidget(self.comboBoxKernelSize)

        layout = QVBoxLayout()
        layout.addLayout(layout_combo_box)
        layout.addWidget(self.label_image)
        layout.addWidget(self.buttonBox)

        self.setLayout(layout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelType.setText(_translate("Dialog", "Blur Type"))
        self.label_kernel_size.setText(_translate("Dialog", "Kernel Size:"))


