'''
Given a string, count the number of vowels present 
in the given string using Sets. You can use sets to
 count the number of vowels in a given string in Python.
 Sets are useful to efficiently check for counting the 
 unique occurrences of vowels.'''
l="hello thsi is python"
v="aeiouAEIOU"
count=0
for i in l:
    if i in v:
        count+=1
print("total vowels are=>",count)