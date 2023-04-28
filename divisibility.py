#read a number  from user and
#check whether it is divisible by 3 or by 5 or by both

n=int(input("Enter a Number"))
if n%3==0 and n%5==0:
    print(n,"is divisible by 3 and 5 both")
elif n%3==0:
    print(n,"is divisible by 3 only")
elif n%5==0:
    print(n,"is divisible by 5 only");
else:
    print(n,"is not divisible by 3 or 5");
    
