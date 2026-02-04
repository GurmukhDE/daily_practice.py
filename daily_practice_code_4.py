#lets find out the even and odd from user provided dataset.

def calculate_even_odd(number):
    unique_values = list(set(number))
    even = []
    odd = []
    for i in unique_values:
        if i %2 ==0:
            even.append(i)
        else:
            odd.append(i)
    return sorted(even), sorted(odd)

num = list(map(int,input('enter the number sep by space').split()))

list_even, list_odd = calculate_even_odd(num)

print('this is the list of ' ,list_even)
print('this is the list of ' ,list_odd)

#------------------------------------------------------------

#Write a function count_vowels(text) that returns the number of vowels in the given string.

def vowel_counter(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count

word = 'Hello'
result = vowel_counter(word)

print(f'the word {word} has {result} vowels')

#lets test our function on other string too

word1 = "my name is gurmukh, and I am enjoying python fuctions"

result1  =vowel_counter(word1)

print(f" the word {word1} has {result1} vowels")

#lets make it more advance and count the string by position and store it in a dictionary

def count_by_posi_in_a_dict(text):
    vowels = "aeiouAEIOU"
    l = [1,3,5,6,8,9,9]
    return vowels

print(type(l))
