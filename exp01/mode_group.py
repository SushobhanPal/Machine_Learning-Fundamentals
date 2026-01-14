class_lower=[]
class_higher=[]
freq=[]


n=int(input("Enter the number of classes: "))
for i in range(n):
    a=int(input(f"Enter Lower limit of class {i+1}: "))
    b=int(input(f"Enter higher limit of class {i+1}: "))
    c=int(input(f"Enter the freq of class {i+1}: "))
    class_lower.append(a)
    class_higher.append(b)
    freq.append(c)

f0=max(freq)
modal_class=freq.index(f0)
l=class_lower[modal_class]
f1=freq[modal_class-1] if modal_class>0 else 0
f2=freq[modal_class+1] if modal_class<n-1 else 0
    
h=class_higher[0]-class_lower[0]


mode = l+(((f0-f1)/(2*f0-f1-f2))*h)

print("Mode: ",mode)
