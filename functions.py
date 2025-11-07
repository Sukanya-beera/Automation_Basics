""" Types of Functions in Python
    (a) Built-in functions                       #print(), len(), type(), sum(), max(), min(), range(), etc.
    (b) User-defined functions                   #You create these using the def keyword
    (c) Lambda functions (anonymous functions) #optional  #Used for short, one-line operations.
    (d) Functions with default parameters        #You can assign a default value to parameters.
    (e) Functions with variable arguments        #Functions with variable arguments   """ 


#1.Write a function square(num) that returns the square of a number.
""" def square(num):
    return num**2
print(square(5)) """

#Write a function is_even(num) that checks whether a number is even or odd.
""" def is_even(num):
    if num%2==0:
        return 'even'
    else:
        return f'odd'
    
print(is_even(73))
print(is_even(22)) """

#Write a function calculate_area(length, width) that returns the area of a rectangle.
""" def calculate_area(length, width):
    area=length*width
    return area

result=calculate_area(5,6)
print(result) """

#Write a function max_of_three(a, b, c) that returns the largest of three numbers.
""" def max_of_three(a, b, c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
    
result=max_of_three(90,8,4)
print(result) """

#Write a function count_vowels(word) that counts and returns how many vowels are in the given string.
""" def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Example
result = count_vowels("Sukanya")
print("Number of vowels:", result) """


