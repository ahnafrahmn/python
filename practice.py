"""
                             <<<<<::  PYTHON  ::>>>>>

======================================================================================================
Hello this is Ahnaf. I'll be writing here my "PYTHON" codes. 

Topics : 
=======
1]  printing "Hello" .
2]  taking inputs and printing them. 
3]  taking input of two integers and do all arithmetic operations with them (+, -, *, /, %).
4]  use of constants and write programs to find the

            a) average of three numbers.

            b) Area and circumference of a circle using constant.

            c) area of rectangle, square and triangle.

5]  using math functions to get the value of 'x' from the equation : 'ax^2 + bx + c = 0' 
    where a,b,c are constant integers.
6]  using follwing math functions:
        1
        ceil(x)
        Return the Ceiling value. It is the smallest integer, greater or equal to the number x.
        2	
        copysign(x, y)
        It returns the number x and copy the sign of y to x.
        3	
        fabs(x)
        Returns the absolute value of x.
        4	
        factorial(x)
        Returns factorial of x. where x ≥ 0
        5	
        floor(x)
        Return the Floor value. It is the largest integer, less or equal to the number x.
        6	
        fsum(iterable)
        Find sum of the elements in an iterable object
        7	
        gcd(x, y)
        Returns the Greatest Common Divisor of x and y
        8	
        isfinite(x)
        Checks whether x is neither an infinity nor nan.
        9	
        isinf(x)
        Checks whether x is infinity
        10	
        isnan(x)
        Checks whether x is not a number.
        11	
        remainder(x, y)
        Find remainder after dividing x by y.
        12
        pow(x, y)
        Return the x to the power y value.
        13	
        sqrt(x)
        Finds the square root of x
        14	
        exp(x)
        Finds xe, where e = 2.718281
        15	
        log(x[, base])
        Returns the Log of x, where base is given. The default base is e
        16
        log2(x)
        Returns the Log of x, where base is 2
        17	
        log10(x)
        Returns the Log of x, where base is 10
        18
        sin(x)
        Return the sine of x in radians
        19
        cos(x)
        Return the cosine of x in radians
        20	
        tan(x)
        Return the tangent of x in radians
        21
        asin(x)
        This is the inverse operation of the sine, there are acos, atan also.
        22	
        degrees(x)
        Convert angle x from radian to degrees
        23	
        radians(x)
        Convert angle x from degrees to radian
    

7]  if..else conditions and elif ladder
8]  using loops and nested loops
9]  functions (with/without parameters and with/without return)
10]  lists
11]  Dictionary
12]  .
13]  .
14]  .
15]  .
16]  .
17]  .
18]  .
19]  .
20]  .
21]  .
22]  .
23]  .
24]  .
25]  .
26]  .
27]  .
28]  .
29]  .

<<:: EXERCISES ::>>
 =================
        1. use nested loops for drawing patterns.
        2. Write a program to do the matrix multiplication.
        3. Write a program to do the matrix Addition.
        4. Write a program using user defined function (with parameter with return type) to compare bigger value from a list.
        5. Write a program using function (with parameter with return type) to swap  2 numbers.
        6. Write a program to pass the result of one function to another function.
        7. Write a program to calculate the factorial of a number by using recursion function.
        8. Use if else inside a function to check whether a number is divisible by both 8 and 5 or not.
        9. Write a program using with return type with parameter function to return even number to the main function
        10. Write a program using function to check the minimum and maximum number from a group of numbers.
        11. Write a program where each function will contain one type of number,
            for example (prime, spy, perfect, composite, even, odd, palindrome, sunny ).
        12. Write a programs with a list  for given operations 
            (searching, sorting, minimum, maximum, frequency, storing, deleting).

            
            
========================================================================================================================
========================================================================================================================
========================================================================================================================

                                  <<<<<  Practice >>>>>



#Topic-1 >>>>>>>>>>

print("Hello")

#Topic-2 >>>>>>>>>>

a = int(input("Enter an integer : "))
b = float(input("Enter a floating number : "))
c = str(input("Enter a word/sentence : "))
import os
os.system("cls")
print(a, "\n", b, "\n", c, sep='')

#Topic-3 >>>>>>>>>>

a, b = input("Enter 2 integers : ").split(" ")
a, b = int(a), int(b)
print(f" a={a} \t b={b}")
print(f" a+b = {a+b}")
print(f" a-b = {a-b}")
print(f" a*b = {a*b}")
print(f" a/b = {a/b}")
print(f" a%b = {a%b}")

#Topic-4 >>>>>>>>>>

(a)
a, b, c = input("Enter 3 numbers : ").split()
a, b, c = int(a) , int(b), int (c)
print(f"Average of {a}, {b}, {c} is : {int((a+b+c)/3)}")

(b)
pi = 3.1416
radius = float(input("Enter radius : "))
print(f" Area of the Circle is : {pi*radius*radius:.2f}\n Circumference of the circle is : {round(2*pi*radius, 2)}")#used 2 metods for 2 deciamal points

(c)
a, b = int(input("Enter height : ")), int(input("Enter width : "))
print(f"Area of the rectangle is : {a*b}")
a = int(input("Enter length of one side of the square : "))
print(f"Area of the square is : {a*a}")
a, b = int(input("Enter height : ")), int(input("Enter base : "))
print(f"Area of the rectangle is : {0.5*a*b:.0f}")

#Topic-5 >>>>>>>>>>

import math as m
a, b, c = input("Enter the values of a, b, c\nfor ax^2 + bx + c = 0\n:> ").split(" ") 
a, b, c = int(a), int(b), int(c)
x1 = float((-b + m.sqrt(pow(b,2)-4*a*c))/(2*a))
x2 = float((-b - m.sqrt(pow(b,2)-4*a*c))/(2*a))
print(f"Here, \n x = {x1:.2f} , {x2:.2f}")

#Topic-6 >>>>>>>>>>

Did not write it cause I am going to apply those math functions in my other programs anyway.
I'd obviously practice them!

#Topic-7+8 >>>>>>>>>>

# Let, bal = the balance user has, Suppose he/she has 5000 BDT in his/her account
# Let, pin = his/her PIN number, suppose it is 1234
bal = 5000
pin = str(1234)
temp = ""
while temp!=pin:    # for repeating until user enters valid PIN
    temp = str(input("Enter your PIN : "))
print(f"\t\t\t ATM \n\nYour account balance is {bal} BDT\n\n")
i=True
while i:  # for repeating until user enters valid amount
    # Let, n = the amount user wants to withdraw 
    n = int(input(f"Enter the amounnt you want to withdraw : ")) 
    if n%500>0 or n<0 or n>bal:
        print("You cannot withdraw this amount.\nPlease try again.\n")
    else: i=False
i = True
while i:
    temp = int(input(f"Confirm that you want to withdraw {n} BDT \n (1)YES \t (2)NO\n:> "))
    if temp==1:
        i=False
        bal = bal-n
        print(f"Successful withdrawal!\nYour new balance is {bal} BDT\nThank you so much!")
    elif temp==2:
        i=False
        print("Thank you!")
    else: 
        print("Invalid Input\nTry again")

        
#Topic-8(Nested Loop) >>>>>>>>>>

>>>> PATTERN :
                Shape : 
                *
                * *
                * * *
>>>> CODE :

n = int(input("Enter a number : "))
for i in range(n+1):
    for j in range(i):
        print(" *", end="")
    print()

    
#Topic-9 >>>>>>>>>>

def main():
    a, b = input("Enter 2 integers : ").split(" ") 
    a, b = int(a), int(b)
    t = int(input("Which arithmatic operation you want to do ?\n (1)+\t(2)-\t(3)*\t(4)/\t(5)%\n"))
    if t==1:
        add(a, b)
    elif t==2:
        sub(a,b)
    elif t==3:
        mul(a,b)
    elif t==4:
        div(a,b)
    elif t==5:
        mod(a,b)
    

def add(a, b):
    print(a+b)
def sub(a, b):
    print(a-b)
def mul(a, b):
    print(a*b)
def div(a, b):
    print(a/b)
def mod(a, b):
    print(a%b)

main()


#Topic-10 >>>>>>>>>>

# Lists

fruits = ["apples", "bananas", "mangoes", "grapes"]
friends = ["Robert", "Raj", "Sam", "Sherlock"]
numbers = [5, 7, 3, 9]

for fruit, friend, number in zip(fruits, friends, numbers):  # zip() is used to access 2 lists at the same time
    print(f"{friend} loves {fruit} and his lucky number is {number}")


mix_info = ["Ahnaf Rahman", 21, "male", "Dhaka, Bangladesh"]
            #  name      , age,  sex,        my city

# we can get the values of the lists by their position in the list. remeber that the indexing of the lists starts from 0.
# so the first item's position is 0

i = mix_info # it's nothing, just taking 'i' instead of 'mix_info' because 'i' is a short variable name to use  
print(f"My name is {i[0]}. I am {i[1]} years old.\nSex : {i[2]}.\nCity of birth : {i[3]}.")

-----------------------------------------------------------------


   Matrix Operations:
 ---------------------

def show_matrix(mat=None, row=0, col=0):
    if mat==None:
        print("Sample Matrix with it's positions : ")
        for i in range(row):
            for j in range(col):
                print(f"'{i+1}{j+1}'", end=' ')
            print()
    else:
        print("Matrix : \n")
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end='  ')
            print()

def input_matrix(mat, row, col):
    show_matrix(None, row, col)
    print("Enter values of the Matrix : \n")
    for i in range(row):
        a = []
        for j in range(col):
            x = int(input(f"Enter the value for position {i+1}{j+1} : "))
            a.append(x)
        mat.append(a)
        print()
    show_matrix(mat, row, col)

def add_matrix(m1, m2 ,r, c):
    t=[]
    for i in range(r):
        a=[]
        for j in range(c):
            a.append(m1[i][j]+m2[i][j])
        t.append(a)
        print()
    return t

def multiply_matrix(m1, m2 ,r1, c1, r2, c2): # result matrix will have row=r1, column=c2
    t=[]
    for i in range(r1):
        a=[]
        for j in range(c2):
            sum, k = 0, 0
            for k in range(c2):
                sum += m1[i][k]*m2[k][j] 
            a.append(sum)
        t.append(a)
        print()
    return t

def matrix():
    x = input("Enter rows  and columns of the 1st matrix : ")
    r1, c1 = [int(_) for _ in x.split(" ")]
    x = input("Enter rows  and columns of the 2nd matrix : ")
    r2, c2 = [int(_) for _ in x.split(" ")]
    mat1 , mat2 =[] , []
    temp = int(input("What operation do you want to do ?\n1)Addition \t 2)Multiplication\n :>"))

    match temp:
        case 1:
            if r1==r2 and c1==c2:
                print("Enter the values for 1st matrix : "); input_matrix(mat1, r1, c1)
                print("-----------------------------------")
                print("Enter the values for 2nd matrix : "); input_matrix(mat2, r2, c2)
                print("-----------------------------------")
                tempMat = add_matrix(mat1, mat2, r1, c1)
                print("Resut", end=' ')
                show_matrix(tempMat, r1, c1)
                print("-----------------------------------")
            else:
                print("Cannot add with these rows and columns!")
        case 2:
            if c1!=r2:
                print("Cannot multiply with these rows and columns!")
            else:
                print("Enter the values for 1st matrix : "); input_matrix(mat1, r1, c1)
                print("-----------------------------------")
                print("Enter the values for 2nd matrix : "); input_matrix(mat2, r2, c2)
                print("-----------------------------------")
                tempMat = multiply_matrix(mat1, mat2, r1, c1, r2, c2)
                print("Resut", end=' ')
                show_matrix(tempMat, r1, c1)
                print("-----------------------------------")

matrix()

-----------------------------------------------------------------------------

#   bigger value from a list

def maximum(a):
    temp=a[0]
    for i in range(len(a)-1): 
        if temp<a[i+1]: 
            temp=a[i+1]
    return temp

nums = [5, 23, 31, 1, 90, 21, 76]
print(f"Given list : {nums} \nThe maximum value is : {maximum(nums)}")


==============================================================================================================
"""





