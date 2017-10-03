r1=input("enter lower range")
r2=input("enter higher range")
for num in range(r1,r2+1):
  sum=0
  temp=num
  o=len(str(num))
  while temp>0:
    r=temp%10
    sum+=r**o
    temp//=10
if num==sum:
  print(num)
