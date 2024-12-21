# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ltranslator.ui'
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
        MainWindow.resize(622, 990)
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bu_switch = QPushButton(self.centralwidget)
        self.bu_switch.setObjectName(u"bu_switch")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bu_switch.sizePolicy().hasHeightForWidth())
        self.bu_switch.setSizePolicy(sizePolicy)
        self.bu_switch.setMaximumSize(QSize(50, 16777215))
        self.bu_switch.setCheckable(True)
        self.bu_switch.setChecked(True)

        self.verticalLayout_2.addWidget(self.bu_switch)

        self.bu_top = QPushButton(self.centralwidget)
        self.bu_top.setObjectName(u"bu_top")
        sizePolicy.setHeightForWidth(self.bu_top.sizePolicy().hasHeightForWidth())
        self.bu_top.setSizePolicy(sizePolicy)
        self.bu_top.setMaximumSize(QSize(50, 16777215))
        self.bu_top.setCheckable(True)
        self.bu_top.setChecked(False)

        self.verticalLayout_2.addWidget(self.bu_top)

        self.bu_scroll = QPushButton(self.centralwidget)
        self.bu_scroll.setObjectName(u"bu_scroll")
        sizePolicy.setHeightForWidth(self.bu_scroll.sizePolicy().hasHeightForWidth())
        self.bu_scroll.setSizePolicy(sizePolicy)
        self.bu_scroll.setMaximumSize(QSize(50, 16777215))
        self.bu_scroll.setCheckable(True)
        self.bu_scroll.setChecked(True)

        self.verticalLayout_2.addWidget(self.bu_scroll)

        self.bu_summary = QPushButton(self.centralwidget)
        self.bu_summary.setObjectName(u"bu_summary")
        sizePolicy.setHeightForWidth(self.bu_summary.sizePolicy().hasHeightForWidth())
        self.bu_summary.setSizePolicy(sizePolicy)
        self.bu_summary.setMaximumSize(QSize(50, 16777215))
        self.bu_summary.setCheckable(True)
        self.bu_summary.setChecked(False)

        self.verticalLayout_2.addWidget(self.bu_summary)

        self.bu_send = QPushButton(self.centralwidget)
        self.bu_send.setObjectName(u"bu_send")
        sizePolicy.setHeightForWidth(self.bu_send.sizePolicy().hasHeightForWidth())
        self.bu_send.setSizePolicy(sizePolicy)
        self.bu_send.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_2.addWidget(self.bu_send)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.bu_clear = QPushButton(self.centralwidget)
        self.bu_clear.setObjectName(u"bu_clear")
        sizePolicy.setHeightForWidth(self.bu_clear.sizePolicy().hasHeightForWidth())
        self.bu_clear.setSizePolicy(sizePolicy)
        self.bu_clear.setMaximumSize(QSize(50, 16777215))

        self.verticalLayout_2.addWidget(self.bu_clear)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.layout_title = QHBoxLayout()
        self.layout_title.setObjectName(u"layout_title")
        self.label_title = QLabel(self.tab_3)
        self.label_title.setObjectName(u"label_title")

        self.layout_title.addWidget(self.label_title)

        self.text_title = QLineEdit(self.tab_3)
        self.text_title.setObjectName(u"text_title")

        self.layout_title.addWidget(self.text_title)


        self.verticalLayout_5.addLayout(self.layout_title)

        self.layout_subject = QHBoxLayout()
        self.layout_subject.setObjectName(u"layout_subject")
        self.label_subject = QLabel(self.tab_3)
        self.label_subject.setObjectName(u"label_subject")

        self.layout_subject.addWidget(self.label_subject)

        self.text_subject = QComboBox(self.tab_3)
        self.text_subject.setObjectName(u"text_subject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_subject.sizePolicy().hasHeightForWidth())
        self.text_subject.setSizePolicy(sizePolicy1)
        self.text_subject.setEditable(True)

        self.layout_subject.addWidget(self.text_subject)


        self.verticalLayout_5.addLayout(self.layout_subject)

        self.bu_fold = QPushButton(self.tab_3)
        self.bu_fold.setObjectName(u"bu_fold")
        self.bu_fold.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.bu_fold)

        self.text_content = QPlainTextEdit(self.tab_3)
        self.text_content.setObjectName(u"text_content")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.text_content.sizePolicy().hasHeightForWidth())
        self.text_content.setSizePolicy(sizePolicy2)
        self.text_content.setMaximumSize(QSize(16777215, 16777215))
        self.text_content.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_5.addWidget(self.text_content)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.text_translation = QTextBrowser(self.tab)
        self.text_translation.setObjectName(u"text_translation")
        self.text_translation.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_3.addWidget(self.text_translation)

        self.text_summary = QTextBrowser(self.tab)
        self.text_summary.setObjectName(u"text_summary")
        sizePolicy1.setHeightForWidth(self.text_summary.sizePolicy().hasHeightForWidth())
        self.text_summary.setSizePolicy(sizePolicy1)
        self.text_summary.setMaximumSize(QSize(16777215, 150))
        self.text_summary.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_3.addWidget(self.text_summary)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.text_config = QComboBox(self.tab_2)
        self.text_config.setObjectName(u"text_config")
        sizePolicy1.setHeightForWidth(self.text_config.sizePolicy().hasHeightForWidth())
        self.text_config.setSizePolicy(sizePolicy1)
        self.text_config.setEditable(False)

        self.horizontalLayout_5.addWidget(self.text_config)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.text_url = QLineEdit(self.tab_2)
        self.text_url.setObjectName(u"text_url")

        self.horizontalLayout_7.addWidget(self.text_url)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.text_model = QLineEdit(self.tab_2)
        self.text_model.setObjectName(u"text_model")

        self.horizontalLayout_6.addWidget(self.text_model)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.text_key = QLineEdit(self.tab_2)
        self.text_key.setObjectName(u"text_key")

        self.horizontalLayout_8.addWidget(self.text_key)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_10.addWidget(self.label_9)

        self.bu_save_config = QPushButton(self.tab_2)
        self.bu_save_config.setObjectName(u"bu_save_config")
        sizePolicy.setHeightForWidth(self.bu_save_config.sizePolicy().hasHeightForWidth())
        self.bu_save_config.setSizePolicy(sizePolicy)
        self.bu_save_config.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_10.addWidget(self.bu_save_config)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.text_config_file = QPlainTextEdit(self.tab_2)
        self.text_config_file.setObjectName(u"text_config_file")

        self.verticalLayout_4.addWidget(self.text_config_file)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.bu_send.clicked.connect(MainWindow.send)
        self.bu_top.clicked.connect(MainWindow.change_top)
        self.text_config.currentIndexChanged.connect(MainWindow.change_config)
        self.bu_summary.clicked.connect(MainWindow.change_summary)
        self.bu_save_config.clicked.connect(MainWindow.save_config)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ltranslator", None))
        self.bu_switch.setText(QCoreApplication.translate("MainWindow", u"\u5f00", None))
        self.bu_top.setText(QCoreApplication.translate("MainWindow", u"\u7f6e\u9876", None))
        self.bu_scroll.setText(QCoreApplication.translate("MainWindow", u"\u6eda\u52a8", None))
        self.bu_summary.setText(QCoreApplication.translate("MainWindow", u"\u6458\u8981", None))
        self.bu_send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.bu_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"\u6807\u9898", None))
        self.label_subject.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u79d1", None))
        self.bu_fold.setText(QCoreApplication.translate("MainWindow", u"\ufe3f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u539f\u6587", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u8bd1\u6587", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6a21\u578b\u670d\u52a1\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"api\u5730\u5740\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u540d\u79f0\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"api key\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u6587\u4ef6\uff1a", None))
        self.bu_save_config.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
    # retranslateUi

