print("Write a PYTHON program to evaluate the student performance")

per=float(input("Enter your Percentage:"))
if per>=90:
    print("Excellent performance")
elif per>=80:
    print("Very Good performance")
elif per>=70:
    print("Good performance")
elif per>=60:
    print("average performance")
else:
    print("Poor performance")


print("Write a PYTHON program to find largest of three numbers.")

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a>b and a>c:
    print(a,"is largest")
elif b>c and b>a:
    print(b,"is largest")
else:
    print(c,"is largest")


print("Write a PYTHON program to find smallest of three numbers")

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a<b and a<c:
    print(a,"is smaller")
elif b<c and b<a:
    print(b,"is smaller")
else:
    print(c,"is smaller")
