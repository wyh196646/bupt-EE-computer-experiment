import pymysql
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimHei']#中文标签正常使用
conn = pymysql.connect(
	host='localhost',
	user='root',
	password='wyh19990713',
	database='stock',
    charset='utf8')
cursor = conn.cursor() 
sql = "select * from data where Date ='2019-3-18' or Date='2019-4-03'"
cursor.execute(sql)
results = cursor.fetchall()
conditionStockName=[]
conditionStockNumber=[]
i=0
k=0
while(i<len(results)-1):
	pricegap=(float(results[i+1][2])-float(results[i][2]))/float(results[i][2])
	finace=(float(results[i+1][7][0:3])-float(results[i][7][0:3]))/float(results[i][7][0:3])
	if((pricegap>0.1)&(finace>0.1)):
		conditionStockName.append(results[i][6])
		k=k+1
	i+=2
print(conditionStockName)
