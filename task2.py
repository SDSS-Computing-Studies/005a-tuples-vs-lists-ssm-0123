#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
loop = True
forloop = 0
words = []
while loop :
    a = input("Enter a word")
    words.append(a.strip())
    forloop = forloop + 1
    if forloop == 5:
        loop = False

print(words)
