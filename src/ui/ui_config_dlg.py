# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_config_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConfigDlg(object):
    def setupUi(self, ConfigDlg):
        ConfigDlg.setObjectName("ConfigDlg")
        ConfigDlg.setWindowModality(QtCore.Qt.NonModal)
        ConfigDlg.resize(667, 440)
        ConfigDlg.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConfigDlg)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(ConfigDlg)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tabDashd = QtWidgets.QWidget()
        self.tabDashd.setObjectName("tabDashd")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabDashd)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tabDashd)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cboDashNetwork = QtWidgets.QComboBox(self.tabDashd)
        self.cboDashNetwork.setObjectName("cboDashNetwork")
        self.cboDashNetwork.addItem("")
        self.cboDashNetwork.addItem("")
        self.horizontalLayout_3.addWidget(self.cboDashNetwork)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.frame_2 = QtWidgets.QFrame(self.tabDashd)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutConnList = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.layoutConnList.setContentsMargins(0, 0, 0, 0)
        self.layoutConnList.setSpacing(2)
        self.layoutConnList.setObjectName("layoutConnList")
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnNewConn = QtWidgets.QToolButton(self.frame)
        self.btnNewConn.setMinimumSize(QtCore.QSize(26, 26))
        self.btnNewConn.setText("")
        self.btnNewConn.setObjectName("btnNewConn")
        self.horizontalLayout.addWidget(self.btnNewConn)
        self.btnDeleteConn = QtWidgets.QToolButton(self.frame)
        self.btnDeleteConn.setMinimumSize(QtCore.QSize(26, 26))
        self.btnDeleteConn.setText("")
        self.btnDeleteConn.setObjectName("btnDeleteConn")
        self.horizontalLayout.addWidget(self.btnDeleteConn)
        self.btnMoveUpConn = QtWidgets.QToolButton(self.frame)
        self.btnMoveUpConn.setMinimumSize(QtCore.QSize(26, 26))
        self.btnMoveUpConn.setText("")
        self.btnMoveUpConn.setObjectName("btnMoveUpConn")
        self.horizontalLayout.addWidget(self.btnMoveUpConn)
        self.btnMoveDownConn = QtWidgets.QToolButton(self.frame)
        self.btnMoveDownConn.setMinimumSize(QtCore.QSize(26, 26))
        self.btnMoveDownConn.setText("")
        self.btnMoveDownConn.setObjectName("btnMoveDownConn")
        self.horizontalLayout.addWidget(self.btnMoveDownConn)
        self.btnRestoreDefault = QtWidgets.QToolButton(self.frame)
        self.btnRestoreDefault.setMinimumSize(QtCore.QSize(26, 26))
        self.btnRestoreDefault.setText("")
        self.btnRestoreDefault.setObjectName("btnRestoreDefault")
        self.horizontalLayout.addWidget(self.btnRestoreDefault)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.layoutConnList.addWidget(self.frame)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.layoutConnList.addWidget(self.label)
        self.lstConns = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstConns.sizePolicy().hasHeightForWidth())
        self.lstConns.setSizePolicy(sizePolicy)
        self.lstConns.setBaseSize(QtCore.QSize(150, 0))
        self.lstConns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lstConns.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lstConns.setObjectName("lstConns")
        self.layoutConnList.addWidget(self.lstConns)
        self.detailsFrame = QtWidgets.QFrame(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailsFrame.sizePolicy().hasHeightForWidth())
        self.detailsFrame.setSizePolicy(sizePolicy)
        self.detailsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detailsFrame.setMidLineWidth(0)
        self.detailsFrame.setObjectName("detailsFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.detailsFrame)
        self.verticalLayout_4.setContentsMargins(-1, 12, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_6.addWidget(self.splitter)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.chbRandomConn = QtWidgets.QCheckBox(self.frame_2)
        self.chbRandomConn.setObjectName("chbRandomConn")
        self.verticalLayout_5.addWidget(self.chbRandomConn)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tabDashd, "")
        self.tabMisc = QtWidgets.QWidget()
        self.tabMisc.setObjectName("tabMisc")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabMisc)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.layHardwareWallet = QtWidgets.QHBoxLayout()
        self.layHardwareWallet.setObjectName("layHardwareWallet")
        self.label_3 = QtWidgets.QLabel(self.tabMisc)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.layHardwareWallet.addWidget(self.label_3)
        self.chbHwTrezor = QtWidgets.QRadioButton(self.tabMisc)
        self.chbHwTrezor.setMinimumSize(QtCore.QSize(60, 0))
        self.chbHwTrezor.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.chbHwTrezor.setChecked(True)
        self.chbHwTrezor.setObjectName("chbHwTrezor")
        self.layHardwareWallet.addWidget(self.chbHwTrezor)
        self.chbHwLedgerNanoS = QtWidgets.QRadioButton(self.tabMisc)
        self.chbHwLedgerNanoS.setObjectName("chbHwLedgerNanoS")
        self.layHardwareWallet.addWidget(self.chbHwLedgerNanoS)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layHardwareWallet.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.layHardwareWallet)
        self.wdgKeepkeyPassEncoding = QtWidgets.QWidget(self.tabMisc)
        self.wdgKeepkeyPassEncoding.setObjectName("wdgKeepkeyPassEncoding")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.wdgKeepkeyPassEncoding)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblKeepkeyPassEncoding = QtWidgets.QLabel(self.wdgKeepkeyPassEncoding)
        self.lblKeepkeyPassEncoding.setOpenExternalLinks(True)
        self.lblKeepkeyPassEncoding.setObjectName("lblKeepkeyPassEncoding")
        self.horizontalLayout_2.addWidget(self.lblKeepkeyPassEncoding)
        self.cboKeepkeyPassEncoding = QtWidgets.QComboBox(self.wdgKeepkeyPassEncoding)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboKeepkeyPassEncoding.sizePolicy().hasHeightForWidth())
        self.cboKeepkeyPassEncoding.setSizePolicy(sizePolicy)
        self.cboKeepkeyPassEncoding.setObjectName("cboKeepkeyPassEncoding")
        self.cboKeepkeyPassEncoding.addItem("")
        self.cboKeepkeyPassEncoding.addItem("")
        self.horizontalLayout_2.addWidget(self.cboKeepkeyPassEncoding)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.wdgKeepkeyPassEncoding)
        self.chbEncryptConfigFile = QtWidgets.QCheckBox(self.tabMisc)
        self.chbEncryptConfigFile.setObjectName("chbEncryptConfigFile")
        self.verticalLayout_2.addWidget(self.chbEncryptConfigFile)
        self.chbCheckForUpdates = QtWidgets.QCheckBox(self.tabMisc)
        self.chbCheckForUpdates.setObjectName("chbCheckForUpdates")
        self.verticalLayout_2.addWidget(self.chbCheckForUpdates)
        self.chbBackupConfigFile = QtWidgets.QCheckBox(self.tabMisc)
        self.chbBackupConfigFile.setObjectName("chbBackupConfigFile")
        self.verticalLayout_2.addWidget(self.chbBackupConfigFile)
        self.chbDontUseFileDialogs = QtWidgets.QCheckBox(self.tabMisc)
        self.chbDontUseFileDialogs.setToolTip("")
        self.chbDontUseFileDialogs.setObjectName("chbDontUseFileDialogs")
        self.verticalLayout_2.addWidget(self.chbDontUseFileDialogs)
        self.hlLogLevel = QtWidgets.QHBoxLayout()
        self.hlLogLevel.setObjectName("hlLogLevel")
        self.lblLogLevel = QtWidgets.QLabel(self.tabMisc)
        self.lblLogLevel.setObjectName("lblLogLevel")
        self.hlLogLevel.addWidget(self.lblLogLevel)
        self.cboLogLevel = QtWidgets.QComboBox(self.tabMisc)
        self.cboLogLevel.setObjectName("cboLogLevel")
        self.cboLogLevel.addItem("")
        self.cboLogLevel.addItem("")
        self.cboLogLevel.addItem("")
        self.cboLogLevel.addItem("")
        self.cboLogLevel.addItem("")
        self.hlLogLevel.addWidget(self.cboLogLevel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hlLogLevel.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.hlLogLevel)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.tabWidget.addTab(self.tabMisc, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConfigDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ConfigDlg)
        self.tabWidget.setCurrentIndex(1)
        self.buttonBox.accepted.connect(ConfigDlg.accept)
        self.buttonBox.rejected.connect(ConfigDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(ConfigDlg)

    def retranslateUi(self, ConfigDlg):
        _translate = QtCore.QCoreApplication.translate
        ConfigDlg.setWindowTitle(_translate("ConfigDlg", "Dialog"))
        self.label_2.setText(_translate("ConfigDlg", "Zcoin network:"))
        self.cboDashNetwork.setItemText(0, _translate("ConfigDlg", "MAINNET"))
        self.cboDashNetwork.setItemText(1, _translate("ConfigDlg", "TESTNET"))
        self.btnNewConn.setToolTip(_translate("ConfigDlg", "Add New Connection"))
        self.btnDeleteConn.setToolTip(_translate("ConfigDlg", "Delete Current Connection"))
        self.btnMoveUpConn.setToolTip(_translate("ConfigDlg", "Move Up Current Connection"))
        self.btnMoveDownConn.setToolTip(_translate("ConfigDlg", "Move Down Current Connection"))
        self.btnRestoreDefault.setToolTip(_translate("ConfigDlg", "Restore Default Connections"))
        self.label.setText(_translate("ConfigDlg", "Connections:"))
        self.chbRandomConn.setToolTip(_translate("ConfigDlg", "Pick random connection to distribute clients\' load over multiple nodes."))
        self.chbRandomConn.setText(_translate("ConfigDlg", "Pick random connection"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDashd), _translate("ConfigDlg", "Zcoin network"))
        self.label_3.setText(_translate("ConfigDlg", "Hardware wallet:"))
        self.chbHwTrezor.setText(_translate("ConfigDlg", "Trezor"))
        self.chbHwLedgerNanoS.setText(_translate("ConfigDlg", "Ledger Nano S"))
        self.lblKeepkeyPassEncoding.setText(_translate("ConfigDlg", "KeepKey passphrase encoding:"))
        self.cboKeepkeyPassEncoding.setItemText(0, _translate("ConfigDlg", "NFC: compatible with the official KeepKey app"))
        self.cboKeepkeyPassEncoding.setItemText(1, _translate("ConfigDlg", "NFKD: compatible with BIP-39 standard and Trezor"))
        self.chbEncryptConfigFile.setToolTip(_translate("ConfigDlg", "<html><head/><body><p>Encrypts configuration file with hardware wallet. </p><p>You will need your hardware wallet connected to open the file.</p></body></html>"))
        self.chbEncryptConfigFile.setText(_translate("ConfigDlg", "Encrypt configuration file"))
        self.chbCheckForUpdates.setText(_translate("ConfigDlg", "Check for updates"))
        self.chbBackupConfigFile.setToolTip(_translate("ConfigDlg", "If checked, old config file will be saved when changing configuration"))
        self.chbBackupConfigFile.setText(_translate("ConfigDlg", "Backup config file"))
        self.chbDontUseFileDialogs.setText(_translate("ConfigDlg", "Don\'t use file dialogs"))
        self.lblLogLevel.setText(_translate("ConfigDlg", "Log level:"))
        self.cboLogLevel.setItemText(0, _translate("ConfigDlg", "Critical"))
        self.cboLogLevel.setItemText(1, _translate("ConfigDlg", "Error"))
        self.cboLogLevel.setItemText(2, _translate("ConfigDlg", "Warning"))
        self.cboLogLevel.setItemText(3, _translate("ConfigDlg", "Info"))
        self.cboLogLevel.setItemText(4, _translate("ConfigDlg", "Debug"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMisc), _translate("ConfigDlg", "Miscellaneous"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConfigDlg = QtWidgets.QDialog()
    ui = Ui_ConfigDlg()
    ui.setupUi(ConfigDlg)
    ConfigDlg.show()
    sys.exit(app.exec_())

