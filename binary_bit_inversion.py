n=int(input("Enter number:"))
a=bin(n)
b=a[2:]
b=b.replace('0','y').replace('1','0').replace('y','1')
print(int(b,2))
