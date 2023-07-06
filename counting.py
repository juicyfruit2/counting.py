# counting the number of times a character occurs in a string.

# string asks the user to enter a word 
string = input(" Enter any word: \n" )

# empty dictionary is used to store the number of occurances 
dict = {}

# for loop is used to loop through the string using set, count & len fuction 
for i in set(string):
    x = string.count(i,0,len(string))
    dict[i] = x

print(dict)

# used this website to look at how to go about this task 
# https://stackoverflow.com/questions/40985203/counting-letter-frequency-in-a-string-python/40985309#40985309