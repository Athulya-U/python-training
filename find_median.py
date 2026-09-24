a=[]
b=[]
N1=int(input("Enter the value of N1:"))
N2=int(input("Enter the value of N2:"))
a=list(map(int,input("Enter the elements:").split()))
b=list(map(int,input("Enter the elements::").split()))
x=sorted(set(a+b))
l=len(x)
if l%2!=0:
  print("op=",x[l//2])
else:
    print("op=",(x[l//2-1]+x[l//2])/2)
