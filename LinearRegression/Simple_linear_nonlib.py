#import statistics
x=[]
y=[]
avg_x=0
avg_y=0

n=int(input("enter number of elements: "))

#Taking input
for i in range (n):
    x.append(float(input("Enter the value of x: ")))
    y.append(float(input("Enter the value of y: ")))

#finding Avrage
for i in range(n):
    avg_x+=x[i]
    avg_y+=y[i]

'''Alternative method to find the avrage 
   avg_x=statistics.mean(x)
   avg_y=statistics.mean(y)
'''

#finding numerator and denom of m
num=0
denom=0
for i in range (n):
    num+=((x[i]-avg_x)*(y[i]-avg_y))
    denom+=((x[i]-avg_x)**2)

#finding equation
m=num/denom
c=avg_y-m*avg_x
print(f"Equation is : Y ={m}*X + {c}")

a=float(input("enter value of X to find Y: "))
b=(m*a)+c
print("Y = ",b)

