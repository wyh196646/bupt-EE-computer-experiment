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
sql = "SELECT date from data;" 
cursor.execute(sql)
results = cursor.fetchall()
stock_date=[]
for x in results:
	stock_date.append(x)
	
def deleteDuplicatedElementFromList2(list):
    resultList = []
    for item in list:
        if not item in resultList:
            resultList.append(item)
    return resultList
    
Alist=deleteDuplicatedElementFromList2(stock_date)
print(Alist)
