# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainGuiyHyRIC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc


class UiMainWindow(object):
    def setup_ui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(495, 554)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 471, 199))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.magic_hit_btn = QPushButton(self.gridLayoutWidget)
        self.magic_hit_btn.setObjectName(u"magic_hit_btn")
        icon = QIcon()
        icon.addFile(u":/icon/assets/magic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.magic_hit_btn.setIcon(icon)

        self.gridLayout.addWidget(self.magic_hit_btn, 1, 3, 1, 1)

        self.magic_fumble_btn = QPushButton(self.gridLayoutWidget)
        self.magic_fumble_btn.setObjectName(u"magic_fumble_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icon/assets/magic_fumble.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.magic_fumble_btn.setIcon(icon1)

        self.gridLayout.addWidget(self.magic_fumble_btn, 5, 3, 1, 1)

        self.critical_hit_label = QLabel(self.gridLayoutWidget)
        self.critical_hit_label.setObjectName(u"critical_hit_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.critical_hit_label.setFont(font)

        self.gridLayout.addWidget(self.critical_hit_label, 0, 0, 1, 4)

        self.bludgeoning_btn = QPushButton(self.gridLayoutWidget)
        self.bludgeoning_btn.setObjectName(u"bludgeoning_btn")
        self.bludgeoning_btn.setEnabled(True)
        icon2 = QIcon()
        icon2.addFile(u":/icon/assets/bludgeoning.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bludgeoning_btn.setIcon(icon2)

        self.gridLayout.addWidget(self.bludgeoning_btn, 1, 0, 1, 1)

        self.piercing_btn = QPushButton(self.gridLayoutWidget)
        self.piercing_btn.setObjectName(u"piercing_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icon/assets/piercing.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.piercing_btn.setIcon(icon3)

        self.gridLayout.addWidget(self.piercing_btn, 1, 1, 1, 1)

        self.fumble_label = QLabel(self.gridLayoutWidget)
        self.fumble_label.setObjectName(u"fumble_label")
        self.fumble_label.setFont(font)

        self.gridLayout.addWidget(self.fumble_label, 4, 0, 1, 4)

        self.ranged_btn = QPushButton(self.gridLayoutWidget)
        self.ranged_btn.setObjectName(u"ranged_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icon/assets/ranged.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ranged_btn.setIcon(icon4)

        self.gridLayout.addWidget(self.ranged_btn, 5, 1, 1, 1)

        self.slashing_btn = QPushButton(self.gridLayoutWidget)
        self.slashing_btn.setObjectName(u"slashing_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icon/assets/slashing.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.slashing_btn.setIcon(icon5)

        self.gridLayout.addWidget(self.slashing_btn, 1, 2, 1, 1)

        self.melee_btn = QPushButton(self.gridLayoutWidget)
        self.melee_btn.setObjectName(u"melee_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icon/assets/melee.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.melee_btn.setIcon(icon6)

        self.gridLayout.addWidget(self.melee_btn, 5, 0, 1, 1)

        self.natural_btn = QPushButton(self.gridLayoutWidget)
        self.natural_btn.setObjectName(u"natural_btn")
        icon7 = QIcon()
        icon7.addFile(u":/icon/assets/natural.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.natural_btn.setIcon(icon7)

        self.gridLayout.addWidget(self.natural_btn, 5, 2, 1, 1)

        self.crit_mult_x2 = QRadioButton(self.gridLayoutWidget)
        self.crit_mult_x2.setObjectName(u"crit_mult_x2")
        self.crit_mult_x2.setChecked(True)

        self.gridLayout.addWidget(self.crit_mult_x2, 3, 0, 1, 1)

        self.crit_mult_x3 = QRadioButton(self.gridLayoutWidget)
        self.crit_mult_x3.setObjectName(u"crit_mult_x3")

        self.gridLayout.addWidget(self.crit_mult_x3, 3, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 4)

        self.crit_mult_x4 = QRadioButton(self.gridLayoutWidget)
        self.crit_mult_x4.setObjectName(u"crit_mult_x4")

        self.gridLayout.addWidget(self.crit_mult_x4, 3, 2, 1, 1)

        self.results_box = QTextBrowser(self.centralwidget)
        self.results_box.setObjectName(u"results_box")
        self.results_box.setEnabled(True)
        self.results_box.setGeometry(QRect(10, 210, 471, 321))
        font2 = QFont()
        font2.setPointSize(12)
        self.results_box.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cr\u00edticos para Pathfinder", None))
        self.magic_hit_btn.setText(QCoreApplication.translate("MainWindow", u"Magia", None))
        self.magic_fumble_btn.setText(QCoreApplication.translate("MainWindow", u"Magia", None))
        self.critical_hit_label.setText(QCoreApplication.translate("MainWindow", u"Cr\u00edticos", None))
        self.bludgeoning_btn.setText(QCoreApplication.translate("MainWindow", u"Contundente", None))
        self.piercing_btn.setText(QCoreApplication.translate("MainWindow", u"Penetrante", None))
        self.fumble_label.setText(QCoreApplication.translate("MainWindow", u"Pifias", None))
        self.ranged_btn.setText(QCoreApplication.translate("MainWindow", u"A distancia", None))
        self.slashing_btn.setText(QCoreApplication.translate("MainWindow", u"Cortante", None))
        self.melee_btn.setText(QCoreApplication.translate("MainWindow", u"Cuerpo a cuerpo", None))
        self.natural_btn.setText(QCoreApplication.translate("MainWindow", u"Ataque natural", None))
        self.crit_mult_x2.setText(QCoreApplication.translate("MainWindow", u"x2", None))
        self.crit_mult_x3.setText(QCoreApplication.translate("MainWindow", u"x3", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Multiplicador", None))
        self.crit_mult_x4.setText(QCoreApplication.translate("MainWindow", u"x4", None))
    # retranslateUi

