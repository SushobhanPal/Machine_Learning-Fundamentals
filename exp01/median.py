li=[]
n=int(input("enter how many datas to be entered\n"))
for i in range(n):
    li.append(int(input("enter element")))

li.sort()
if (n%2==0):
    median = (li[int(n/2)]+li[int((n/2)-1)])/2
else:
    median = li[int((n+1)/2)]
    
print("Medain is ", median)
