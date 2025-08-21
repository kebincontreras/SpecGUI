# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acquisition_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(1227, 523)
        self.horizontalLayout_5 = QHBoxLayout(MainWidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.leftVLayout = QVBoxLayout()
        self.leftVLayout.setObjectName(u"leftVLayout")
        self.dividerLine1 = QFrame(MainWidget)
        self.dividerLine1.setObjectName(u"dividerLine1")
        self.dividerLine1.setFrameShape(QFrame.HLine)
        self.dividerLine1.setFrameShadow(QFrame.Sunken)

        self.leftVLayout.addWidget(self.dividerLine1)

        self.DeviceHLayout = QHBoxLayout()
        self.DeviceHLayout.setObjectName(u"DeviceHLayout")
        self.DeviceHLayout.setContentsMargins(-1, 0, -1, -1)
        self.WordDateLabel = QLabel(MainWidget)
        self.WordDateLabel.setObjectName(u"WordDateLabel")
        self.WordDateLabel.setMinimumSize(QSize(0, 30))
        self.WordDateLabel.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.WordDateLabel.setFont(font)

        self.DeviceHLayout.addWidget(self.WordDateLabel, 0, Qt.AlignRight)

        self.DateLabel = QLabel(MainWidget)
        self.DateLabel.setObjectName(u"DateLabel")
        self.DateLabel.setMinimumSize(QSize(155, 0))
        self.DateLabel.setMaximumSize(QSize(1616516, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.DateLabel.setFont(font1)
        self.DateLabel.setStyleSheet(u"*{\n"
"}\n"
"QLabel {\n"
"background:rgb(235, 235, 235);\n"
"border-color:rgb(240, 240, 240);\n"
"border-radius: 5px;\n"
"border-width: 2px;\n"
"}")
        self.DateLabel.setLineWidth(2)
        self.DateLabel.setAlignment(Qt.AlignCenter)
        self.DateLabel.setWordWrap(False)

        self.DeviceHLayout.addWidget(self.DateLabel, 0, Qt.AlignLeft)

        self.DeviceHLayout.setStretch(0, 2)
        self.DeviceHLayout.setStretch(1, 3)

        self.leftVLayout.addLayout(self.DeviceHLayout)

        self.dividerLine2 = QFrame(MainWidget)
        self.dividerLine2.setObjectName(u"dividerLine2")
        self.dividerLine2.setMaximumSize(QSize(16777215, 16777215))
        self.dividerLine2.setFrameShape(QFrame.HLine)
        self.dividerLine2.setFrameShadow(QFrame.Sunken)

        self.leftVLayout.addWidget(self.dividerLine2)

        self.integrationTimeVLayout = QVBoxLayout()
        self.integrationTimeVLayout.setObjectName(u"integrationTimeVLayout")
        self.intTimeHLayout1 = QHBoxLayout()
        self.intTimeHLayout1.setObjectName(u"intTimeHLayout1")
        self.intTimeHLayout1.setContentsMargins(-1, -1, -1, 0)
        self.integrationTimeLabel = QLabel(MainWidget)
        self.integrationTimeLabel.setObjectName(u"integrationTimeLabel")
        self.integrationTimeLabel.setMaximumSize(QSize(16777215, 31))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(False)
        self.integrationTimeLabel.setFont(font2)
        self.integrationTimeLabel.setAlignment(Qt.AlignCenter)

        self.intTimeHLayout1.addWidget(self.integrationTimeLabel)

        self.VISSpinBox = QSpinBox(MainWidget)
        self.VISSpinBox.setObjectName(u"VISSpinBox")
        self.VISSpinBox.setMinimumSize(QSize(150, 0))
        self.VISSpinBox.setMaximumSize(QSize(150, 25))
        self.VISSpinBox.setMinimum(10000)
        self.VISSpinBox.setMaximum(50000)
        self.VISSpinBox.setValue(10000)

        self.intTimeHLayout1.addWidget(self.VISSpinBox)

        self.intTimeHLayout1.setStretch(1, 4)

        self.integrationTimeVLayout.addLayout(self.intTimeHLayout1)


        self.leftVLayout.addLayout(self.integrationTimeVLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.RatioLabel = QLabel(MainWidget)
        self.RatioLabel.setObjectName(u"RatioLabel")
        self.RatioLabel.setMaximumSize(QSize(16777215, 31))
        self.RatioLabel.setFont(font2)

        self.horizontalLayout_2.addWidget(self.RatioLabel)

        self.RatiospinBox = QSpinBox(MainWidget)
        self.RatiospinBox.setObjectName(u"RatiospinBox")
        self.RatiospinBox.setMinimumSize(QSize(150, 0))
        self.RatiospinBox.setMaximumSize(QSize(150, 16777215))
        self.RatiospinBox.setMinimum(1)
        self.RatiospinBox.setMaximum(100)

        self.horizontalLayout_2.addWidget(self.RatiospinBox)


        self.leftVLayout.addLayout(self.horizontalLayout_2)

        self.line_3 = QFrame(MainWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.leftVLayout.addWidget(self.line_3)

        self.saveAsHLayout = QHBoxLayout()
        self.saveAsHLayout.setObjectName(u"saveAsHLayout")
        self.saveAsLabel = QLabel(MainWidget)
        self.saveAsLabel.setObjectName(u"saveAsLabel")
        self.saveAsLabel.setMinimumSize(QSize(0, 42))
        self.saveAsLabel.setMaximumSize(QSize(117, 45))
        self.saveAsLabel.setFont(font)
        self.saveAsLabel.setAlignment(Qt.AlignCenter)

        self.saveAsHLayout.addWidget(self.saveAsLabel)

        self.savelineEdit = QLineEdit(MainWidget)
        self.savelineEdit.setObjectName(u"savelineEdit")
        self.savelineEdit.setMinimumSize(QSize(0, 30))
        self.savelineEdit.setMaximumSize(QSize(16777215, 30))
        self.savelineEdit.setFont(font1)
        self.savelineEdit.setStyleSheet(u"*{\n"
"}\n"
"QLineEdit{\n"
"background:rgb(255, 255, 255);\n"
"border-color:rgb(240, 240, 240);\n"
"\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"border-top-right-radius: 0;\n"
"border-bottom-right-radius: 0;\n"
"\n"
"border-width: 2px;\n"
"}")

        self.saveAsHLayout.addWidget(self.savelineEdit)

        self.saveAsPushButton = QPushButton(MainWidget)
        self.saveAsPushButton.setObjectName(u"saveAsPushButton")
        self.saveAsPushButton.setMinimumSize(QSize(30, 30))
        self.saveAsPushButton.setMaximumSize(QSize(30, 30))
        self.saveAsPushButton.setStyleSheet(u"*{\n"
"}\n"
"QPushButton {\n"
"background:rgb(212, 237, 255);\n"
"border-top-left-radius: 0;\n"
"border-bottom-left-radius: 0;\n"
"border-top-right-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background:rgb(178, 209, 236);\n"
"}")
        icon = QIcon()
        icon.addFile(u"resources/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveAsPushButton.setIcon(icon)
        self.saveAsPushButton.setIconSize(QSize(20, 20))

        self.saveAsHLayout.addWidget(self.saveAsPushButton)

        self.saveAsAskLabel = QLabel(MainWidget)
        self.saveAsAskLabel.setObjectName(u"saveAsAskLabel")
        self.saveAsAskLabel.setMaximumSize(QSize(18, 18))
        self.saveAsAskLabel.setPixmap(QPixmap(u"resources/qs.png"))
        self.saveAsAskLabel.setScaledContents(True)

        self.saveAsHLayout.addWidget(self.saveAsAskLabel)


        self.leftVLayout.addLayout(self.saveAsHLayout)

        self.dividerLine4 = QFrame(MainWidget)
        self.dividerLine4.setObjectName(u"dividerLine4")
        self.dividerLine4.setMaximumSize(QSize(16777215, 18))
        self.dividerLine4.setFrameShape(QFrame.HLine)
        self.dividerLine4.setFrameShadow(QFrame.Sunken)

        self.leftVLayout.addWidget(self.dividerLine4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.executeButon = QPushButton(MainWidget)
        self.executeButon.setObjectName(u"executeButon")
        self.executeButon.setMinimumSize(QSize(150, 25))
        self.executeButon.setMaximumSize(QSize(170, 30))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        self.executeButon.setFont(font3)
        self.executeButon.setStyleSheet(u"*{\n"
"}\n"
"QPushButton {\n"
"	background:rgb(194, 248, 165);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(138, 226, 36);\n"
"	\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"    color:rgb(156, 156, 156);\n"
"	border: 0px solid rgb(180, 219, 255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.executeButon)

        self.stopButton = QPushButton(MainWidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(150, 25))
        self.stopButton.setMaximumSize(QSize(170, 30))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.stopButton.setFont(font4)
        self.stopButton.setStyleSheet(u"*{\n"
"}\n"
"QPushButton {\n"
"	background:rgb(255, 170, 172);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(226, 112, 142);\n"
"	\n"
"	\n"
"}\n"
"QPushButton:pressed {\n"
"    color:rgb(156, 156, 156);\n"
"	border: 0px solid rgb(180, 219, 255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.stopButton)


        self.leftVLayout.addLayout(self.horizontalLayout_6)

        self.line = QFrame(MainWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.leftVLayout.addWidget(self.line)

        self.metaDataVLayout = QVBoxLayout()
        self.metaDataVLayout.setObjectName(u"metaDataVLayout")
        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.metaDataVLayout.addItem(self.verticalSpacer)


        self.leftVLayout.addLayout(self.metaDataVLayout)


        self.horizontalLayout_5.addLayout(self.leftVLayout)

        self.line_2 = QFrame(MainWidget)
        self.line_2.setObjectName(u"line_2")
        font5 = QFont()
        font5.setPointSize(8)
        self.line_2.setFont(font5)
        self.line_2.setFrameShadow(QFrame.Raised)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.VLine)

        self.horizontalLayout_5.addWidget(self.line_2)

        self.figureWidget = QWidget(MainWidget)
        self.figureWidget.setObjectName(u"figureWidget")
        self.verticalLayout = QVBoxLayout(self.figureWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.figureVLayout = QVBoxLayout()
        self.figureVLayout.setObjectName(u"figureVLayout")
        self.figureVLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.figureVLayout.setContentsMargins(0, -1, -1, 0)

        self.verticalLayout.addLayout(self.figureVLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(self.figureWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 20))
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.restTimeLabel = QLabel(self.figureWidget)
        self.restTimeLabel.setObjectName(u"restTimeLabel")
        font6 = QFont()
        font6.setBold(True)
        self.restTimeLabel.setFont(font6)

        self.verticalLayout_3.addWidget(self.restTimeLabel, 0, Qt.AlignHCenter)

        self.restTimeValueLabel = QLabel(self.figureWidget)
        self.restTimeValueLabel.setObjectName(u"restTimeValueLabel")

        self.verticalLayout_3.addWidget(self.restTimeValueLabel, 0, Qt.AlignHCenter)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.InfoLabel = QLabel(self.figureWidget)
        self.InfoLabel.setObjectName(u"InfoLabel")
        self.InfoLabel.setMaximumSize(QSize(16777215, 40))
        self.InfoLabel.setStyleSheet(u"QLabel {\n"
"    background-color: #ffffff; /* Fondo blanco */\n"
"    border: 1px solid #ccc; /* Borde gris de 2px */\n"
"    border-radius: 10px; /* Bordes semi-redondos */\n"
"    color: #000; /* Color del texto (negro) */\n"
"    padding: 4px; /* Espaciado interno del QLabel */\n"
"    font-size: 10px; /* Tama\u00f1o de fuente */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.InfoLabel)

        self.verticalLayout.setStretch(0, 20)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)

        self.horizontalLayout_5.addWidget(self.figureWidget)

        self.horizontalLayout_5.setStretch(2, 10)

        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Widget", None))
        self.WordDateLabel.setText(QCoreApplication.translate("MainWidget", u"Fecha", None))
        self.DateLabel.setText(QCoreApplication.translate("MainWidget", u"25/07/2023", None))
        self.integrationTimeLabel.setText(QCoreApplication.translate("MainWidget", u"Tiempo de Integraci\u00f3n", None))
        self.VISSpinBox.setSuffix(QCoreApplication.translate("MainWidget", u" ms", None))
        self.RatioLabel.setText(QCoreApplication.translate("MainWidget", u"Radio de Compresi\u00f3n", None))
        self.RatiospinBox.setSuffix(QCoreApplication.translate("MainWidget", u"%", None))
        self.saveAsLabel.setText(QCoreApplication.translate("MainWidget", u"Guardar como", None))
        self.saveAsPushButton.setText("")
#if QT_CONFIG(tooltip)
        self.saveAsAskLabel.setToolTip(QCoreApplication.translate("MainWidget", u"El guardado de datos sigue este patr\u00f3n:\n"
"\n"
"- coded_apertures(.npy, .pkl, .mat). Este archivo contendr\u00e1 un array de shape (S, M, N), donde\n"
"    S es el n\u00famero de c\u00f3digos de apertura, M y N son las dimensiones de los c\u00f3digos de apertura.\n"
"    \n"
"- samples(.npz, .pkl, .mat). Este archivo contendr\u00e1 un diccionario con las siguientes claves:\n"
"    - 'measurements': array de shape (shots, numero de bandas)\n"
"    - 'wavelengths': array de shape (numero de bandas,)", None))
#endif // QT_CONFIG(tooltip)
        self.saveAsAskLabel.setText("")
        self.executeButon.setText(QCoreApplication.translate("MainWidget", u"Ejecutar", None))
        self.stopButton.setText(QCoreApplication.translate("MainWidget", u"Detener", None))
        self.restTimeLabel.setText(QCoreApplication.translate("MainWidget", u"Tiempo restante", None))
        self.restTimeValueLabel.setText(QCoreApplication.translate("MainWidget", u"30s", None))
        self.InfoLabel.setText(QCoreApplication.translate("MainWidget", u"TextLabel", None))
    # retranslateUi

