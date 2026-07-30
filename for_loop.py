
print("Write a PYTHON program to print the natural numbers up to n")

n=int(input("Enter size of natural numbers to print: "))
for i in range(1,n+1):
    print(i)


print("Write a PYTHON program to print even numbers up to n")
n=int(input("Enter size of numbers to print all even numbers to it: "))
for i in range(1,n+1):
    if i%2==0:
        print(i)


print("Write a PYTHON program to print odd numbers up to n")
n=int(input("Enter size of numbers to print all odd numbers to it: "))
for i in range(1,n+1):
    if i%2!=0:
        print(i)


print("Write a PYTHON program that prints  1 2 4 8 16 32 … n2")
n=int(input("Enter size of natural numbers:"))
val=1
for i in range(n):
    print(val)
    val=val*2


print("Write a PYTHON program to sum the given sequence 1 + 1/ 1! + 1/ 2! + 1/3! + ….  + 1/n!")
n = int(input("Enter the value of n: "))

sum_series = 1.0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    sum_series += 1 / factorial

print("Sum of the series =", sum_series)


print(" Write a PYTHON program to compute the cosine series cos(x) = 1 – x2 / 2! + x4 / 4! – x6 / 6! + … xn / n!")
x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 1
fact = 1
sign = -1

for i in range(2, 2 * n, 2):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum = sum + sign * (x ** i) / fact
    sign = -sign

print("Cosine series =", sum)


print(" Write a short PYTHON program to check weather the square root of number is prime or  not.")
import math

n=int(input("Enter a number: "))
s=int(math.sqrt(n))
print(s)

r=0
for i in range(1,s+1):
    if s%i==0:
        r+=1

if r==2:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")




print(" Write a PYTHON program to produce following design")
for i in range(3):
    for j in ['A','B','C']:
        print(j,end=" ")
    print()
			

print(" Write a PYTHON program to produce following design")
'''
      A
      A B
      A B C
      A B C D 
      A B C D E
      If user enters n value as 5
'''

n=int(input("Enter number to print value:"))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()


print("10. Write a PYTHON program to produce following design")
'''
       A B C D E
       A B C D
       A B C
       A B
       A                      
      (If user enters n value as 5)
'''
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
