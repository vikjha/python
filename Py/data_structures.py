#lists are mutable
# list.append() --> add a single peice of data
#example list = [1,2,3]
#list.append[4]
#>>>[1,2,3,4]
#list.extend for multiple pieces of data
#list.extend([5,6,7])
#>>> [1,2,3,4,5,6,7]
#splits break strings on white spaces or whats in the method parantheses
#'hello there students'.split ()
#>>>['hello', 'there', 'students']
#split() Parameters
#The split() method takes maximum of 2 parameters:

#If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
#maxsplit (optional) - The maxsplit defines the maximum number of splits.
#The default value of maxsplit is -1, meaning, no limit on the number of splits.
#available = "banana split;hot fudge;cherry;malted;black and white"

#sundaes = available.split(';')

#menu = 'Our available flavors are: {}.'.format(','.join(sundaes))
#display_menu = menu
#def add(a, b):

#    try:
#        f1= float(a)
#        f2= float(b)
#    except ValueError:
#        return none
#    else:
#        return (f1 + f2)
#
#The issue is with the loop in your else block. It is stating that for each letter in item, print that letter. For the challenge you just want to print the the entire word if it does not start with 'a'

#def loopy(items):
 # for item in items:
#    if item[0] == "a":
#      continue
#    else:
#        print(item)
#
This challenge is similar to an earlier one. Remember, though, I want you to practice! You'll probably want to use try and except on this one. You might have to not use the else block, though.
Write a function named squared that takes a single argument.
If the argument can be converted into an integer, convert it and return the square of the number (num ** 2 or num * num).
If the argument cannot be turned into an integer (maybe it's a string of non-numbers?), return the argument multiplied by its length. Look in the file for examples.

# EXAMPLES
def squared(num):
    try:
        num = int(num)
        return num * num
    except:
        return num * len(num)

def squared(num):
  try:
    return (int(num) ** 2)
  except ValueError:
    return (str(num) * len(num))

You've seen how random.choice() works. It gets a random member from an iterable (like a list or a string).
I want you to try and reproduce it yourself.
First, import the random library.
Then create a function named random_item that takes a single argument, an iterable. Then use random.randint() to get a random number between 0 and the length of the iterable, minus one. Return the iterable member that's at your random number's index.
Check the file for an example.

Using iterable[ ... ] with square brackets is used to lookup an item in the iterable by an index number.

Using iterable( ... ) with parens would be used if iterable was called as a function. It's not a function so this doesn't work in this case.
# EXAMPLE
import random
# random_item("Treehouse")
def random_item(iterable):
    return random.randint(0, len(iterable) -1)

# The randomly selected number is 4.
# The return value would be "h"


I need you to create a new function for me.
This one will be named sillycase and it'll take a single string as an argument.
sillycase should return the same string but the first half should be lowercased and the second half should be uppercased.
For example, with the string "Treehouse", sillycase would return "treeHOUSE".
Don't worry about rounding your halves, but remember that indexes should be integers. You'll want to use the int() function or integer division, //.






def sillycase(string):
    mid = int(len(string)/2)

    result = (string[:mid]).lower() + (string[mid:]).upper()

    return result


second way to make a dictionary

dict([['key', 'value']])

dictionary = {'key': 'value', 'key1':'value1', ect}
