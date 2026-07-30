print("Write a PYTHON program to print the natural numbers up to n")
n=int(input("Enter size of n:"))
i=1
while i<=n:
    print(i)
    i+=1

print("Write a PYTHON program to print even numbers up to n")
n=int(input("Enter n: "))
i=2
while i<=n:
    print(i)
    i=i+2
        

print("Write a PYTHON program to print odd numbers up to n")
n=int(input("Enter n: "))
i=1
while i<=n:
    print(i)
    i=i+2


print("Write a PYTHON program to print sum of natural numbers up to n")
n = int(input("Enter n: "))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print("Sum =",sum)


print("Write a PYTHON program to print sum of odd numbers up to n")
n=int(input("Enter n: "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+2
print(sum)

print("Write a PYTHON program to print sum of even numbers up to ")
n=int(input("Enter size of n:"))
i=2
sum=0
while i<=n:
    sum=sum+i
    i=i+2
print(sum)


print("Write a PYTHON program to print natural numbers up to n in reverse order.")
n=int(input("Enter size of n:"))
while n>=1:
    print(n)
    n=n-1


print("Write a PYTHON program to print Fibonacci series up to n")
n=int(input("Enter n: "))
a=0
b=1
while a<=n:
    print(a)
    c=a+b
    a=b
    b=c

print("Write a PYTHON program  find a factorial of given number")
n=int(input("Enter a number: "))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print("Factorial =",fact)


print("Write a PYTHON program to check the entered number is prime or not")
n=int(input("Enter a number: "))
i=2
while i<n:
    if n%i==0:
        print("Not Prime")
        break
    i=i+1
else:
    print("Prime")


print("Write a PYTHON program to find the sum of digits of given number")
n=int(input("Enter a number: "))
sum=0
while n>0:
    sum=sum+n%10
    n=n//10
print("Sum =",sum)


print("Write a PYTHON program to check the entered  number is palindrome or no")
n=int(input("Enter a number: "))
temp=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n = n // 10
if temp==rev:
    print("Palindrome")
else:
    print("Not Palindrome")


print("Write a PYTHON program to reverse the given number.")
n=int(input("Enter a number: "))
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
print("Reverse =",rev)


print("Write a PYTHON program to print the multiplication table")
n=int(input("Enter a number: "))
i=1
while i<=10:
    print(n,"*",i,"=",n*i)
    i=i+1


print("Write a PYTHON program to print the largest of n numbers")
n=int(input("Enter how many numbers: "))
i=1
largest=int(input("Enter number: "))
while i<n:
    x=int(input("Enter number: "))
    if x>largest:
        largest=x
    i=i+1
print("Largest =",largest)


print("Write a PYTHON program to print smallest of n numbers")
n=int(input("Enter how many numbers: "))
i=1
smallest=int(input("Enter number: "))
while i<n:
    x=int(input("Enter number: "))
    if x<smallest:
        smallest=x
    i=i+1
print("Smallest =",smallest)
