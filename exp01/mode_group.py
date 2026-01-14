class_lower=[]
class_higher=[]
freq=[]
midpoint=[]
c_freq=[]

n=int(input("Enter the number of classes: "))
for i in range(n):
    a=int(input(f"Enter Lower limit of class {i+1}: "))
    b=int(input(f"Enter higher limit of class {i+1}: "))
    c=int(input(f"Enter the freq of class {i}: "))
    class_lower.append(a)
    class_higher.append(b)
    freq.append(c)
    midpoint.append((a+b)/2)