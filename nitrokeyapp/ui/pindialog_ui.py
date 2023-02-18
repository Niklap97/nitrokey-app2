# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pindialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PinDialog(object):
    def setupUi(self, PinDialog):
        PinDialog.setObjectName("PinDialog")
        PinDialog.resize(358, 155)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PinDialog.sizePolicy().hasHeightForWidth())
        PinDialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/new/icon_NK.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PinDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(PinDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(PinDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setMaxLength(39)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(PinDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.status = QtWidgets.QLabel(PinDialog)
        self.status.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.status.setText("TextLabel")
        self.status.setObjectName("status")
        self.horizontalLayout.addWidget(self.status)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cancelButton = QtWidgets.QPushButton(PinDialog)
        self.cancelButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.cancelButton.setAutoDefault(False)
        self.cancelButton.setDefault(False)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.okButton = QtWidgets.QPushButton(PinDialog)
        self.okButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.okButton.setAutoDefault(True)
        self.okButton.setDefault(True)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(PinDialog)
        self.cancelButton.clicked.connect(PinDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(PinDialog)
        PinDialog.setTabOrder(self.lineEdit, self.checkBox)

    def retranslateUi(self, PinDialog):
        _translate = QtCore.QCoreApplication.translate
        PinDialog.setWindowTitle(_translate("PinDialog", "Password dialog"))
        self.label.setText(_translate("PinDialog", "Enter card password:"))
        self.lineEdit.setAccessibleName(_translate("PinDialog", "Enter card PIN"))
        self.checkBox.setText(_translate("PinDialog", "Show password"))
        self.cancelButton.setText(_translate("PinDialog", "&Cancel"))
        self.okButton.setText(_translate("PinDialog", "&OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PinDialog = QtWidgets.QDialog()
    ui = Ui_PinDialog()
    ui.setupUi(PinDialog)
    PinDialog.show()
    sys.exit(app.exec_())
