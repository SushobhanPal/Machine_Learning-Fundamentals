li=[]
n=int(input("enter how many datas to be entered\n"))
for i in range(n):
    li.append(int(input("enter element")))
li.sort()
li_count=[]
li_mode=[]

for i in range (n):
    count=0;
    for j in range(i,n):
        if(li[i]==li[j]):
            count+=1
    li_count.append(count)
    li_mode.append(li[i])
    
maximum=max(li_count)

mode=li_mode[li_count.index(maximum)]

print("Mode is  is ",mode)
print(maximum)
print(li_mode)
print(li_count)

    