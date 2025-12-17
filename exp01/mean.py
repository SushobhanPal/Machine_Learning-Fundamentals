li=[]
sum=0
for i in range(0,7):
    li.append(int(input("enter element")))
    sum+=li[i]

mean =sum/7

print("mean is ", mean)