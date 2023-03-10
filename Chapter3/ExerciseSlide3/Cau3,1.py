print("Nhap 3 so thuc:")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a<b:
    if a>c:
        print("SLN="+str(b))
        print("SBN="+str(c))
    if b<c:
        print("SLN="+str(c))
        print("SBN="+str(a))
elif a>b:
    if a<c:
        print("SLN="+str(c))
        print("SBN="+str(b))