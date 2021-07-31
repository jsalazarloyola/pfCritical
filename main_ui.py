# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainGuizFzwKP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UiMainWindow(object):
    def setup_ui(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
        main_window.resize(574, 518)
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"centralwidget")
        self.grid_layout_widget = QWidget(self.central_widget)
        self.grid_layout_widget.setObjectName(u"gridLayoutWidget")
        self.grid_layout_widget.setGeometry(QRect(10, 10, 551, 227))
        self.grid_layout = QGridLayout(self.grid_layout_widget)
        self.grid_layout.setObjectName(u"gridLayout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.magic_hit_btn = QPushButton(self.grid_layout_widget)
        self.magic_hit_btn.setObjectName(u"magic_hit_btn")

        self.grid_layout.addWidget(self.magic_hit_btn, 1, 3, 1, 1)

        self.magic_fumble_btn = QPushButton(self.grid_layout_widget)
        self.magic_fumble_btn.setObjectName(u"magic_fumble_btn")

        self.grid_layout.addWidget(self.magic_fumble_btn, 5, 3, 1, 1)

        self.critical_hit_label = QLabel(self.grid_layout_widget)
        self.critical_hit_label.setObjectName(u"critical_hit_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.critical_hit_label.setFont(font)

        self.grid_layout.addWidget(self.critical_hit_label, 0, 0, 1, 4)

        self.bludgeoning_btn = QPushButton(self.grid_layout_widget)
        self.bludgeoning_btn.setObjectName(u"bludgeoning_btn")
        self.bludgeoning_btn.setEnabled(True)

        self.grid_layout.addWidget(self.bludgeoning_btn, 1, 0, 1, 1)

        self.piercing_btn = QPushButton(self.grid_layout_widget)
        self.piercing_btn.setObjectName(u"piercing_btn")

        self.grid_layout.addWidget(self.piercing_btn, 1, 1, 1, 1)

        self.fumble_label = QLabel(self.grid_layout_widget)
        self.fumble_label.setObjectName(u"fumble_label")
        self.fumble_label.setFont(font)

        self.grid_layout.addWidget(self.fumble_label, 4, 0, 1, 4)

        self.ranged_btn = QPushButton(self.grid_layout_widget)
        self.ranged_btn.setObjectName(u"ranged_btn")

        self.grid_layout.addWidget(self.ranged_btn, 5, 1, 1, 1)

        self.slashing_btn = QPushButton(self.grid_layout_widget)
        self.slashing_btn.setObjectName(u"slashing_btn")

        self.grid_layout.addWidget(self.slashing_btn, 1, 2, 1, 1)

        self.melee_btn = QPushButton(self.grid_layout_widget)
        self.melee_btn.setObjectName(u"melee_btn")

        self.grid_layout.addWidget(self.melee_btn, 5, 0, 1, 1)

        self.natural_btn = QPushButton(self.grid_layout_widget)
        self.natural_btn.setObjectName(u"natural_btn")

        self.grid_layout.addWidget(self.natural_btn, 5, 2, 1, 1)

        self.crit_mult_x2 = QRadioButton(self.grid_layout_widget)
        self.crit_mult_x2.setObjectName(u"crit_mult_x2")
        self.crit_mult_x2.setChecked(True)

        self.grid_layout.addWidget(self.crit_mult_x2, 3, 0, 1, 1)

        self.crit_mult_x3 = QRadioButton(self.grid_layout_widget)
        self.crit_mult_x3.setObjectName(u"crit_mult_x3")

        self.grid_layout.addWidget(self.crit_mult_x3, 3, 1, 1, 1)

        self.label = QLabel(self.grid_layout_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.grid_layout.addWidget(self.label, 2, 0, 1, 4)

        self.crit_mult_x4 = QRadioButton(self.grid_layout_widget)
        self.crit_mult_x4.setObjectName(u"crit_mult_x4")

        self.grid_layout.addWidget(self.crit_mult_x4, 3, 2, 1, 1)

        self.results_box = QTextBrowser(self.central_widget)
        self.results_box.setObjectName(u"results_box")
        self.results_box.setEnabled(True)
        self.results_box.setGeometry(QRect(10, 250, 551, 241))
        font2 = QFont()
        font2.setPointSize(12)
        self.results_box.setFont(font2)
        main_window.setCentralWidget(self.central_widget)
        self.status_bar = QStatusBar(main_window)
        self.status_bar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.status_bar)

        self.retranslate_ui(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setup_ui

    def retranslate_ui(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cr\u00edticos para Pathfinder", None))
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
    # retranslate_ui

