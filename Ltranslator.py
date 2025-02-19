# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ltranslator.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 900)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/翻译.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bu_switch = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bu_switch.sizePolicy().hasHeightForWidth())
        self.bu_switch.setSizePolicy(sizePolicy)
        self.bu_switch.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bu_switch.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/开关.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bu_switch.setIcon(icon1)
        self.bu_switch.setIconSize(QtCore.QSize(20, 20))
        self.bu_switch.setCheckable(True)
        self.bu_switch.setChecked(True)
        self.bu_switch.setObjectName("bu_switch")
        self.verticalLayout_2.addWidget(self.bu_switch)
        self.bu_top = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bu_top.sizePolicy().hasHeightForWidth())
        self.bu_top.setSizePolicy(sizePolicy)
        self.bu_top.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bu_top.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/去顶部.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bu_top.setIcon(icon2)
        self.bu_top.setIconSize(QtCore.QSize(20, 20))
        self.bu_top.setCheckable(True)
        self.bu_top.setChecked(False)
        self.bu_top.setObjectName("bu_top")
        self.verticalLayout_2.addWidget(self.bu_top)
        self.bu_scroll = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bu_scroll.sizePolicy().hasHeightForWidth())
        self.bu_scroll.setSizePolicy(sizePolicy)
        self.bu_scroll.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bu_scroll.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/跑步机1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bu_scroll.setIcon(icon3)
        self.bu_scroll.setIconSize(QtCore.QSize(20, 20))
        self.bu_scroll.setCheckable(True)
        self.bu_scroll.setChecked(True)
        self.bu_scroll.setObjectName("bu_scroll")
        self.verticalLayout_2.addWidget(self.bu_scroll)
        self.bu_summary = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bu_summary.sizePolicy().hasHeightForWidth())
        self.bu_summary.setSizePolicy(sizePolicy)
        self.bu_summary.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bu_summary.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/压缩.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bu_summary.setIcon(icon4)
        self.bu_summary.setIconSize(QtCore.QSize(20, 20))
        self.bu_summary.setCheckable(True)
        self.bu_summary.setChecked(False)
        self.bu_summary.setObjectName("bu_summary")
        self.verticalLayout_2.addWidget(self.bu_summary)
        self.bu_send = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bu_send.sizePolicy().hasHeightForWidth())
        self.bu_send.setSizePolicy(sizePolicy)
        self.bu_send.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bu_send.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/发送.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bu_send.setIcon(icon5)
        self.bu_send.setIconSize(QtCore.QSize(20, 20))
        self.bu_send.setObjectName("bu_send")
        self.verticalLayout_2.addWidget(self.bu_send)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.layout_title = QtWidgets.QHBoxLayout()
        self.layout_title.setObjectName("layout_title")
        self.label_title = QtWidgets.QLabel(self.tab_3)
        self.label_title.setObjectName("label_title")
        self.layout_title.addWidget(self.label_title)
        self.text_title = QtWidgets.QLineEdit(self.tab_3)
        self.text_title.setObjectName("text_title")
        self.layout_title.addWidget(self.text_title)
        self.verticalLayout_5.addLayout(self.layout_title)
        self.layout_subject = QtWidgets.QHBoxLayout()
        self.layout_subject.setObjectName("layout_subject")
        self.label_subject = QtWidgets.QLabel(self.tab_3)
        self.label_subject.setObjectName("label_subject")
        self.layout_subject.addWidget(self.label_subject)
        self.text_subject = QtWidgets.QComboBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_subject.sizePolicy().hasHeightForWidth())
        self.text_subject.setSizePolicy(sizePolicy)
        self.text_subject.setEditable(True)
        self.text_subject.setObjectName("text_subject")
        self.layout_subject.addWidget(self.text_subject)
        self.verticalLayout_5.addLayout(self.layout_subject)
        self.bu_fold = QtWidgets.QPushButton(self.tab_3)
        self.bu_fold.setMaximumSize(QtCore.QSize(16777215, 20))
        self.bu_fold.setObjectName("bu_fold")
        self.verticalLayout_5.addWidget(self.bu_fold)
        self.text_content = QtWidgets.QPlainTextEdit(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_content.sizePolicy().hasHeightForWidth())
        self.text_content.setSizePolicy(sizePolicy)
        self.text_content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text_content.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.text_content.setObjectName("text_content")
        self.verticalLayout_5.addWidget(self.text_content)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.text_translation = QtWidgets.QTextBrowser(self.tab)
        self.text_translation.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.text_translation.setObjectName("text_translation")
        self.verticalLayout_3.addWidget(self.text_translation)
        self.text_summary = QtWidgets.QTextBrowser(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_summary.sizePolicy().hasHeightForWidth())
        self.text_summary.setSizePolicy(sizePolicy)
        self.text_summary.setMaximumSize(QtCore.QSize(16777215, 150))
        self.text_summary.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.text_summary.setObjectName("text_summary")
        self.verticalLayout_3.addWidget(self.text_summary)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.text_config = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_config.sizePolicy().hasHeightForWidth())
        self.text_config.setSizePolicy(sizePolicy)
        self.text_config.setEditable(False)
        self.text_config.setObjectName("text_config")
        self.horizontalLayout_5.addWidget(self.text_config)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.text_url = QtWidgets.QLineEdit(self.tab_2)
        self.text_url.setObjectName("text_url")
        self.horizontalLayout_7.addWidget(self.text_url)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.text_model = QtWidgets.QLineEdit(self.tab_2)
        self.text_model.setObjectName("text_model")
        self.horizontalLayout_6.addWidget(self.text_model)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        self.text_key = QtWidgets.QLineEdit(self.tab_2)
        self.text_key.setObjectName("text_key")
        self.horizontalLayout_8.addWidget(self.text_key)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.bu_save_config = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bu_save_config.sizePolicy().hasHeightForWidth())
        self.bu_save_config.setSizePolicy(sizePolicy)
        self.bu_save_config.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bu_save_config.setObjectName("bu_save_config")
        self.horizontalLayout_10.addWidget(self.bu_save_config)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.text_config_file = QtWidgets.QPlainTextEdit(self.tab_2)
        self.text_config_file.setObjectName("text_config_file")
        self.verticalLayout_4.addWidget(self.text_config_file)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.bu_send.clicked.connect(MainWindow.send) # type: ignore
        self.bu_top.clicked.connect(MainWindow.change_top) # type: ignore
        self.text_config.currentIndexChanged['int'].connect(MainWindow.change_config) # type: ignore
        self.bu_summary.clicked.connect(MainWindow.change_summary) # type: ignore
        self.bu_save_config.clicked.connect(MainWindow.save_config) # type: ignore
        self.bu_fold.clicked.connect(MainWindow.change_fold) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ltranslator"))
        self.bu_switch.setToolTip(_translate("MainWindow", "开/关"))
        self.bu_top.setToolTip(_translate("MainWindow", "置顶"))
        self.bu_scroll.setToolTip(_translate("MainWindow", "滚动"))
        self.bu_summary.setToolTip(_translate("MainWindow", "摘要"))
        self.bu_send.setToolTip(_translate("MainWindow", "发送"))
        self.label_title.setText(_translate("MainWindow", "标题"))
        self.label_subject.setText(_translate("MainWindow", "学科"))
        self.bu_fold.setToolTip(_translate("MainWindow", "展开/折叠"))
        self.bu_fold.setText(_translate("MainWindow", "︿"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "原文"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "译文"))
        self.label_4.setText(_translate("MainWindow", "当前模型服务："))
        self.label_6.setText(_translate("MainWindow", "api地址："))
        self.label_5.setText(_translate("MainWindow", "模型名称："))
        self.label_7.setText(_translate("MainWindow", "api key："))
        self.label_9.setText(_translate("MainWindow", "配置文件："))
        self.bu_save_config.setText(_translate("MainWindow", "保存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "设置"))
