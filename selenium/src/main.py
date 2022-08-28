from operator import truediv
import sys
import io
import time
import os
import collector
import register
import component.log as log
import component.utility as utility

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox

logger = log.getLogger("common")
#if(workType == 1 or workType == 2):
#    if(workType == 1):
#        print('[수집]을 시작해볼게용~♥')
#        collector.init()
#    else:
#        print('[등록]을 시작해볼게용~♥')
#        register.init()
#else:
#    print('숫자 1, 2 둘 중 하나만 넣어야지~')
#    print('프로그램을 다시 시작해줘요~')
#    time.sleep(2)
#    sys.exit(1)
########################################################################

#logger = log.getLogger("common")

class MultiButtonDemo(QWidget):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super(MultiButtonDemo, self).__init__()
        
        layout = QVBoxLayout()
        self.label = QLabel("아래의 수집 또는 등록 버튼을 클릭해주세요.")
        layout.addWidget(self.label)
        labels = ["수집", "등록", "종료"]
        for label in labels:
            btn = QPushButton(label)
            btn.clicked.connect(self.clicked)
            layout.addWidget(btn)
        
        self.setLayout(layout)
        
        self.setWindowTitle("[AvaCorn] Beta 1.0.0")
        
    def getAlert(self, title, text):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(title)
        dlg.setText(text)
        button = dlg.exec_()
        return button
    
    #----------------------------------------------------------------------
    def clicked(self):
        """
        Change label based on what button was pressed
        """
        button = self.sender()
        if isinstance(button, QPushButton):
            #self.label.setText("You pressed %s!" % button.text())
            buttonType = button.text()
            if(buttonType == '수집'):
                self.label.setText('수집 중................')
                self.getAlert('알림', '수집을 선택했습니다.')
                try:
                    status, message = collector.init()
                    logger.info('status ::::  '  + status)
                    logger.info('message ::::  '  + message)
                    if(status == 'fail'):
                        self.getAlert('오류', message)
                        self.label.setText('아래의 수집 또는 등록 버튼을 클릭해주세요.')
                except:
                    self.getAlert('오류', message)
                    self.label.setText('아래의 수집 또는 등록 버튼을 클릭해주세요.')
                    #sys.exit(1)
            elif(buttonType == '등록'):
                #self.label.setText('[등록] 버튼을 클릭했습니다.')
                self.label.setText('등록 중................')
                self.getAlert('알림', '등록을 선택했습니다.')
                try:
                    status, message = register.init()
                    if(status == 'fail'):
                        self.getAlert('오류', message)
                        self.label.setText('아래의 수집 또는 등록 버튼을 클릭해주세요.')
                except:
                    self.getAlert('오류', message)
                    self.label.setText('아래의 수집 또는 등록 버튼을 클릭해주세요.')           
            else:
                sys.exit(1)
#----------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication([])
    form = MultiButtonDemo()
    form.show()
    app.exec_()

