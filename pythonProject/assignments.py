import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
print(np.mean(numbers))

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print(pd.__version__)
print(np.__version__)

import random
import string


import random
from random import choice

answers = ['Nah', 'Yes', 'Correct', 'Keep being Delusional', 'God said it, so shall it be', 'NO', 'False', 'Absolutely',]
#these are the answeres the random 8 ball would give

def magicball():
    rando = ['Nah', 'Yes', 'Correct', 'Keep being Delusional', 'God said it, so shall it be', 'NO', 'False', 'Absolutely',]
    print(random.choice(rando))

magicball()

'''for number in range(1, 99, 2):
    print(number)   
    num = int((input('Pick a random number: ')))
    if num not in number:
        print('Number not on the list ')
    else:
        print('stop')'''


'''Create a function that'll generate a random 8 digit password with numbers, 
letters and special characters using the random module, do your research'''



'''assignment 1
create a list named friends that contains 5 names.
Use append and insert to add 5 more names to the list.
use a for loop to send a message to every name on the list.'''

# We can use the extend method or the plus sign method to add multiple names to a list
# Method 1: Using extend with a list of multiple names
#     friends.extend(["Chisom", "Samson", "Christabel"])
#
#     # Method 2: Using the plus sign
#     friends = friends + ["Chisom", "Samson", "Christabel"]

friends = ['Joshua', 'Leo', 'Emmanuel', 'Favour', 'Augusta']
updated = input('respond "yes" to see the appended lists. ')

friends.insert(0,'Williams')
friends.append('Kelvin, Drake, Tiana')
friends.insert(2,'Abigail,' ' Christopher')
friends.insert(5,'Clement,' ' Ayo')
friends.append('Simon, Kimberly' )
print(friends)


for names in friends:
    print(names)
    greetings = input(f'It was nice meeting you {names}')


'''assignment 2
create a list containing odd numbers from 1 to 99
using a combination of for loops and conditional statements,
create a loop that will check if a number that was typed by the user is in the odd number list'''

numbers = range( 1,100,2)
for num in numbers:
    choice = input('Type a number: ')
    if choice in numbers:
        print('you picked right')
    else:
        print('not included')


''' numbers = range(1, 100, 2)
  for num in numbers:
    print(num)
    choice = input("Type 'quit' to stop, or press Enter to continue: ")

    if choice.lower() == "quit":
      print("Loop stopped early!")
      break  # Ends the loop immediately, ignoring the rest of the numbers '''


''' assignment 3
create 2 empty lists named Names and Usernames respectively
create a function to add new entries into the Names and Usernames lists
create a function that will check an index that a user inputs exists in the Names list 
and then brings out the Username in the equivalent Usernames index. The output should look like this:
    Name: Jane J.
    Username: JanetDB'''

Names = []
Usernames = []


def humans(new):
    Names.append(new)
    Usernames.append()

print(humans)

def greeting():
   for people in Names:
       print('')



''' assignment 4
in a new file, create a function called 'create_account' that collects first_name, last_name, username, password, opening_balance. 
Let the opening_balance be = 0 by default. Let the create_account function pass all the information it is collecting into a dictionary.
In the same file, create a function named 'calculate_interest' that will take a dictionary as input
(preferably one that you created with the create_account function) 
and use the opening_balance value to calculate the simple interest over a period of a year and print the result.
hint: principal = account['opening_balance']
      ***formula***
      print(result)
create another new file and call the two functions seperately'''
 #name of file is interest