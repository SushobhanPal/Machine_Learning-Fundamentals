class_lower=[]
class_higher=[]
freq=[]
midpoint=[]
c_freq=[]

n=int(input("Enter the number of classes: "))
for i in range(n):
    a=int(input(f"Enter Lower limit of class {i+1}: "))
    b=int(input(f"Enter higher limit of class {i+1}: "))
    c=int(input(f"Enter the freq of class {i+1}: "))
    class_lower.append(a)
    class_higher.append(b)
    freq.append(c)
    midpoint.append((a+b)/2)

#Mean
assumed_mean=midpoint[n//2]
h=class_higher[0]-class_lower[0]

sum1=0
sum2=0
for i in range(n):
    sum1+=freq[i]*((midpoint[i]-assumed_mean)/h)
    sum2+=freq[i]
    c_freq.append(sum2)

mean=assumed_mean + (h * (sum1/sum2))

print("Mean of the given data is: ",mean)


# Median
for i in range(n):
    if(c_freq[i]>=(sum2/2)):
        median_class=i
        break

l=class_lower[median_class]
f=freq[median_class]
cf=0 if median_class==0 else c_freq[median_class-1]

median = l+(h*(((sum2/2)-cf)/f))

print("Median is ",median)
    
#Mode
f0=max(freq)
modal_class=freq.index(f0)
l_m=class_lower[modal_class]
f1=freq[modal_class-1] if modal_class>0 else 0
f2=freq[modal_class+1] if modal_class<n-1 else 0



mode = l_m+(((f0-f1)/(2*f0-f1-f2))*h)

print("Mode: ",mode)