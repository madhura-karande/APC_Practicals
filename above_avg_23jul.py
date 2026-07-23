print("Write a PYTHON program to check weather number is even or odd.")

n=int(input("Enter a number:"))
if n%2==0:
    print(n,"is even")
else:
    print(n,"is odd")


print("Write a PYTHON program to check a year for leap year.")

y=int(input("Enter year:"))
if (y%4==0 and y%100!=0)or (y%400==0):
    print(y,"is leap year")
else:
    print(y,"is not leap year")


print("Write a PYTHON program to determine whether the driver is insured or not    ")
       
m=input("Are you Married:(yes/no)")
g=input("Enter your Gender:(male/female)")
a=int(input("Enter your age:"))
if m=='yes':
    print("Company will give you insurance!")
elif m=='no' and g=='male' and a>=30:
    print("Company will give you insurance!")
elif m=='no' and g=='female' and a>=25:
    print("Company will give you insurance!")
else:
    print("insurance is not allowed!")
