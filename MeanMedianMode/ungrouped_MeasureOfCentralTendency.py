li=[]
n=int(input("enter how many datas to be entered\n"))
for i in range(n):
    li.append(int(input("enter element")))

li.sort()
#mean

sum1=0
for i in range(n):
    sum1+=li[i]
mean =sum1/n

print("mean is ", mean)


#median

if (n%2==0):
    median = (li[int(n/2)]+li[int((n/2)-1)])/2
else:
    median = li[int((n+1)/2)]
    
print("Medain is ", median)

#mode

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


    