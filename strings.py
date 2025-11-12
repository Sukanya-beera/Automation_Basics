#Write a function count_vowels(string) that returns the number of vowels in a string.

""" def count_vowels(name):
    vowels='aeiouAEIOU'
    count=0
    for char in name:
        if char in vowels:
            count+=1
    return count

print(count_vowels('iiIAua')) """

#Write a function reverse_string(text) that returns the string in reverse order.

""" def reverse_string(text):
    reverse=text[::-1]
    return reverse
print(reverse_string('samsung')) """

""" def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text   # add each character to the front
    return reversed_text

# Example
word = "Python"
print(reverse_string(word)) """

#Write a function is_palindrome(word) that checks if a word reads the same backward.

""" def is_palindrome(word):
    reverse=word[::-1]
    if word==reverse:
        return True
    else:
        return False

print(is_palindrome('pip')) """

""" def is_palindrome(word):
    reverse=''
    for char in word:
        reverse=char+reverse
    if reverse==word:
        return True
    else:
        return False
print(is_palindrome('pop')) """

#Write a function find_even_numbers(numbers) that returns a list of only even numbers

""" def find_even_numbers(numbers):
    dupli=[]
    for i in numbers:
        if i%2==0:
            dupli.append(i)
    return dupli

print(find_even_numbers([1,2,3,4,5,6,7,8,9])) """

#Write a function multiply_all(*args) that multiplies any number of arguments together.
""" def multiply_all(*args):
    result=1
    for num in args:
        result*=num
    return result
print(multiply_all(2,3,4,5))

or

def multiply_all(*args):
    return math.prod(args)  //inbuild method

 """
#Write a function student_details(name, age, city="Unknown") that prints all details (use default argument).
""" def student_details(name, age, city="Hyd"):
    print(f'student-details: {name},{age},{city}')

student_details('soon',35,'denmark')
student_details('sony',30,) """

#Write a function calculate_grade(score) that returns A/B/C/D/F depending on the marks.

""" def calculate_grade(score):

    #34 F,35-45 D,46-55 C,56-65-B, 66-100 A 
    if score>65:
        print('A')
    elif score>55:
        print('B')
    elif score>45:
        print('C')
    elif score>35:
        print('D')
    else:
        print('F')

calculate_grade(90)
 """
#Write a function remove_duplicates(lst) that removes duplicates from a list.

""" def remove_duplicates(lst):
    return list(set(lst))

# Example:
numbers = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(numbers))
 """
#Write a function count_words(sentence) that counts how many words are in a string.
""" def count_words(sentence):
    words=sentence.split()
    return len(words)

result=count_words('how are you doing')
print(result) """

#Write a function is_prime(num) that checks if a number is prime or not.
""" def is_prime(num):
    if num < 2:       # handle 0 and 1, not prime
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(9)) """

#Write a program to capitalize every word in a sentence using a string method
""" def capitalize(sentence):
    return sentence.title()

print(capitalize('how are you doing?')) """
    
#Given a list of names, use list methods to add, remove, and sort the elements.
""" lst=['sony','meena','john','win']
lst.append('Raj')
print(lst)
lst.remove('meena')
print(lst)
lst.sort()
print((lst)) """

#Write a function that takes a string and returns it in uppercase.

""" def convert_upper(string):
    return string.upper()
print(convert_upper('samsung')) """


