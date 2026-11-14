# Day 1 –  Problem Solving 

# Problem: First Non-Repeating Character
# Given a string, find the first character that appears only once in the entire string.
# Example 1
# Input:
# "programming"
# Output:
# 'p'

# Approach 1: Brute Force 
# It is the most straightforward approach.
# For every character, count how many times it appears in the entire string.
# We can use Python's .count() method.

def first_non_repeat(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None
result = first_non_repeat("Programming")
print(result)

# Approach 2: Using a Dictionary
# Instead of repeatedly counting characters, we can count all characters once
# Then, we can store the frequencies in a dictionary.

def first_non_repeat(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char] = 1
    
    for char in s:
        if frequency[char] == 1:
            return char
    return None

result = first_non_repeat("Programming")
print(result)
 
# Approach 3: Using Counter
# Python provides a specialized tool for frequency counting:collections.Counter
# This makes code shorter

from collections import Counter

def first_non_repeat(s):
    frequency = Counter(s)
    for char in s:
        if frequency[char] == 1:
            return char
    return None
result = first_non_repeat("Programming")
print(result)
