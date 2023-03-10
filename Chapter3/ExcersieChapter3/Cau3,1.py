import math
print("Nhap 3 canh cua mot tam giac:")
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
p=(a+b+c)/2
if (a+b)>c:
    if (a+c)>b:
        if (b+c)>a:
            print("Dien tich="+str(round(math.sqrt((p*(p-a)*(p-b)*(p-c))),3)))
else:
    print("Khong hop le")