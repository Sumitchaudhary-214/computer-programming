'''Given a string. The task is to print all words with even length in the given string.

Examples: 

Input: s = "This is a python language"
Output: This is python language

Input: s = "i am laxmi"
Output: am'''
s="hello this is a python language"
for i in s.split():
    if len(i)%2==0:
        print(i,end=" ")