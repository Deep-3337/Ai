#1
# pi=22/7
# degree = float(input("Input degrees: "))
# radian = degree*(pi/180)
# print(radian)

#o/p:- Input degrees: 15
# 0.2619047619047619

# 2
# pi=22/7
# radian = float(input("Input radians: "))
# degree = radian*(180/pi)
# print(degree)

# o/p :- Input radians: 1
# 57.27272727272727

# 3
# l_base = float(input("Input Long base : "))
# s_base = float(input("Input Short base : "))
# height = float(input("Input Height : "))
# area = ((l_base+s_base)/2)*height
# print("Area of trapezoid is ",area)

# o/p :- Input Long base : 5
# Input Short base : 5
# Input Height : 6
# Area of trapezoid is  30.0

# 4
# b = float(input("Input Base of parallelogrom : "))
# h = float(input("Input Height of parallelogrom : "))

# area = b*h
# print("Area is : ",area)

# o/p :- Input Base of parallelogrom : 5
# Input Height of parallelogrom : 6
# Area is :  30.0

# 5
# pi=22/7
# height = float(input("Height of cylinder: "))
# radius = float(input("Radius of cylinder: "))
# volume = pi * radius * radius * height
# sur_area = ((2*pi*radius) * height) + ((pi*radius**2)*2)
# print("Volume is: ", volume)
# print("Surface Area is: ", sur_area)

# o/p :- Height of cylinder: 4
# Radius of cylinder: 6
# Volume is:  452.57142857142856
# Surface Area is:  377.1428571428571

# 6
# pi=22/7
# radian = float(input("Radius of sphere: "))
# sur_area = 4 * pi * radian **2
# volume = (4/3) * (pi * radian ** 3)
# print("Surface Area is: ", sur_area)
# print("Volume is: ", volume)

# o/p :- Radius of sphere: .75
# Surface Area is:  7.071428571428571
# Volume is:  1.7678571428571428

# 7
# pi=22/7
# diameter = float(input("Diameter of circle: "))
# angle = float(input("Angle measure: "))
# arc_length = (pi*diameter) * (angle/360)
# print("Arc Length is: ", arc_length)

# o/p :- Diameter of circle: 8
# Angle measure: 45
# Arc Length is:  3.142857142857143

# 8
# pi=22/7
# radius = float(input("Radius of Circle: "))
# angle = float(input("Angle measure: "))
# sur_area = (pi*radius**2) * (angle/360)
# print("Sector Area: ", sur_area)

# o/p :- Radius of Circle: 4
# Angle measure: 45
# Sector Area:  6.285714285714286

# 9
# def discriminant():
#     x_value = float(input("The x value: "))
#     y_value = float(input("The y value: "))
#     z_value = float(input("The z value: "))
#     discriminant = (y_value**2) - (4*x_value*z_value)
#     if discriminant > 0:
#         print("Two Solutions. Discriminant value is:", discriminant)
#     elif discriminant == 0:
#         print("One Solution. Discriminant value is:", discriminant)
#     elif discriminant < 0:
#         print("No Real Solutions. Discriminant value is:", discriminant)


# discriminant()

# 10
# def smallest_multiple(n):
#     if (n<=2):
#       return n
#     i = n * 2
#     factors = [number  for number in range(n, 1, -1) if number * 2 > n]
#     print(factors)

#     while True:
#         for a in factors:
#             if i % a != 0:
#                 i += n
#                 break
#             if (a == factors[-1] and i % a == 0):
#                 return i
                
# print(smallest_multiple(13))

# 11
# def sum_difference(n=2):
#     sum_of_squares = 0
#     square_of_sum = 0
#     for num in range(1, n+1):
#         sum_of_squares += num * num
#         square_of_sum += num

#     square_of_sum = square_of_sum ** 2

#     return square_of_sum - sum_of_squares


# print(sum_difference(12))

# 12
# def power_base_sum(base, power):
#     return sum([int(i) for i in str(pow(base, power))])


# print(power_base_sum(2, 100))

# 13
# def is_abundant(n):
#     fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
#     return fctr_sum > n
# print(is_abundant(12))
# print(is_abundant(13))

# 14
# def amicable_numbers_sum(limit):
#     if not isinstance(limit, int):
#         return "Input is not an integer!"

#     if limit < 1:
#         return "Input must be bigger than 0!"

#     amicables = set()

#     for num in range(2, limit+1):
#         if num in amicables:
#             continue

#         sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])
#         sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])
#         if num == sum_fact2 and num != sum_fact:
#             amicables.add(num)
#             amicables.add(sum_fact2)

#     return sum(amicables)


# print(amicable_numbers_sum(9999))
# print(amicable_numbers_sum(999))
# print(amicable_numbers_sum(99))

# 15
# def sum_div(number):
#     divisors = [1]
#     for i in range(2, number):
#         if (number % i)==0:
#             divisors.append(i)
#     return sum(divisors)
# print(sum_div(8))
# print(sum_div(12))

# 16
# def permute_string(str):
#     if len(str) == 0:
#         return ['']
#     prev_list = permute_string(str[1:len(str)])
#     next_list = []
#     for i in range(0,len(prev_list)):
#         for j in range(0,len(str)):
#             new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
#             if new_str not in next_list:
#                 next_list.append(new_str)
#     return next_list

# print(permute_string('ABCD'))

# 17
# n=int(input("Input a Number: "))
# List=range(-1,n*n+9,2)
# i=2
# while List[i:]:List=sorted(set(List)-set(List[List[i]::List[i]]));i+=1
# print(List[1:n+1])

# 18
# def BabylonianAlgorithm(number):
#     if(number == 0):
#         return 0

#     g = number/2.0
#     g2 = g + 1
#     while(g != g2):
#         n = number/ g
#         g2 = g
#         g = (g + n)/2

#     return g
# print('The Square root of 0.3 =', BabylonianAlgorithm(0.3))

# 19
# def multiply(x, y):
#     if y < 0:
#         return -multiply(x, -y)
#     elif y == 0:
#         return 0
#     elif y == 1:
#         return x
#     else:
#         return x + multiply(x, y - 1)

# print(multiply(2, 3))

# 20
# def magic_square_test(my_matrix):
#     iSize = len(my_matrix[0])
#     sum_list = []
    
#     #Horizontal Part:
#     sum_list.extend([sum (lines) for lines in my_matrix])   

#     #Vertical Part:
#     for col in range(iSize):
#         sum_list.append(sum(row[col] for row in my_matrix))
    
#     #Diagonals Part
#     result1 = 0
#     for i in range(0,iSize):
#         result1 +=my_matrix[i][i]
#     sum_list.append(result1)  
    
#     result2 = 0
#     for i in range(iSize-1,-1,-1):
#         result2 +=my_matrix[i][i]
#     sum_list.append(result2)

#     if len(set(sum_list))>1:
#         return False
#     return True

# m=[[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]] 
# print(magic_square_test(m))

# m=[[2, 7, 6], [9, 5, 1], [4, 3, 8]]
# print(magic_square_test(m))

# m=[[2, 7, 6], [9, 5, 1], [4, 3, 7]]
# print(magic_square_test(m))

# 21
# def sieve_of_Eratosthenes(num):
#     limitn = num+1
#     not_prime_num = set()
#     prime_nums = []

#     for i in range(2, limitn):
#         if i in not_prime_num:
#             continue

#         for f in range(i*2, limitn, i):
#             not_prime_num.add(f)

#         prime_nums.append(i)

#     return prime_nums

# print(sieve_of_Eratosthenes(50))

# 22
# import sys
# def Next_smallest_Palindrome(num):
#     numstr = str(num)
#     for i in range(num+1,sys.maxsize):
#         if str(i) == str(i)[::-1]:
#             return i

# print(Next_smallest_Palindrome(99))

# 23
# def Previous_Palindrome(num):
#     for x in range(num-1,0,-1):
#         if str(x) == str(x)[::-1]:
#             return x
# print(Previous_Palindrome(99))

# 24
# from fractions import Fraction
# value = 2.3
# print(Fraction(value).limit_denominator())

# 25
# def catalan_number(num):
#     if num <=1:
#          return 1
   
#     res_num = 0
#     for i in range(num):
#         res_num += catalan_number(i) * catalan_number(num-i-1)
#     return res_num
 
# for n in range(10):
#     print(catalan_number(n))

# 26
# print("{:,}".format(1000000))
# print("{:,}".format(10000))

# 27
# from math import radians, sin, cos, acos

# print("Input coordinates of two points:")
# slat = radians(float(input("Starting latitude: ")))
# slon = radians(float(input("Ending longitude: ")))
# elat = radians(float(input("Starting latitude: ")))
# elon = radians(float(input("Ending longitude: ")))

# dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
# print("The distance is %.2fkm." % dist)

# 28
# from math import tan, pi
# n_sides = int(input("Input number of sides: "))
# s_length = float(input("Input the length of a side: "))
# p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
# print("The area of the polygon is: ",p_area)

# 29
# import math
# v = float(input("Input wind speed in kilometers/hour: "))
# t = float(input("Input air temperature in degrees Celsius: "))
# wci = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
# print("The wind chill index is", int(round(wci, 0)))

# 30
# from math import sqrt

# print("Quadratic function : (a * x^2) + b*x + c")
# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))

# r = b**2 - 4*a*c

# if r > 0:
#     num_roots = 2
#     x1 = (((-b) + sqrt(r))/(2*a))     
#     x2 = (((-b) - sqrt(r))/(2*a))
#     print("There are 2 roots: %f and %f" % (x1, x2))
# elif r == 0:
#     num_roots = 1
#     x = (-b) / 2*a
#     print("There is one root: ", x)
# else:
#     num_roots = 0
#     print("No roots, discriminant < 0.")
#     exit()

# 31
# b_num = list(input("Input a binary number: "))
# value = 0

# for i in range(len(b_num)):
# 	digit = b_num.pop()
# 	if digit == '1':
# 		value = value + pow(2, i)
# print("The decimal value of the number is", value)

# 32
# cn = complex(2,3)
# print("Complex Number: ",cn)
# print("Complex Number - Real part: ",cn.real)
# print("Complex Number - Imaginary part: ",cn.imag)

# 33
# print("Addition of two complex numbers : ",(4+3j)+(3-7j))
# print("Subtraction of two complex numbers : ",(4+3j)-(3-7j))
# print("Multiplication of two complex numbers : ",(4+3j)*(3-7j))
# print("Division of two complex numbers : ",(4+3j)/(3-7j))

# 34
# import cmath
# cn = complex(3,4) 
# print("Length of a complex number: ", abs(cn))
# print("Complex number Angle: ",cmath.phase(0+1j) )

# 35
# import cmath
# cn = complex(3,4)
# print("Polar Coordinates: ",cmath.polar(cn))
# cn1 = cmath.rect(2, cmath.pi)
# print("Polar to rectangular: ",cn1)

# 36
# from decimal import *
# data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
# print("Maximum: ", max(data))
# print("Minimum: ", min(data))


# 37
# from decimal import *
# data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
# print("Sum: ", sum(data))
# print("Sorted order: ", sorted(data))


# 38
# from decimal import *
# x = Decimal('1.44')
# print("Square root of ",x, " is :", x.sqrt())
# print("exponential of ",x, " is :", x.exp())


# 39
# import decimal
# context = decimal.getcontext()
# print('Emax     =', context.Emax)
# print('Emin     =', context.Emin)
# print('capitals =', context.capitals)
# print('prec     =', context.prec)
# print('rounding =', context.rounding)
# print('flags    =')
# for x, y in context.flags.items():
#     print('  {}: {}'.format(x, y))
# print('traps    =')
# for x, y in context.traps.items():
#     print('  {}: {}'.format(x, y))

# 40
import decimal

d = decimal.Decimal('00.26598')
print("Original Number : ",d)
for i in range(1, 5):
    decimal.getcontext().prec = i
    print("Precision-",i, ':', d * 1)
