a=int(input("Tieu thu="))
VAT=0.1
if 1<=a<=100:
    b=a*550
elif 101<=a<=150:
    b=((100*550)+(a-100)*750)
elif 151<=a<200:
    b=((100*550)+(a-150)*950+50*750)
else:
    b=((100*550)+50*750+50*950+(a-200))
print("Phai tra="+str(b+b*VAT))