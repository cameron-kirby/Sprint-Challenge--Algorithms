'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

'''
Input word being checked as well as declare the substring we are looking for
Base case: if the input is not a string or has a length of 0 or 1, exit the function
Search the left-most character i of the word the letter "t" and i+1 for "h"
    if true add 1 to count
set word to word minus 1 index
call function again until there is only 1 character in word left
'''

def count_th(word):
    substring = "th"
    if len(word) < 2:
        return 0
    elif word[:2] == substring:
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
