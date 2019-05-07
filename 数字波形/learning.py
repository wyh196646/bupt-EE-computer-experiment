# -*- coding: utf-8 -*-

import numpy as np
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication,  QLineEdit , QWidget ,QFormLayout,QPushButton,QMessageBox,QLabel,QVBoxLayout,QSizePolicy
import sys 
import random
import matplotlib.pyplot as plt
from numpy.linalg import cholesky

Alist=[]
Blist=[]
Clist=[]
class initUI(QWidget):
	def __init__(self):
		super(initUI, self).__init__()
		self.setWindowTitle("数字波形生成器")
		self.resize(700,700)
		flo = QFormLayout()          		
		self.Asequence = QLineEdit()
		self.Bsequence = QLineEdit()
		self.Fexpression= QLineEdit()
		self.Csequence= QLineEdit()
		self.hint=QLabel("支持四种运算,与,或,非,异或,同或，输入分别为为~A,~B,A&B,A|B,A^B,~(A^B)")
		self.bupt=QLabel("Developed by Hao 2019/4/13")
		self.btn=QPushButton('运算')
		self.btn_1=QPushButton("画图")
		self.Asequence.setInputMask("BBBBBBBB")
		self.Bsequence.setInputMask("BBBBBBBB")
		flo.addRow("A序列",self.Asequence)
		flo.addRow("B序列", self.Bsequence)
		flo.addRow("F表达式",self.Fexpression)
		flo.addWidget(self.hint)
		flo.addRow("运算结果",self.Csequence)
		flo.addWidget(self.btn) 
		flo.addWidget(self.btn_1)  
		flo.addWidget(self.bupt)	                    
		self.setLayout(flo)	
		self.btn.clicked.connect(self.on_click)
		self.btn_1.clicked.connect(self.paintA)
		
	def  on_click(self):
		Avalue=self.Asequence.text()
		Bvalue=self.Bsequence.text()
		for(i,j) in zip(Avalue,Bvalue):
			Alist.append(int(i))
			Blist.append(int(j))
		if self.Fexpression.text() =='~A':
			for i in A:
				c=~(int(i))
				Clist.append(c)
		elif self.Fexpression.text()=='~B':
			for i in B:
				c=~(int(i))
				Clist.append(c)
		elif self.Fexpression.text()=='A&B':
			for (i,j) in zip(Avalue,Bvalue):
				c=int(i)&int(j)#北邮电子院的数学物理方法这门课能不能别开了
				Clist.append(c)
		elif self.Fexpression.text()=='A|B':
			for (i,j) in zip(Avalue,Bvalue):
				c=int(i)|int(j)#学也学不明白，学你*呢，老师你自己会吗
				Clist.append(c)
		elif self.Fexpression.text()=='A^B':
			for (i,j) in zip(Avalue,Bvalue):
				c=int(i)^int(j)
				Clist.append(c)
		elif self.Fexpression.text()=='~(A^B)':
			for (i,j) in zip(Avalue,Bvalue):
				c=~(int(i)^int(j))
				Clist.append(c)
		num_list_new = [str(x) for x in Clist]
		re=",".join(num_list_new)
		self.Csequence.setText(re)

	def paintA(self):
		yA=[]
		yB=[]
		yC=[]
		plt.figure()
		x=np.arange(1,len(Alist),0.1)
		for i in x:
			if(Alist[int(i)]==1):
				yA.append(1)
			else :
				yA.append(0)
		for j in x:
			if(Blist[int(j)]==1):
				yB.append(1)
			else :
				yB.append(0)
		for k in x:
			if(Clist[int(k)]==1):
				yC.append(1)
			else :
				yC.append(0)
		ax1=plt.subplot(221)
		ax1.set_title("A")
		plt.plot(x,yA)
		ax2 = plt.subplot(222)
		ax2.set_title("B")
		plt.plot(x,yB)
		ax3 = plt.subplot(212)
		ax3.set_title("C")
		plt.plot(x,yC)
		plt.show()

if __name__ == "__main__":       
	app = QApplication(sys.argv)
	first= initUI()
	first.show()
	sys.exit(app.exec_())
