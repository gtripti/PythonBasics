def name_function() :
    '''
    DOCSTRING:Information about the function
    Input : no
    Output: Hello
    '''
    print('Hello')
name_function()

# Add argument
def say_hello(name):
    print('Hello ' + name)
say_hello('Tripti') 

# default parameter
def say_hello_default(name = 'Name'):
    print('Hello ' + name)
say_hello_default()
say_hello_default('Tripti')

# Function with return keyword
def say_hello_return(name = 'Name') :
    return 'Hello ' + name
result = say_hello_return()
result
result = say_hello_return('Tripti')
result

def add_numbers(n1,n2):
    return n1+n2
sum = add_numbers(2,4)
sum

# Find out if the word 'dog' is in the string
def dog_check(myString):
    return 'dog' in myString.lower()
dog_check('Dog ran away')

# Pig latin 
# if word starts with a vowel then add 'ay' at the end
# if it does not start with vowel then put the first letter at the end and add 'ay' at the end
# Example : word -- > ordway ; apple --> appleay
def pig_latin(word):
    first_letter = word[0] 
    # Check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else :
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

pig_latin('word')

# Return lesser of 2 numbers if both even else return greater of the number if any one is odd
def lesser_of_two (n1,n2):
    if n1%2 == 0:
        if n2%2 == 0 :
            result = min(n1,n2)
        else:
            result = max(n1,n2)
    else :
        result = max(n1,n2)
    return result
lesser_of_two(2,4)
lesser_of_two(7,5)

# pass 2 strings if both start with same letter return true else return false
def animal_crackers(text):
    wordList = text.lower().split()
    print(wordList)
    # first = wordList[0]
    # second = wordList[1]
    return wordList[0][0] == wordList[1][0]

# Given 2 int if sum of them or any one int is 20 then return true else false
def makes_twenty(n1,n2):
    return (n1+n2) == 20 or n1 == 20 or n2 == 20
makes_twenty(12,8)
makes_twenty(20,10)
makes_twenty(2,4)

# Write a function that capitalizes the first and forth letter of the word
def old_macdonald(name):
    first_letter= name[0]
    inbetween = name[1:3]
    forth_letter = name[3]
    rest_letter = name[4:]
    return first_letter.upper() + inbetween + forth_letter.upper() + rest_letter
old_macdonald('tripti')

# Or better method
def better_old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    return first_half.capitalize() + second_half.capitalize()
better_old_macdonald('tripti')

# return the reversed sentence
def reverse_sentence(text):
    word_list = text.split()
    reverse_wordList = word_list[::-1]
    return ' '.join(reverse_wordList)
reverse_sentence('I am Home')

# return True if difference of n from 100 or 200 is less than or equal to 10
def abs_diff(n):
    return (abs(100-n) <= 10) or (abs(200 - n) <= 10)
abs_diff(150)

# Find 2 3's in a list
def has_33(num):
    for i in range(0,len(num) - 1):
        # if num[i] == 3 and num[i+1] == 3:
        if num[i:i+2] == [3,3]:
            return True
    return False
has_33([1,3,3])
has_33([3,1,3])

# Print every letter of string thrice
def letter_thrice(myString):
    result = ''
    for char in myString:
        result += char**3
    return result
letter_thrice('Hello')

# BLACK JACK -- Input: 3 integer numbers; output -- if sum <= 21 return sum
#if n == 11 then sum minus 10 else sum > 21 print bust
def black_jack(n1,n2,n3):
    if sum([n1,n2,n3]) <= 21 :
        return sum([n1,n2,n3])
    elif 11 in [n1,n2,n3] and sum([n1,n2,n3]) <= 31 :
        return sum([n1,n2,n3]) - 10
    else:
        return 'BUST'
black_jack(5,6,7)
black_jack(9,9,9)
black_jack(9,9,11)

# SUMMER OF 69 -- return sum of list ignoring the numbers from 6 to 9
def summer_of_69(arr):
    total = 0
    add = True
    for num in arr :
        while add :
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add :
            if num != 9 :
                break
            else:
                add = True
                break
    return total
summer_of_69([1,3,5])
summer_of_69([4,5,6,7,8,9])
summer_of_69([2,1,6,9,11])

# SPT GAME Input: List of integers and returns true if contains 007 in order

def spy_game(myList):
    code = [0,0,7,'x']
    for i in myList:
        if i == code[0] :
            code.pop(0)
    return len(code) == 1
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,5,0,4,2,0])

# COUNT PRIME -- return the number of prime numbers including th enumber itself
def count_prime(number):
    # Check
    if num < 2 :
        return 0
    # Greater than 2
    
    # Store our prime numbers
    primes = [2]
    # counter going up to input num
    x = 3
    
    while x <= number :
        for y in range(3,x,2):
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)


        