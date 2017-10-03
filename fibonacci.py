tot=input("enter a number")
n1=0
n2=1
n3=0
print(n1,n2)
for i in range(2,tot+1):
  n3=n1+n2
  print(n3)
  n1=n2
  n2=n3
  
