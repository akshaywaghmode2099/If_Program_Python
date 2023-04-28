#read coordinates of a point in a 2-D plane
#and display it's quadrant

x=int(input("Enter x Coordinate"))
y=int(input("Enter y Coordinate"))

if x>0 and y>0:
    print((x,y),"lies in 1st quadrant")
elif x<0 and y>0:
    print((x,y),"lies in 2nd quadrant")
elif x<0 and y<0:
    print((x,y),"lies in 3rd quadrant")
elif x>0 and y<0:
    print((x,y),"lies in 4th quadrant")
else:
    print("point is a origin")
    
    
