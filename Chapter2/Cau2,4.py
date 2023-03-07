a=int(input("nhap do dai canh thu nhat:"))
b=int(input("nhap do dai canh thu hai:"))
c=int(input(("nhap do dai canh thu ba:")))
S=(a+b+c)/2
X=S*(S-a)*(S-b)*(S-c)
import math
print("Dien tich=",math.sqrt(X))