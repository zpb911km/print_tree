# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 720)
        self.horizontalLayout_2 = QHBoxLayout(MainWindow)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.InputLayout = QVBoxLayout()
        self.InputLayout.setObjectName(u"InputLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.InputLayout.addItem(self.verticalSpacer_2)

        self.InputBox = QPlainTextEdit(MainWindow)
        self.InputBox.setObjectName(u"InputBox")
        font = QFont()
        font.setFamily(u"Cascadia Mono")
        self.InputBox.setFont(font)
        self.InputBox.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))

        self.InputLayout.addWidget(self.InputBox)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.InputLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.InputLayout)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.OperationLayout = QVBoxLayout()
        self.OperationLayout.setObjectName(u"OperationLayout")
        self.verticalSpacer_5 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.OperationLayout.addItem(self.verticalSpacer_5)

        self.ButtonGroup_1 = QGroupBox(MainWindow)
        self.ButtonGroup_1.setObjectName(u"ButtonGroup_1")
        self.verticalLayout = QVBoxLayout(self.ButtonGroup_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.AutoTransCheckBox = QCheckBox(self.ButtonGroup_1)
        self.AutoTransCheckBox.setObjectName(u"AutoTransCheckBox")
        self.AutoTransCheckBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.AutoTransCheckBox)

        self.TransformationButton = QPushButton(self.ButtonGroup_1)
        self.TransformationButton.setObjectName(u"TransformationButton")
        self.TransformationButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.TransformationButton)


        self.OperationLayout.addWidget(self.ButtonGroup_1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.OperationLayout.addItem(self.verticalSpacer_7)

        self.ButtonGroup_2 = QGroupBox(MainWindow)
        self.ButtonGroup_2.setObjectName(u"ButtonGroup_2")
        self.verticalLayout_3 = QVBoxLayout(self.ButtonGroup_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox = QCheckBox(self.ButtonGroup_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.checkBox)

        self.spinBox = QSpinBox(self.ButtonGroup_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(2147483647)
        self.spinBox.setValue(30)

        self.verticalLayout_3.addWidget(self.spinBox)


        self.OperationLayout.addWidget(self.ButtonGroup_2)

        self.verticalSpacer_6 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.OperationLayout.addItem(self.verticalSpacer_6)


        self.horizontalLayout_2.addLayout(self.OperationLayout)

        self.horizontalSpacer_4 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.OutputLayout = QVBoxLayout()
        self.OutputLayout.setObjectName(u"OutputLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.OutputLayout.addItem(self.verticalSpacer_3)

        self.OutputBox = QPlainTextEdit(MainWindow)
        self.OutputBox.setObjectName(u"OutputBox")
        font1 = QFont()
        font1.setFamily(u"Cascadia Code")
        self.OutputBox.setFont(font1)
        self.OutputBox.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.OutputBox.setReadOnly(True)

        self.OutputLayout.addWidget(self.OutputBox)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.OutputLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout_2.addLayout(self.OutputLayout)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.retranslateUi(MainWindow)
        self.checkBox.toggled.connect(self.spinBox.setEnabled)
        self.AutoTransCheckBox.toggled.connect(self.TransformationButton.setDisabled)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.InputBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u8f93\u5165\u2026\u2026", None))
        self.AutoTransCheckBox.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u8f6c\u6362", None))
        self.TransformationButton.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6\u9650\u5236", None))
    # retranslateUi

