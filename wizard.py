# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wizard_design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot, QSize
import os, sys

# Translate asset paths to useable format for PyInstaller
def resource_path(relative_path):
  if hasattr(sys, '_MEIPASS'):
      return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath('.'), relative_path)

class ProgressBarPage(QtWidgets.QWizardPage):
    def __init__(self):
        super().__init__()
    
    def isComplete(self):
        return self.field("progressBar") == 100

class Ui_Wizard(QObject):
    def setupUi(self, Wizard):
        Wizard.setObjectName("Wizard")
        Wizard.setWindowModality(QtCore.Qt.NonModal)
        Wizard.setEnabled(True)
        Wizard.resize(655, 513)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("./assets/MI_icon.ico")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        Wizard.setWindowIcon(icon)
        Wizard.setLayoutDirection(QtCore.Qt.LeftToRight)
        Wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        Wizard.setOptions(QtWidgets.QWizard.NoCancelButtonOnLastPage|QtWidgets.QWizard.NoDefaultButton)
        
        # Page 0
        self.wizardPage0 = QtWidgets.QWizardPage()
        self.wizardPage0.setObjectName("wizardPage0")
        
        self.gridLayout_4 = QtWidgets.QGridLayout(self.wizardPage0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.LogoLayout_0 = QtWidgets.QHBoxLayout()
        self.LogoLayout_0.setObjectName("LogoLayout_0")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LogoLayout_0.addItem(spacerItem1)
        self.MedicInsightLogo_0 = QtWidgets.QLabel(self.wizardPage0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MedicInsightLogo_0.sizePolicy().hasHeightForWidth())
        self.MedicInsightLogo_0.setSizePolicy(sizePolicy)
        self.MedicInsightLogo_0.setMaximumSize(QtCore.QSize(200, 74))
        self.MedicInsightLogo_0.setText("")
        self.MedicInsightLogo_0.setPixmap(QtGui.QPixmap(resource_path("./assets/MI_logo.jpg")))
        self.MedicInsightLogo_0.setScaledContents(True)
        self.MedicInsightLogo_0.setWordWrap(False)
        self.MedicInsightLogo_0.setObjectName("MedicInsightLogo_0")
        self.LogoLayout_0.addWidget(self.MedicInsightLogo_0)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LogoLayout_0.addItem(spacerItem2)
        self.verticalLayout_9.addLayout(self.LogoLayout_0)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_9.addItem(spacerItem3)
        self.textBrowser_Welcome = QtWidgets.QTextBrowser(self.wizardPage0)
        self.textBrowser_Welcome.setObjectName("textBrowser_Welcome")
        self.verticalLayout_9.addWidget(self.textBrowser_Welcome)
        self.horizontalLayout_10.addLayout(self.verticalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.gridLayout_4.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        Wizard.addPage(self.wizardPage0)
        
        # Page 1
        self.wizardPage1 = QtWidgets.QWizardPage()
        self.wizardPage1.setObjectName("wizardPage1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.wizardPage1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.wizardPage1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.LogoLayout_1 = QtWidgets.QHBoxLayout()
        self.LogoLayout_1.setObjectName("LogoLayout_1")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LogoLayout_1.addItem(spacerItem5)
        self.MedicInsightLogo_1 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MedicInsightLogo_1.sizePolicy().hasHeightForWidth())
        self.MedicInsightLogo_1.setSizePolicy(sizePolicy)
        self.MedicInsightLogo_1.setMaximumSize(QtCore.QSize(200, 74))
        self.MedicInsightLogo_1.setText("")
        self.MedicInsightLogo_1.setPixmap(QtGui.QPixmap(resource_path("./assets/MI_logo.jpg")))
        self.MedicInsightLogo_1.setScaledContents(True)
        self.MedicInsightLogo_1.setWordWrap(False)
        self.MedicInsightLogo_1.setObjectName("MedicInsightLogo_1")
        self.LogoLayout_1.addWidget(self.MedicInsightLogo_1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LogoLayout_1.addItem(spacerItem6)
        self.verticalLayout_10.addLayout(self.LogoLayout_1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_ApiKeyMessage = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ApiKeyMessage.setFont(font)
        self.label_ApiKeyMessage.setObjectName("label_ApiKeyMessage")
        self.verticalLayout_3.addWidget(self.label_ApiKeyMessage)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_ApiKey = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ApiKey.setFont(font)
        self.label_ApiKey.setObjectName("label_ApiKey")
        self.horizontalLayout_11.addWidget(self.label_ApiKey)
        self.lineEdit_ApiKey = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_ApiKey.setText("")
        self.lineEdit_ApiKey.setObjectName("lineEdit_ApiKey")
        self.horizontalLayout_11.addWidget(self.lineEdit_ApiKey)
        self.pushButton_ApikeyTest = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_ApikeyTest.setObjectName("pushButton_ApikeyTest")
        self.horizontalLayout_11.addWidget(self.pushButton_ApikeyTest)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.verticalLayout_10.addLayout(self.verticalLayout_3)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_InputMessage = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_InputMessage.setFont(font)
        self.label_InputMessage.setObjectName("label_InputMessage")
        self.verticalLayout.addWidget(self.label_InputMessage)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_InputFilePath = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_InputFilePath.setFont(font)
        self.label_InputFilePath.setObjectName("label_InputFilePath")
        self.horizontalLayout.addWidget(self.label_InputFilePath)
        self.lineEdit_InputFilePath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_InputFilePath.setObjectName("lineEdit_InputFilePath")
        self.horizontalLayout.addWidget(self.lineEdit_InputFilePath)
        self.pushButton_InputBrowse = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_InputBrowse.setObjectName("pushButton_InputBrowse")
        self.horizontalLayout.addWidget(self.pushButton_InputBrowse)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem8)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_OutputMessage = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_OutputMessage.setFont(font)
        self.label_OutputMessage.setObjectName("label_OutputMessage")
        self.verticalLayout_2.addWidget(self.label_OutputMessage)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_OutputFilePath = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_OutputFilePath.setFont(font)
        self.label_OutputFilePath.setObjectName("label_OutputFilePath")
        self.horizontalLayout_2.addWidget(self.label_OutputFilePath)
        self.lineEdit_OutputFilePath = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_OutputFilePath.setObjectName("lineEdit_OutputFilePath")
        self.horizontalLayout_2.addWidget(self.lineEdit_OutputFilePath)
        self.pushButton_OutputBrowse = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_OutputBrowse.setObjectName("pushButton_OutputBrowse")
        self.horizontalLayout_2.addWidget(self.pushButton_OutputBrowse)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_10.addLayout(self.verticalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem9)
        self.debugTextBrowser = QtWidgets.QTextBrowser(self.splitter)
        self.debugTextBrowser.setObjectName("debugTextBrowser")
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        Wizard.addPage(self.wizardPage1)
        
        # Page 2
        self.wizardPage2 = ProgressBarPage()
        self.wizardPage2.setObjectName("wizardPage2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wizardPage2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.LogoLayout_2 = QtWidgets.QHBoxLayout()
        self.LogoLayout_2.setObjectName("LogoLayout_2")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LogoLayout_2.addItem(spacerItem10)
        self.MedicInsightLogo_2 = QtWidgets.QLabel(self.wizardPage2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MedicInsightLogo_2.sizePolicy().hasHeightForWidth())
        self.MedicInsightLogo_2.setSizePolicy(sizePolicy)
        self.MedicInsightLogo_2.setMaximumSize(QtCore.QSize(200, 74))
        self.MedicInsightLogo_2.setText("")
        self.MedicInsightLogo_2.setPixmap(QtGui.QPixmap(resource_path("./assets/MI_logo.jpg")))
        self.MedicInsightLogo_2.setScaledContents(True)
        self.MedicInsightLogo_2.setWordWrap(False)
        self.MedicInsightLogo_2.setObjectName("MedicInsightLogo_2")
        self.LogoLayout_2.addWidget(self.MedicInsightLogo_2)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LogoLayout_2.addItem(spacerItem11)
        self.verticalLayout_8.addLayout(self.LogoLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem13)
        self.startButtonLayout = QtWidgets.QHBoxLayout()
        self.startButtonLayout.setObjectName("startButtonLayout")
        self.startButton = QtWidgets.QPushButton(self.wizardPage2)
        self.startButton.setMinimumSize(QtCore.QSize(90, 0))
        self.startButton.setObjectName("startButton")
        self.startButtonLayout.addWidget(self.startButton)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.startButtonLayout.addItem(spacerItem14)
        self.verticalLayout_4.addLayout(self.startButtonLayout)
        self.progressBar = QtWidgets.QProgressBar(self.wizardPage2)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem15)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        spacerItem16 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        Wizard.addPage(self.wizardPage2)
        
        # Page 3
        self.wizardPage3 = QtWidgets.QWizardPage()
        self.wizardPage3.setObjectName("wizardPage3")
        self.gridLayout = QtWidgets.QGridLayout(self.wizardPage3)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.LogoLayout_3 = QtWidgets.QHBoxLayout()
        self.LogoLayout_3.setObjectName("LogoLayout_3")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LogoLayout_3.addItem(spacerItem17)
        self.MedicInsightLogo_3 = QtWidgets.QLabel(self.wizardPage3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MedicInsightLogo_3.sizePolicy().hasHeightForWidth())
        self.MedicInsightLogo_3.setSizePolicy(sizePolicy)
        self.MedicInsightLogo_3.setMaximumSize(QtCore.QSize(200, 74))
        self.MedicInsightLogo_3.setText("")
        self.MedicInsightLogo_3.setPixmap(QtGui.QPixmap(resource_path("./assets/MI_logo.jpg")))
        self.MedicInsightLogo_3.setScaledContents(True)
        self.MedicInsightLogo_3.setWordWrap(False)
        self.MedicInsightLogo_3.setObjectName("MedicInsightLogo_3")
        self.LogoLayout_3.addWidget(self.MedicInsightLogo_3)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LogoLayout_3.addItem(spacerItem18)
        self.verticalLayout_7.addLayout(self.LogoLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem19)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem20)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.wizardPage3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.lineEdit_ReadOnlyOutPath = QtWidgets.QLineEdit(self.wizardPage3)
        self.lineEdit_ReadOnlyOutPath.setReadOnly(True)
        self.lineEdit_ReadOnlyOutPath.setObjectName("lineEdit_ReadOnlyOutPath")
        self.verticalLayout_5.addWidget(self.lineEdit_ReadOnlyOutPath)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem21)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem22)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        Wizard.addPage(self.wizardPage3)

        self.retranslateUi(Wizard)
        self.pushButton_ApikeyTest.clicked.connect(self.testKeyPressedSlot)
        self.lineEdit_InputFilePath.returnPressed.connect(self.inputReturnPressedSlot)
        self.pushButton_InputBrowse.clicked.connect(self.inputBrowseSlot)
        self.pushButton_OutputBrowse.clicked.connect(self.outputBrowseSlot)
        self.lineEdit_OutputFilePath.returnPressed.connect(self.outputReturnPressedSlot)
        self.startButton.clicked.connect(self.startSlot)
        self.progressBar.valueChanged.connect(self.wizardPage2.completeChanged)
        
        QtCore.QMetaObject.connectSlotsByName(Wizard)

    def retranslateUi(self, Wizard):
        _translate = QtCore.QCoreApplication.translate
        Wizard.setWindowTitle(_translate("Wizard", "Medic Insight Placement Allocation Program - v0.2"))
        self.label_ApiKeyMessage.setText(_translate("Wizard", "Enter a Google Cloud Geocoding API key:"))
        self.label_ApiKey.setText(_translate("Wizard", "API key:"))
        self.pushButton_ApikeyTest.setText(_translate("Wizard", "Test key"))
        self.label_InputMessage.setText(_translate("Wizard", "Select data to be sorted:"))
        self.label_InputFilePath.setText(_translate("Wizard", "File Path:"))
        self.pushButton_InputBrowse.setText(_translate("Wizard", "Browse..."))
        self.label_OutputMessage.setText(_translate("Wizard", "Save output to:"))
        self.label_OutputFilePath.setText(_translate("Wizard", "File Path:"))
        self.pushButton_OutputBrowse.setText(_translate("Wizard", "Browse..."))
        self.startButton.setText(_translate("Wizard", "Start"))
        self.label.setText(_translate("Wizard", "Finished! Sorted data saved to:"))
        
        self.textBrowser_Welcome.setHtml(_translate("Wizard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to the Medic Insight Placement Allocation Program wizard.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This software will allocate students to clinical placements prioritising in this order:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  1) Provide placement in the closest hospital to the student\'s home</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  2) Provide placements on the same day</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  3) Provide placements within the same hospital or site (e.g. QEUH and RHC)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  4) Provide placements of varying types (e.g. ward and clinic)</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">For guidance on how to use this software and for troubleshooting, please refer to the manual on the google drive called &quot;MI Placement Allocation Program Manual&quot;.</span></p></body></html>"))
        
    # Page 1 slots
    @pyqtSlot( )
    def testKeyPressedSlot( self ):
        pass
        
    @pyqtSlot( )
    def inputBrowseSlot( self ):
        pass
    
    @pyqtSlot( )
    def inputReturnPressedSlot( self ):
        pass
    
    @pyqtSlot( )
    def outputBrowseSlot( self ):
        pass
    
    @pyqtSlot( )
    def outputReturnPressedSlot( self ):
        pass
    
    # Page 2 slots
    @pyqtSlot( )
    def startSlot( self ):
        pass
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Wizard = QtWidgets.QWizard()
    ui = Ui_Wizard()
    ui.setupUi(Wizard)
    Wizard.show()
    sys.exit(app.exec_())
