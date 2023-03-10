print("Nhap don gia M1,M2,M3:")
M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
S=int(input("S="))
if S<=100:
    print("Phai tra="+str((M1*100)))
elif 101<=S<=150:
    print("Phai tra="+str((M1*100)+(S-100)*M2))
elif S>151:
    print("Phai tra="+str((M1*100)+50*20+(S-150)*M3))
