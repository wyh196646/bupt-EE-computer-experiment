import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt 
import pandas as pd 
import pymysql
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimHei']
a='0'
conn = pymysql.connect(host='localhost',user='root',password='wyh19990713',database='stock',charset='utf8')
cursor = conn.cursor()
stock_name=[]
class myWindow:
	def __init__(self, root, myTitle, Xlist):
		self.top = tk.Toplevel(root, width=300, height=200)
		self.top.title(myTitle)
		self.top.attributes('-topmost', 1)
		label = tk.Label(self.top, text=myTitle)
		label.place(x=0, y=20)
		labelx= tk.Label(self.top, text='组合查询的结果已经嵌入到下拉选项中')
		labelx.place(x=0, y=50)
		buptstockpull= ttk.Combobox(self.top, width=12)
		buptstockpull['values'] = Xlist# 设置下拉列表的值
		buptstockpull.current(0)  
		buptstockpull.place( x=100,y=20)      # 设置其在界面中出现的位置  column代表列   row 代表行
		query_pull=ttk.Button(self.top, text="下拉查询:",command=lambda :stock_pull(buptstockpull.get()))
		query_pull.place(x=200, y=20)

def deleteDuplicatedElementFromList2(list):
	resultList = []
	for item in list:
		if not item in resultList:
			resultList.append(item)
	return resultList

def init():
	sql_2 = "SELECT stock_name from data;" 
	cursor.execute(sql_2)
	results = cursor.fetchall()
	for x in results:
		stock_name.append(x)
init()

def clickMe():
	sql_1= "SELECT * from data where Stock_code ='%s';" 
	cursor.execute(sql_1%nameEntered.get())
	results = cursor.fetchall()
	price=[]
	date=[]
	number=0
	finace=[]#40/30358248.8
	for row in results:
		price.append(float(row[2]))
		date.append(row[3])
		i=0
		number=0
		j=1
		while(i<3):
			if i<2:
				number+=(float (row[7][i])*10**j)#数据为几十亿，取前三位，后面单位由元转换为十亿
				i=i+1
				j=j-1
			else:
				number+=(float(row[7][i])/10)
				i=i+1
				j=j-1
		finace.append(number)
	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx()
	ax1.plot(date, price, 'g-')
	ax2.plot(date, finace, 'b-')
	ax1.set_xlabel('日期')
	ax1.set_ylabel('收盘价(单位/元)  绿色曲线')
	ax2.set_ylabel('融资融券余额(单位/亿)  蓝色曲线')
	ax1.set_title('%s   收盘价/融资融券余额'%row[6])
	plt.show()

def Combination_query():
	evaluestockprice=0
	evaluestockfinace=0
	if stockprincechange.get()=='上涨10%':
		evaluestockprice=0.1
	elif(stockprincechange.get()=='上涨20%'):
		evaluestockprice=0.2
	elif(stockprincechange.get()=='上涨30%'):
		evaluestockprice=0.3
	elif(stockprincechange.get()=='下跌10%'):
		evaluestockprice=-0.1
	elif(stockprincechange.get()=='下跌20%'):#用字典可以优化
		evaluestockprice=-0.2
	elif (stockprincechange.get()=='下跌30%'):
		evaluestockprice=-0.3
	if(financing.get()=='增加10%'):
		evaluestockfinace=0.1
	elif(financing.get()=='增加20%'):
		evaluestockfinace=0.2
	elif(financing.get()=='增加30%'):
		evaluestockfinace=0.3
	elif(financing.get()=='减少10%'):
		evaluestockfinace=-0.1
	elif(financing.get()=='减少20%'):
		evaluestockfinace=-0.2
	elif(financing.get()=='减少30%'):
		evaluestockfinace=-0.3
	print(evaluestockfinace)
	print(evaluestockprice)
	sql_combition = "select * from data where Date ='%s' or Date='%s'"
	cursor.execute(sql_combition%(startdate.get(),finaldate.get()))
	results = cursor.fetchall()
	i=0
	k=0
	stock1=[]
	finacehash=[]
	if(evaluestockprice>0):
		while(i<len(results)-1):
			pricegap=(float(results[i+1][2])-float(results[i][2]))/float(results[i][2])
			finacegap=(float(results[i+1][7][0:3])-float(results[i][7][0:3]))/float(results[i][7][0:3])
			if(pricegap>evaluestockprice):
				stock1.append(results[i][6])
				finacehash.append(finacegap)	
			i=i+2
	elif(evaluestockprice>0):
		while(i<len(results)-1):
			pricegap=(float(results[i+1][2])-float(results[i][2]))/float(results[i][2])
			finacegap=(float(results[i+1][7][0:3])-float(results[i][7][0:3]))/float(results[i][7][0:3])
			if(pricegap<evaluestockprice):
				stock1.append(results[i][6])
				finacehash.append(finacegap)	
			i=i+2
	print(stock1)
	print(finacehash)		
	print(len(finacehash))
	print(len(stock1))
	m=0
	q=0
	if(evaluestockfinace>0):
		while(m<len(finacehash)-1):
			if(finacehash[m]<evaluestockfinace):
				stock1[m]='0'
			m=m+1
	elif(evaluestockfinace<0):
		while(m<len(finacehash)-1):
			if(finacehash[m]<evaluestockfinace):
				stock1[m]='0'
			m=m+1
	while '0' in stock1:
		stock1.remove('0')
	print(stock1)
	w1 = myWindow(win, '查询结果', stock1)
	
def stock_pull(a):
	sql_1= "SELECT * from data where  Stock_name='%s';" 
	cursor.execute(sql_1%a)
	results = cursor.fetchall()
	price=[]
	date=[]
	number=0
	finace=[]
	for row in results:
		price.append(float(row[2]))
		date.append(row[3])
		i=0
		number=0
		j=1
		while(i<3):
			if i<2:
				number+=(float (row[7][i])*10**j)#数据为几十亿，取前三位，后面单位由元转换为十亿
				i=i+1
				j=j-1
			else:
				number+=(float(row[7][i])/10)
				i=i+1
				j=j-1
		finace.append(number)
	fig, ax1 = plt.subplots()
	ax2 = ax1.twinx()
	ax1.plot(date, price, 'g-')
	ax2.plot(date, finace, 'b-')
	ax1.set_xlabel('日期')
	ax1.set_ylabel('收盘价(单位/元) 绿色曲线')
	ax2.set_ylabel('融资融券余额(单位/亿)  蓝色曲线')
	ax1.set_title('%s   收盘价/融资融券余额'%row[6])
	plt.show()

win = tk.Tk()
win.title("股票分析系统")   
win.geometry('500x200+550+230')

label1=ttk.Label(win, text="请输入你要查询的股票代码:")
label1.grid(row=0,column=0 )    

nameEntered = tk.Entry(win, width=10)  
nameEntered.grid(row=0,column=1 )  
nameEntered.focus()  

query_stock_code=ttk.Button(win, text="查询",command=clickMe)
query_stock_code.grid(row=0, column=2)
#----------------------------------------------------------功能模块一----------------------------------------------------------------------------------
label2=ttk.Label(win, text="进行组合查询:")
label2.grid(row=4,column=0 )    
 
label3=ttk.Label(win, text="输入查询起始日期")
label3.grid(row=4,column=1 )


label4=ttk.Label(win, text="输入查询截止日期")
label4.grid(row=5,column=1 )


label5=ttk.Label(win, text="融资增减比例")
label5.grid(row=6,column=1 )

label6=ttk.Label(win, text="股价涨跌幅")
label6.grid(row=7,column=1 )

label10=ttk.Label(win, text="developed by wyh196646")
label10.grid(row=15,column=1)

startdate= tk.Entry(win, width=12)  
startdate.grid(row=4,column=3 ) 
startdate.insert(10,"2019-3-18")

finaldate = tk.Entry(win, width=12)  
finaldate.grid(row=5,column=3 )
finaldate.insert(10,'2019-4-03')


financing = ttk.Combobox(win, width=12)
financing['values'] = ["增加10%","增加20%","增加30%","减少10%","减少20%","减少30%"]   # 设置下拉列表的值
financing.grid( row=6,column=3)      # 设置其在界面中出现的位置  column代表列   row 代表行
financing.current(0)  


stockprincechange = ttk.Combobox(win, width=12 )
stockprincechange['values'] ="上涨10%","上涨20%","上涨30%","下跌10%","下跌20%","下跌30%"     # 设置下拉列表的值
stockprincechange.grid( row=7,column=3)      # 设置其在界面中出现的位置  column代表列   row 代表行
stockprincechange.current(0)  

label7=ttk.Label(win, text="进行组合查询")
label7.grid(row=10,column=1)

query_stock=ttk.Button(win, text="查询:",command=Combination_query)
query_stock.grid(row=10, column=3)
#--------------------------------------------------功能模块二---------------------------------------------------------------------

win.mainloop()  
