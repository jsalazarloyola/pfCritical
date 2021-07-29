# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainGuianJtPE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiMainWindow(object):
    def setup_ui(self, main_window: QMainWindow):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(574, 278)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 551, 142))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.slashing_btn = QPushButton(self.gridLayoutWidget)
        self.slashing_btn.setObjectName(u"slashing_btn")

        self.gridLayout.addWidget(self.slashing_btn, 1, 2, 1, 1)

        self.bludgeoning_btn = QPushButton(self.gridLayoutWidget)
        self.bludgeoning_btn.setObjectName(u"bludgeoning_btn")

        self.gridLayout.addWidget(self.bludgeoning_btn, 1, 0, 1, 1)

        self.piercing_btn = QPushButton(self.gridLayoutWidget)
        self.piercing_btn.setObjectName(u"piercing_btn")

        self.gridLayout.addWidget(self.piercing_btn, 1, 1, 1, 1)

        self.magic_hit_btn = QPushButton(self.gridLayoutWidget)
        self.magic_hit_btn.setObjectName(u"magic_hit_btn")

        self.gridLayout.addWidget(self.magic_hit_btn, 1, 3, 1, 1)

        self.critical_hit_label = QLabel(self.gridLayoutWidget)
        self.critical_hit_label.setObjectName(u"critical_hit_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.critical_hit_label.setFont(font)

        self.gridLayout.addWidget(self.critical_hit_label, 0, 0, 1, 4)

        self.fumble_label = QLabel(self.gridLayoutWidget)
        self.fumble_label.setObjectName(u"fumble_label")
        self.fumble_label.setFont(font)

        self.gridLayout.addWidget(self.fumble_label, 2, 0, 1, 4)

        self.melee_btn = QPushButton(self.gridLayoutWidget)
        self.melee_btn.setObjectName(u"melee_btn")

        self.gridLayout.addWidget(self.melee_btn, 3, 0, 1, 1)

        self.ranged_btn = QPushButton(self.gridLayoutWidget)
        self.ranged_btn.setObjectName(u"ranged_btn")

        self.gridLayout.addWidget(self.ranged_btn, 3, 1, 1, 1)

        self.natural_btn = QPushButton(self.gridLayoutWidget)
        self.natural_btn.setObjectName(u"natural_btn")

        self.gridLayout.addWidget(self.natural_btn, 3, 2, 1, 1)

        self.magic_fumble_btn = QPushButton(self.gridLayoutWidget)
        self.magic_fumble_btn.setObjectName(u"magic_fumble_btn")

        self.gridLayout.addWidget(self.magic_fumble_btn, 3, 3, 1, 1)

        self.results_box = QTextBrowser(self.centralwidget)
        self.results_box.setObjectName(u"results_box")
        self.results_box.setGeometry(QRect(10, 160, 551, 91))
        font1 = QFont()
        font1.setPointSize(12)
        self.results_box.setFont(font1)
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cr\u00edticos para Pathfinder", None))
        self.slashing_btn.setText(QCoreApplication.translate("MainWindow", u"Cortante", None))
        self.bludgeoning_btn.setText(QCoreApplication.translate("MainWindow", u"Contundente", None))
        self.piercing_btn.setText(QCoreApplication.translate("MainWindow", u"Penetrante", None))
        self.magic_hit_btn.setText(QCoreApplication.translate("MainWindow", u"Magia", None))
        self.critical_hit_label.setText(QCoreApplication.translate("MainWindow", u"Cr\u00edticos", None))
        self.fumble_label.setText(QCoreApplication.translate("MainWindow", u"Pifias", None))
        self.melee_btn.setText(QCoreApplication.translate("MainWindow", u"Cuerpo a cuerpo", None))
        self.ranged_btn.setText(QCoreApplication.translate("MainWindow", u"A distancia", None))
        self.natural_btn.setText(QCoreApplication.translate("MainWindow", u"Ataque natural", None))
        self.magic_fumble_btn.setText(QCoreApplication.translate("MainWindow", u"Magia", None))
    # retranslate_ui

