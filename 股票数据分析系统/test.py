Alist=[0,1,0,1,1,0]
Blist=[1,1,0,0,0,0]
c='A&B'
q=[]
for (A,B) in zip(Alist,Blist):
	q.append(eval(c))
print(q)
