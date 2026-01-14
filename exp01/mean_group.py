class_lower=[]
class_higher=[]
freq=[]
midpoint=[]

n=int(input("Enter the number of classes: "))
for i in range(n):
    a=int(input(f"Enter Lower limit of class {i+1}"))
    b=int(input(f"Enter higher limit of class {i+1}"))
    c=int(input(f"Enter the freq of class {i}"))
    class_lower.append(a)
    class_higher.append(b)
    freq.append(c)
    midpoint.append((a+b)/2)

assumeed_mean=midpoint[int(n/2)]
class_width=class_higher[0]-class_lower[0]

sum=0
sum2=0
for i in range(n):
    sum+=freq[i]*((midpoint[i]-assumeed_mean)/class_width)
    sum2+=freq[i]

mean=assumeed_mean + (class_width * (sum/sum2))

print("Mean of the given data is: ",mean)


    
    