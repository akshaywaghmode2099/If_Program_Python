#read 4 numbers from user and display minimum number only

a=int(input("Enter first no"))
b=int(input("Enter second no"))
c=int(input("Enter third no"))
d=int(input("Enter fourth no"))
if a<b<c<d:
    print(a,"is the smallest no")
elif b<c<d:
    print(b,"is the smallest no")
elif c<d:
    print(c,"is the smallest no")
else:
    print("d is the smallest no")
