# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
''' Note that in this case it is an auto converted file but still we went ahead and typed QDialog inside the class and not object which was there original
Also we included the import statement from PyQt5.QtWidgets import QDialog'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QInputDialog, QLineEdit, QMessageBox


class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(727, 597)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listWidget = QtWidgets.QListWidget(self.splitter)
        self.listWidget.setObjectName("listWidget")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_pushButton = QtWidgets.QPushButton(self.widget)
        self.add_pushButton.setObjectName("add_pushButton")
        self.verticalLayout.addWidget(self.add_pushButton)
        self.edit_pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.edit_pushButton_2.setObjectName("edit_pushButton_2")
        self.verticalLayout.addWidget(self.edit_pushButton_2)
        self.remove_pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.remove_pushButton_3.setObjectName("remove_pushButton_3")
        self.verticalLayout.addWidget(self.remove_pushButton_3)
        self.up_pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.up_pushButton_4.setObjectName("up_pushButton_4")
        self.verticalLayout.addWidget(self.up_pushButton_4)
        self.down_pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.down_pushButton_5.setObjectName("down_pushButton_5")
        self.verticalLayout.addWidget(self.down_pushButton_5)
        self.sort_pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.sort_pushButton_6.setObjectName("sort_pushButton_6")
        self.verticalLayout.addWidget(self.sort_pushButton_6)
        self.close_pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.close_pushButton_7.setObjectName("close_pushButton_7")
        self.verticalLayout.addWidget(self.close_pushButton_7)
        self.verticalLayout_2.addWidget(self.splitter)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.Employee()
        self.add_pushButton.clicked.connect(self.Add)
        self.edit_pushButton_2.clicked.connect(self.Edit)
        self.remove_pushButton_3.clicked.connect(self.Remove)
        self.up_pushButton_4.clicked.connect(self.up)
        self.down_pushButton_5.clicked.connect(self.down)
        self.sort_pushButton_6.clicked.connect(self.sort)



    def Employee(self):
        self.persons = ['john','babu','roy','tom']
        self.listWidget.addItems(self.persons)
        self.listWidget.setCurrentRow(2)  # this is to indicate where to highlight in the list when the app launches

    def Add(self):
        row = self.listWidget.currentRow()
        text,ok  = QInputDialog.getText(self, 'Employee WIndow', "Enter the empployee name")
        print("text value is :", text, "Ok value is :" , ok)
        if ok and text is not None:
            self.listWidget.insertItem(row,text)

    def Edit(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item is not None:
            string, ok = QInputDialog.getText(self, "Employee Dialog", "Edit EMployeename", QLineEdit.Normal, item.text())
            if string and ok is not None:
                item.setText(string)

    def Remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)

        if item is None:
            return

        reply = QMessageBox.question(self,"Remove Employee", "Do you want to remove employee"+ str(item.text())
                                     ,QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item

    def up(self):
        row = self.listWidget.currentRow()
        if row >=1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row -1, item)
            self.listWidget.setCurrentItem(item)

    def down(self):
        row = self.listWidget.currentRow()
        if row < self.listWidget.count() -1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row +1, item)
            self.listWidget.setCurrentItem(item)

    def sort(self):
        self.listWidget.sortItems()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Employee Application"))
        Dialog.setWindowIcon((QIcon("icon1.jpg")))
        self.add_pushButton.setText(_translate("Dialog", "Add"))
        self.edit_pushButton_2.setText(_translate("Dialog", "Edit"))
        self.remove_pushButton_3.setText(_translate("Dialog", "Remove"))
        self.up_pushButton_4.setText(_translate("Dialog", "Up"))
        self.down_pushButton_5.setText(_translate("Dialog", "Down"))
        self.sort_pushButton_6.setText(_translate("Dialog", "Sort"))
        self.close_pushButton_7.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
