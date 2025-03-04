# 1. Write a Python program to check if a number is even or odd.
number=int(input("please enter a number to check even/odd :"))

if number%2==0:
    print("even")
else:
    print("odd")
#--------------------------------------------------------------------------------------------------
#2. Write a program to find the sum of digits of a given number. 
# 2. Write a program to find the sum of digits of a given number.
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        digit = number % 10  # Get the last digit
        sum_digits += digit  # Add the digit to the sum
        number = number // 10  # Remove the last digit
    return sum_digits

# Example usage
number = 12345
print("Sum of digits:", sum_of_digits(number))  # Output should be 15
#--------------------------------------------------------------------------------------------------
#3. Implement a function to check if a string is a palindrome. 
def check_palindrome(string):
    if string.lower()==string[::-1].lower():
        print('yes')
    else:
        print('no')
check_palindrome('maam')
#---------------------------------------------------------------------------------------------------
#4. Write a function to find the factorial of a number using recursion.
def factorial(num):
    if num == 0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))
#---------------------------------------------------------------------------------------------------
# 5. Implement a function to find the second largest element in a list.
def second_largest(lst):
    if len(lst) < 2:
        return None  # Not enough elements to find the second largest
    unique_lst = list(set(lst))  # Remove duplicates
    unique_lst.sort()  # Sort the list
    return unique_lst[-2]  # Return the second last element

# Example usage
lst = [10, 20, 4, 45, 99, 99]
print("Second largest element is:", second_largest(lst))
#---------------------------------------------------------------------------------------------------
# 6. Write a program to count the occurrences of each character in a string.
def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Example usage
s = "hello world"
print(count_characters(s))

#7. Write a program to reverse a given list without using the reverse() method.
lst=[1,2,3,4,5]
newlst=lst[::-1] 
print(newlst)
#-----------------------------------------------------------------------------------------------------
# 8. Implement a function to check if a number is a prime number.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(11))  # Output should be True
print(is_prime(4))   # Output should be False

#9. Write a program to merge two sorted lists into a single sorted list. 
# 9. Write a program to merge two sorted lists into a single sorted list.
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    # Merge the two lists while maintaining the sorted order
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append any remaining elements from list1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Append any remaining elements from list2
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print("Merged sorted list:", merge_sorted_lists(list1, list2))

#10. Write a function to find the longest word in a given sentence.

# 10. Write a function to find the longest word in a given sentence.
def find_longest_word(sentence):
    words = sentence.split()  # Split the sentence into words
    longest_word = max(words, key=len)  # Find the word with the maximum length
    return longest_word

# Example usage
sentence = "The quick brown fox jumps over the lazy dog"
print("Longest word:", find_longest_word(sentence))


