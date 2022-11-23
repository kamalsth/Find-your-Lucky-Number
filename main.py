import add
import cal
import display

print("Enter your date of birth")
a=int(input("Enter Year:: "))
yr=cal.cal(a)
b=int(input("Enter Month:: "))
mth=cal.cal(b)
c=int(input("Enter Day:: "))
day=cal.cal(c)

birth=add.add(yr,mth,day)

print("\nEnter the time of Birth")
h=int(input("Enter Hours:: "))
hr=cal.cal(h)
m=int(input("Enter Minutes:: "))
min=cal.cal(m)
s=int(input("Enter Second:: "))
sec=cal.cal(s)

time=add.add(hr,min,sec)

total=add.add(birth,time,0)
while total>=10:
    total=cal.cal(total)

display.display(a,b,c,h,m,s,total)
