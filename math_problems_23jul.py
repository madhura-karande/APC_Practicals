
print("create  program to calculate area of triangle, volume of sphere, total surface area of cylinder,area of square")
print("Area of Triangle")
b=int(input("Enter Base value:"))
h=int(input("Enter Height:"))
at=0.5*b*h
print("Area of Triangle:",at)
print()
print("Volume of Sphere")
r=float(input("Enter Radius:"))
vs=4/3*3.14*r**3
print("Volume of Sphere:",vs)
print()
print("surface area of cylinder")
h1=int(input("Enter height:"))
r1=float(input("Enter radius:"))
sc=2*3.14*r1*(r1+h)
print("Total surface area of cylinder:",sc)
print()
print("area of square")
s=int(input("Enter side:"))
a=s*s
print("Area of square:",a)
print()
print()


print("write a program to convert pounds into kg, km into miles,")
p=int(input("Enetr pounds to convert into kg:"))
k=p*0.453592
print("Pounds into KG:",k)
print()
km=int(input("Enetr kilometers to convert into miles:"))
m=k*0.621371
print("Kilometers into miles:",m)
print()
print()


print("write a program to calculate factoria of a number")
n=int(input("Enter number:"))
f=1
for i in range(1,n+1):
   f=f*i
print("Factorial:",f)
print()
print()


print("write a proram to check whether the number is prime or not")
num=int(input("Enter a number:"))
if num>=1:
    print("Number is not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print("Number is not prime")
            break
        else:
            print("number is prime")
print()
print()


print("write a program to check the number is palindrome or not")
pa=int(input("Enter a Number:"))
rev=0
temp=pa
while pa>0:
    rem=pa%10
    rev=rev*10+rem
    pa=pa//10
if temp==rev:
    print("Palindrome")
else:
    print("Not paindrome")
print()
print()


print("write a program to convert decimal to binary, decimal to octal, decimal to hexadecimal")
d=int(input("Enter decimal value:"))
print("Decimal to binary conversion: ",bin(d))
print("Decimal to octal conversion: ",oct(d))
print("Decimal to hexadecima conversion: ",hex(d))
print()
print()



print("write a program to calculate factors of a number")
num=int(input("Enter a number:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)
print()
print()



print("write a program to find ascii value of a character")
ch=input("Enter a character:")
print("ASCII value of",ch,"is",ord(ch))
