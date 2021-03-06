# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Proxy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_infoview(object):
    def setupUi(self, infoview):
        infoview.setObjectName("infoview")
        infoview.resize(740, 535)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        infoview.setFont(font)
        infoview.setTabPosition(QtWidgets.QTabWidget.North)
        infoview.setTabShape(QtWidgets.QTabWidget.Rounded)
        infoview.setIconSize(QtCore.QSize(40, 30))
        self.information = QtWidgets.QWidget()
        self.information.setEnabled(True)
        self.information.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.information.setObjectName("information")
        self.widget_left_info = QtWidgets.QWidget(self.information)
        self.widget_left_info.setGeometry(QtCore.QRect(20, 0, 331, 431))
        self.widget_left_info.setStyleSheet("background-color: rgb(240, 255, 255);")
        self.widget_left_info.setObjectName("widget_left_info")
        self.label_uuid = QtWidgets.QLabel(self.widget_left_info)
        self.label_uuid.setGeometry(QtCore.QRect(10, 80, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_uuid.setFont(font)
        self.label_uuid.setObjectName("label_uuid")
        self.text_UUID = QtWidgets.QTextBrowser(self.widget_left_info)
        self.text_UUID.setGeometry(QtCore.QRect(10, 100, 300, 50))
        self.text_UUID.setObjectName("text_UUID")
        self.label_pubkey = QtWidgets.QLabel(self.widget_left_info)
        self.label_pubkey.setGeometry(QtCore.QRect(10, 160, 30, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_pubkey.setFont(font)
        self.label_pubkey.setObjectName("label_pubkey")
        self.text_infopublickey = QtWidgets.QTextBrowser(self.widget_left_info)
        self.text_infopublickey.setGeometry(QtCore.QRect(10, 190, 300, 50))
        self.text_infopublickey.setObjectName("text_infopublickey")
        self.btn_reset = QtWidgets.QPushButton(self.widget_left_info)
        self.btn_reset.setGeometry(QtCore.QRect(110, 270, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_reset.setObjectName("btn_reset")
        self.widget_right_info = QtWidgets.QWidget(self.information)
        self.widget_right_info.setGeometry(QtCore.QRect(350, 0, 351, 431))
        self.widget_right_info.setStyleSheet("background-color: rgb(240, 255, 255);")
        self.widget_right_info.setObjectName("widget_right_info")
        self.label_version = QtWidgets.QLabel(self.widget_right_info)
        self.label_version.setGeometry(QtCore.QRect(10, 80, 72, 15))
        self.label_version.setObjectName("label_version")
        self.text_version = QtWidgets.QTextBrowser(self.widget_right_info)
        self.text_version.setGeometry(QtCore.QRect(10, 100, 261, 31))
        self.text_version.setObjectName("text_version")
        self.label_author = QtWidgets.QLabel(self.widget_right_info)
        self.label_author.setGeometry(QtCore.QRect(10, 140, 72, 15))
        self.label_author.setObjectName("label_author")
        self.label_directory = QtWidgets.QLabel(self.widget_right_info)
        self.label_directory.setGeometry(QtCore.QRect(10, 200, 72, 15))
        self.label_directory.setObjectName("label_directory")
        self.text_author = QtWidgets.QTextBrowser(self.widget_right_info)
        self.text_author.setGeometry(QtCore.QRect(10, 160, 261, 31))
        self.text_author.setObjectName("text_author")
        self.text_workdirectory = QtWidgets.QTextBrowser(self.widget_right_info)
        self.text_workdirectory.setGeometry(QtCore.QRect(10, 220, 261, 51))
        self.text_workdirectory.setObjectName("text_workdirectory")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Resources/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        infoview.addTab(self.information, icon, "")
        self.signature = QtWidgets.QWidget()
        self.signature.setObjectName("signature")
        self.widget_center_2 = QtWidgets.QWidget(self.signature)
        self.widget_center_2.setGeometry(QtCore.QRect(20, 0, 341, 461))
        self.widget_center_2.setStyleSheet("background-color: rgb(240, 255, 255);")
        self.widget_center_2.setObjectName("widget_center_2")
        self.label_signer = QtWidgets.QLabel(self.widget_center_2)
        self.label_signer.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.label_signer.setObjectName("label_signer")
        self.label_choosefile = QtWidgets.QLabel(self.widget_center_2)
        self.label_choosefile.setGeometry(QtCore.QRect(10, 140, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_choosefile.setFont(font)
        self.label_choosefile.setObjectName("label_choosefile")
        self.text_choosefile = QtWidgets.QTextBrowser(self.widget_center_2)
        self.text_choosefile.setGeometry(QtCore.QRect(9, 169, 301, 41))
        self.text_choosefile.setObjectName("text_choosefile")
        self.lable_createsign = QtWidgets.QLabel(self.widget_center_2)
        self.lable_createsign.setGeometry(QtCore.QRect(10, 220, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lable_createsign.setFont(font)
        self.lable_createsign.setObjectName("lable_createsign")
        self.text_createfile = QtWidgets.QTextBrowser(self.widget_center_2)
        self.text_createfile.setGeometry(QtCore.QRect(9, 249, 301, 41))
        self.text_createfile.setObjectName("text_createfile")
        self.combo_signer = QtWidgets.QComboBox(self.widget_center_2)
        self.combo_signer.setGeometry(QtCore.QRect(10, 110, 301, 21))
        self.combo_signer.setObjectName("combo_signer")
        self.excu_btn = QtWidgets.QPushButton(self.widget_center_2)
        self.excu_btn.setGeometry(QtCore.QRect(90, 310, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.excu_btn.setFont(font)
        self.excu_btn.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.excu_btn.setObjectName("excu_btn")
        self.btn_choosefile = QtWidgets.QPushButton(self.widget_center_2)
        self.btn_choosefile.setGeometry(QtCore.QRect(120, 140, 21, 21))
        self.btn_choosefile.setStyleSheet("border-color: rgb(240, 255, 255);")
        self.btn_choosefile.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Resources/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_choosefile.setIcon(icon1)
        self.btn_choosefile.setIconSize(QtCore.QSize(20, 20))
        self.btn_choosefile.setObjectName("btn_choosefile")
        self.widget_right_2 = QtWidgets.QWidget(self.signature)
        self.widget_right_2.setGeometry(QtCore.QRect(361, 0, 351, 461))
        self.widget_right_2.setStyleSheet("background-color: rgb(240, 255, 255);")
        self.widget_right_2.setObjectName("widget_right_2")
        self.lable_signerUuid_2 = QtWidgets.QLabel(self.widget_right_2)
        self.lable_signerUuid_2.setGeometry(QtCore.QRect(10, 90, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lable_signerUuid_2.setFont(font)
        self.lable_signerUuid_2.setObjectName("lable_signerUuid_2")
        self.text_signerUuid_2 = QtWidgets.QTextBrowser(self.widget_right_2)
        self.text_signerUuid_2.setGeometry(QtCore.QRect(10, 110, 321, 31))
        self.text_signerUuid_2.setObjectName("text_signerUuid_2")
        self.lable_agentUuid_2 = QtWidgets.QLabel(self.widget_right_2)
        self.lable_agentUuid_2.setGeometry(QtCore.QRect(10, 150, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lable_agentUuid_2.setFont(font)
        self.lable_agentUuid_2.setObjectName("lable_agentUuid_2")
        self.label_time_2 = QtWidgets.QLabel(self.widget_right_2)
        self.label_time_2.setGeometry(QtCore.QRect(10, 210, 72, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_time_2.setFont(font)
        self.label_time_2.setObjectName("label_time_2")
        self.label_signeffective_2 = QtWidgets.QLabel(self.widget_right_2)
        self.label_signeffective_2.setGeometry(QtCore.QRect(10, 270, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_signeffective_2.setFont(font)
        self.label_signeffective_2.setObjectName("label_signeffective_2")
        self.text_agentUuid_2 = QtWidgets.QTextBrowser(self.widget_right_2)
        self.text_agentUuid_2.setGeometry(QtCore.QRect(10, 170, 321, 31))
        self.text_agentUuid_2.setObjectName("text_agentUuid_2")
        self.text_time_2 = QtWidgets.QTextBrowser(self.widget_right_2)
        self.text_time_2.setGeometry(QtCore.QRect(10, 230, 321, 31))
        self.text_time_2.setObjectName("text_time_2")
        self.text_signeffective_2 = QtWidgets.QTextBrowser(self.widget_right_2)
        self.text_signeffective_2.setGeometry(QtCore.QRect(10, 290, 321, 31))
        self.text_signeffective_2.setObjectName("text_signeffective_2")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Resources/signature.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        infoview.addTab(self.signature, icon2, "")
        self.verify = QtWidgets.QWidget()
        self.verify.setObjectName("verify")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.verify)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_center_4 = QtWidgets.QWidget(self.verify)
        self.widget_center_4.setStyleSheet("background-color: rgb(240, 255, 255);")
        self.widget_center_4.setObjectName("widget_center_4")
        self.label_verifyfile = QtWidgets.QLabel(self.widget_center_4)
        self.label_verifyfile.setGeometry(QtCore.QRect(10, 100, 91, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_verifyfile.setFont(font)
        self.label_verifyfile.setObjectName("label_verifyfile")
        self.text_verifyfile = QtWidgets.QTextBrowser(self.widget_center_4)
        self.text_verifyfile.setGeometry(QtCore.QRect(10, 120, 300, 50))
        self.text_verifyfile.setObjectName("text_verifyfile")
        self.label_signfile = QtWidgets.QLabel(self.widget_center_4)
        self.label_signfile.setGeometry(QtCore.QRect(10, 180, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_signfile.setFont(font)
        self.label_signfile.setObjectName("label_signfile")
        self.text_signfile = QtWidgets.QTextBrowser(self.widget_center_4)
        self.text_signfile.setGeometry(QtCore.QRect(10, 200, 300, 50))
        self.text_signfile.setObjectName("text_signfile")
        self.btn_verifysign = QtWidgets.QPushButton(self.widget_center_4)
        self.btn_verifysign.setGeometry(QtCore.QRect(100, 270, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_verifysign.setFont(font)
        self.btn_verifysign.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_verifysign.setObjectName("btn_verifysign")
        self.btn_verifyfile = QtWidgets.QPushButton(self.widget_center_4)
        self.btn_verifyfile.setGeometry(QtCore.QRect(90, 100, 21, 21))
        self.btn_verifyfile.setStyleSheet("border-color: rgb(240, 255, 255);")
        self.btn_verifyfile.setText("")
        self.btn_verifyfile.setIcon(icon1)
        self.btn_verifyfile.setIconSize(QtCore.QSize(20, 20))
        self.btn_verifyfile.setObjectName("btn_verifyfile")
        self.signfile_btn = QtWidgets.QPushButton(self.widget_center_4)
        self.signfile_btn.setGeometry(QtCore.QRect(80, 180, 21, 21))
        self.signfile_btn.setStyleSheet("border-color: rgb(240, 255, 255);")
        self.signfile_btn.setText("")
        self.signfile_btn.setIcon(icon1)
        self.signfile_btn.setIconSize(QtCore.QSize(20, 20))
        self.signfile_btn.setObjectName("signfile_btn")
        self.widget_right = QtWidgets.QWidget(self.widget_center_4)
        self.widget_right.setGeometry(QtCore.QRect(360, 0, 352, 470))
        self.widget_right.setStyleSheet("background-color: rgb(240, 255, 255);")
        self.widget_right.setObjectName("widget_right")
        self.lable_signerUuid = QtWidgets.QLabel(self.widget_right)
        self.lable_signerUuid.setGeometry(QtCore.QRect(10, 90, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lable_signerUuid.setFont(font)
        self.lable_signerUuid.setObjectName("lable_signerUuid")
        self.text_signerUuid = QtWidgets.QTextBrowser(self.widget_right)
        self.text_signerUuid.setGeometry(QtCore.QRect(10, 110, 321, 31))
        self.text_signerUuid.setObjectName("text_signerUuid")
        self.lable_agentUuid = QtWidgets.QLabel(self.widget_right)
        self.lable_agentUuid.setGeometry(QtCore.QRect(10, 150, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lable_agentUuid.setFont(font)
        self.lable_agentUuid.setObjectName("lable_agentUuid")
        self.label_time = QtWidgets.QLabel(self.widget_right)
        self.label_time.setGeometry(QtCore.QRect(10, 210, 72, 15))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_time.setFont(font)
        self.label_time.setObjectName("label_time")
        self.label_signeffective = QtWidgets.QLabel(self.widget_right)
        self.label_signeffective.setGeometry(QtCore.QRect(10, 270, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_signeffective.setFont(font)
        self.label_signeffective.setObjectName("label_signeffective")
        self.text_agentUuid = QtWidgets.QTextBrowser(self.widget_right)
        self.text_agentUuid.setGeometry(QtCore.QRect(10, 170, 321, 31))
        self.text_agentUuid.setObjectName("text_agentUuid")
        self.text_time = QtWidgets.QTextBrowser(self.widget_right)
        self.text_time.setGeometry(QtCore.QRect(10, 230, 321, 31))
        self.text_time.setObjectName("text_time")
        self.text_signeffective = QtWidgets.QTextBrowser(self.widget_right)
        self.text_signeffective.setGeometry(QtCore.QRect(10, 290, 321, 31))
        self.text_signeffective.setObjectName("text_signeffective")
        self.horizontalLayout.addWidget(self.widget_center_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./Resources/verify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        infoview.addTab(self.verify, icon3, "")
        self.proxy = QtWidgets.QWidget()
        self.proxy.setObjectName("proxy")
        self.widget_center_5 = QtWidgets.QWidget(self.proxy)
        self.widget_center_5.setGeometry(QtCore.QRect(20, 0, 341, 461))
        self.widget_center_5.setStyleSheet("background-color: rgb(240, 255, 255);")
        self.widget_center_5.setObjectName("widget_center_5")
        self.label_clientlist = QtWidgets.QLabel(self.widget_center_5)
        self.label_clientlist.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.label_clientlist.setObjectName("label_clientlist")
        self.combo_clientlist = QtWidgets.QComboBox(self.widget_center_5)
        self.combo_clientlist.setGeometry(QtCore.QRect(10, 110, 301, 21))
        self.combo_clientlist.setObjectName("combo_clientlist")
        self.label_authorizelist = QtWidgets.QLabel(self.widget_center_5)
        self.label_authorizelist.setGeometry(QtCore.QRect(10, 160, 71, 16))
        self.label_authorizelist.setObjectName("label_authorizelist")
        self.combo_authorizelist = QtWidgets.QComboBox(self.widget_center_5)
        self.combo_authorizelist.setGeometry(QtCore.QRect(10, 180, 301, 21))
        self.combo_authorizelist.setObjectName("combo_authorizelist")
        self.btn_newproxy = QtWidgets.QPushButton(self.widget_center_5)
        self.btn_newproxy.setGeometry(QtCore.QRect(90, 240, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_newproxy.setFont(font)
        self.btn_newproxy.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_newproxy.setObjectName("btn_newproxy")
        self.widget_right_4 = QtWidgets.QWidget(self.proxy)
        self.widget_right_4.setGeometry(QtCore.QRect(360, 0, 351, 461))
        self.widget_right_4.setStyleSheet("background-color: rgb(240, 255, 255);")
        self.widget_right_4.setObjectName("widget_right_4")
        self.btn_cancleauthorize = QtWidgets.QPushButton(self.widget_right_4)
        self.btn_cancleauthorize.setGeometry(QtCore.QRect(120, 240, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancleauthorize.setFont(font)
        self.btn_cancleauthorize.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.btn_cancleauthorize.setObjectName("btn_cancleauthorize")
        self.lable_uuid = QtWidgets.QLabel(self.widget_right_4)
        self.lable_uuid.setGeometry(QtCore.QRect(50, 70, 51, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lable_uuid.setFont(font)
        self.lable_uuid.setObjectName("lable_uuid")
        self.text_uuid = QtWidgets.QTextBrowser(self.widget_right_4)
        self.text_uuid.setGeometry(QtCore.QRect(50, 90, 261, 31))
        self.text_uuid.setObjectName("text_uuid")
        self.text_proxypublickey = QtWidgets.QTextBrowser(self.widget_right_4)
        self.text_proxypublickey.setGeometry(QtCore.QRect(50, 160, 261, 31))
        self.text_proxypublickey.setObjectName("text_proxypublickey")
        self.lable_publickey = QtWidgets.QLabel(self.widget_right_4)
        self.lable_publickey.setGeometry(QtCore.QRect(50, 130, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lable_publickey.setFont(font)
        self.lable_publickey.setObjectName("lable_publickey")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./Resources/proxy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        infoview.addTab(self.proxy, icon4, "")

        self.retranslateUi(infoview)
        infoview.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(infoview)

    def retranslateUi(self, infoview):
        _translate = QtCore.QCoreApplication.translate
        infoview.setWindowTitle(_translate("infoview", "TabWidget"))
        self.label_uuid.setText(_translate("infoview", "UUID"))
        self.label_pubkey.setText(_translate("infoview", "公钥"))
        self.btn_reset.setText(_translate("infoview", "重置密钥"))
        self.label_version.setText(_translate("infoview", "版本号："))
        self.label_author.setText(_translate("infoview", "作者："))
        self.label_directory.setText(_translate("infoview", "工作目录："))
        infoview.setTabText(infoview.indexOf(self.information), _translate("infoview", "信息"))
        self.label_signer.setText(_translate("infoview", "<html><head/><body><p><span style=\" font-weight:600;\">签名人</span></p></body></html>"))
        self.label_choosefile.setText(_translate("infoview", "选择文件"))
        self.lable_createsign.setText(_translate("infoview", "生成签名"))
        self.excu_btn.setText(_translate("infoview", "执行签名"))
        self.lable_signerUuid_2.setText(_translate("infoview", "原签名人UUID:"))
        self.lable_agentUuid_2.setText(_translate("infoview", "代理人UUID:"))
        self.label_time_2.setText(_translate("infoview", "时间戳："))
        self.label_signeffective_2.setText(_translate("infoview", "签名是否成功："))
        infoview.setTabText(infoview.indexOf(self.signature), _translate("infoview", "签名"))
        self.label_verifyfile.setText(_translate("infoview", "验证文件名"))
        self.label_signfile.setText(_translate("infoview", "签名文件"))
        self.btn_verifysign.setText(_translate("infoview", "验证签名"))
        self.lable_signerUuid.setText(_translate("infoview", "原签名人UUID:"))
        self.lable_agentUuid.setText(_translate("infoview", "代理人UUID:"))
        self.label_time.setText(_translate("infoview", "时间戳："))
        self.label_signeffective.setText(_translate("infoview", "签名是否有效："))
        infoview.setTabText(infoview.indexOf(self.verify), _translate("infoview", "验证"))
        self.label_clientlist.setText(_translate("infoview", "<html><head/><body><p>代理客户</p></body></html>"))
        self.label_authorizelist.setText(_translate("infoview", "<html><head/><body><p><span style=\" font-weight:600;\">授权列表</span></p></body></html>"))
        self.btn_newproxy.setText(_translate("infoview", "新建代理"))
        self.btn_cancleauthorize.setText(_translate("infoview", "撤销授权"))
        self.lable_uuid.setText(_translate("infoview", "UUID:"))
        self.lable_publickey.setText(_translate("infoview", "公钥："))
        infoview.setTabText(infoview.indexOf(self.proxy), _translate("infoview", "代理"))
