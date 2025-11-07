#1Check if a given number is positive, negative, or zero.
""" n=int(input('enter a number: '))
if n==0:
    print('zero')
elif n>0:
    print('positive number')
else:
    print('negative number') """

#2Find out whether a person is eligible to vote (age ≥ 18).

""" age=int(input('enter your age: '))
if age>=18:
    print('you are eligible to vote')

else:
    print('you are not eligible to vote') """

#3Given a number, check if it is even or odd.
""" n=int(input('enter a number: '))

if n==2 or n%2==0:
    print(f'{n} is an even number')

else:
    print(f'{n} is an odd number') """

#4Write a program to find the largest of three numbers.

""" numbers=[100,22,182]
large_num=0
for i in numbers:
    if i>large_num:
        large_num=i
print(large_num) """

#5Ask the user for a password — print “Access Granted” if correct, otherwise “Access Denied”.
""" key='He110 W0rld'
password=input('please enter the password: ')
if password==key:
    print('Access Granted')         
else:
     print('Access Denied') """

#6Write a program that checks if a year is a leap year.
""" year=int(input('enter the year: '))

if year%400==0:
    print('leap year')
elif year%100==0:
    print('not a leap year')
elif year%4==0:
    print('leap year')
else:
    print('not a leap year') """

#7Ask the user for marks and print the grade (A, B, C, D, F) based on score ranges.
""" marks=int(input('enter your marks: '))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F") """

#8Check if a given character is a vowel or consonant.
""" alphabet=input('enter the character: ')
vowels=['a','e','i','o','u']
for i in vowels:
    if alphabet==i:
        print('vowel')
        break
else:
    print('consonant') """

#9Write a program that checks if a number is divisible by both 3 and 5.
""" n=int(input('enter a number: '))
if n%3==0 and n%5==0:
    print('yes divisible by both 3 and 5')
else:
    print('not divisible by both 3 and 5') """

#10Write a small login simulation — if username and password match, print “Welcome”; else print “Invalid credentials”.