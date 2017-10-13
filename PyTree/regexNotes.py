# Documentation
#
# open() docs
# file_object.close() docs
# file_object.read() docs
# Regular Expressions
# New Terms
#
# open() - Opens a file in Python. This won't contain the content of the file, it just points to it in memory.
# .read() - Reads the entire contents of the file object it's called on.
# .close() - Closes the file object it's called on. This clears the file out of Python's memory.
# r'string' - A raw string that makes writing regular expressions easier.
# re.match(pattern, text, flags) - Tries to match a pattern against the beginning of the text.
# re.search(pattern, text, flags) - Tries to match a pattern anywhere in the text. Returns the first match.


#import re # import regular expressions
# \w - matches an Unicode word character. That's any letter, uppercase or lowercase, numbers, and the underscore character. In "new-releases-204", \w would match each of the letters in "new" and "releases" and the numbers 2, 0, and 4. It wouldn't match the hyphens.
# \W - is the opposite to \w and matches anything that isn't an Unicode word character. In "new-releases-204", \W would only match the hyphens.
# \s - matches whitespace, so spaces, tabs, newlines, etc.
# \S - matches everything that isn't whitespace.
# \d - is how we match any number from 0 to 9
# \D - matches anything that isn't a number.
# \b - matches word boundaries. What's a word boundary? It's the edges of word, defined by white space or the edges of the string.
# \B - matches anything that isn't the edges of a word.
# # Two other escape characters that we didn't cover in the video are \A and \Z. These match the beginning and the end of the string, respectively. As we'll learn later, though, ^ and $ are more commonly used and usually what you actually want.
# \w{3} - matches any three word characters in a row.
# \w{,3} - matches 0, 1, 2, or 3 word characters in a row.
# \w{3,} - matches 3 or more word characters in a row. There's no upper limit.
# \w{3, 5} - matches 3, 4, or 5 word characters in a row.
# \w? - matches 0 or 1 word characters.
# \w* - matches 0 or more word characters. Since there is no upper limit, this is, effectively, infinite word characters.
# \w+ - matches 1 or more word characters. Like *, it has no upper limit, but it has to occur at least once.
# re.findall(pattern, text, flags) - Finds all non-overlapping occurrences of the pattern in the text.

# Create a function named find_words that takes a count and a string. Return a list of all of the words in the string that are count word characters long or longer.

import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

Create a function named find_words that takes a count and a string. Return a list of all of the words in the string that are count word characters long or longer.

Your regular expression needed two fixes: change /w to \w, and remove space later part of string changing ', }' to ',}'.

The updated line is now:.

    return re.findall(r'\w{'+ str(count) + ',}', string) #<-- cast count as string
An alternate to using the range specifiers "{}", you can multiply the character search \w by count then check for optional additional characters with \w* as shown below:

    return re.findall(r'\w' * count + '\w*', string)
Finally you could also use the string format method:

def find_words(cnt,s):
    return re.findall(r'\w{{{:d},}}'.format(cnt), s)
# [abc] - this is a set of the characters 'a', 'b', and 'c'. It'll match any of those characters, in any order, but only once each.
# [a-z], [A-Z], or [a-zA-Z] - ranges that'll match any/all letters in the English alphabet in lowercase, uppercase, or both upper and lowercases.
# [0-9] - range that'll match any number from 0 to 9. You can change the ends to restrict the set.

#^ means do not search characters after it
#re.IGNORECASE flag -- doesnt care upper/lower case for search


Create a function named find_emails that takes a string. Return a list of all of the email addresses in the string.

def find_emails(string):
    re_string = re.findall(r'[-\w\d+.]+@[-\w\d.]+', string)
    return re_string


# [^abc] - a set that will not match, and, in fact, exclude, the letters 'a', 'b', and 'c'.
# re.IGNORECASE or re.I - flag to make a search case-insensitive. re.match('A', 'apple', re.I) would find the 'a' in 'apple'.
# re.VERBOSE or re.X - flag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.

add multiple flags with the single pipe symbol
ex re.VERBOSE|re.IGNORECASE


Create a variable named good_numbers that is an re.findall() where the pattern matches anything in string except the numbers 5, 6, and 7.

import re

string = '1234567890'

good_numbers = re.findall(r'[^5-7]', string)





import re

string = '1234567890'

good_numbers = re.findall(r'[^5-7]', string)

line = re.search(r'''
    ^(?P<name>[-\w]*, \s[-\w]+)\t # Last and First names
    (?P<email>[-w\d.+]+a[-w\d.]+)\t # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and company
    (?P<twitter>@[\w\d]+)?$ # twitter
''', data, re.X|re.M)


# ([abc]) - creates a group that contains a set for the letters 'a', 'b', and 'c'. This could be later accessed from the Match object as .group(1)
# (?P<name>[abc]) - creates a named group that contains a set for the letters 'a', 'b', and 'c'. This could later be accessed from the Match object as .group('name').
# .groups() - method to show all of the groups on a Match object.
# re.MULTILINE or re.M - flag to make a pattern regard lines in your text as the beginning or end of a string.
# ^ - specifies, in a pattern, the beginning of the string.
# $ - specifies, in a pattern, the end of the string.

Create a variable names that is an re.match() against string. The pattern should provide two groups, one for a last name match and one for a first name match. The name parts are separated by a comma and a space.


import re

string = 'Perotto, Pier Giorgio'

names = re.match(r'^(?P<firstname>[\w]*),\s(?P<lastname>[\w\s\w]*)',string,re.X|re.M)


Create a new variable named contacts that is an re.search() where the pattern catches the email address and phone number from string. Name the email pattern email and the phone number pattern phone. The comma and spaces * should not* be part of the groups.

import re

string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

contacts = re.search(r''' #<-- Wrap in multiline quote. Remove leading caret (^)
    (?P<email>[-\w\d.+]+@[-\w\d.]+)
     ,\s
     (?P<phone>\d{3}-\d{3}-\d{4})''' #<-- Add closing paren. Remove extra backslashes. Remove trailing $
     , string, re.X | re.M) #<-- Add verbose (for multiline quote), and multiline (for muliple lines in string) flags
Great! Now, make a new variable, twitters that is an re.search() where the pattern catches the Twitter handle for a person. Remember to mark it as being at the end of the string. You'll also want to use the re.MULTILINE flag.

twitters=re.search(r'''
  (?P<twitter>@[^t][\w\d]+)''', string, re.X)

#   re.compile(pattern, flags) - method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
# .groupdict() - method to generate a dictionary from a Match object's groups. The keys will be the group names. The values will be the results of the patterns in the group.
# re.finditer() - method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
# .group() - method to access the content of a group. 0 or none is the entire match. 1 through how ever many groups you have will get that group. Or use a group's name to get it if you're using named groups.

# Create a variable named players that is an re.search() or re.match() to capture three groups: last_name, first_name, and score. It should include re.MULTILINE.
import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.match(r'''
                    (?P<last_name>[\w ]*)
                    ,\s
                    (?P<first_name>[\w ]*)
                    :\s
                    (?P<score>[\d]*)'''
                    , string, re.X|re.M)

Wow! OK, now, create a class named Player that has those same three attributes, last_name, first_name, and score. I should be able to set them through __init__.
class Player:
  last_name = ""
  first_name = ""
  score = ""

  def __init__(self, last_name=last_name, first_name=first_name, score=score):
    self.last_name = last_name
    self.first_name = first_name
    self.score = score

    or

# Here is a simplified version that does not set class attributes nor use the class attributes as
# '__init__' defaults. This also passes the challenge:

class Player:
  def __init__(self, last_name, first_name, score):
    self.last_name = last_name
    self.first_name = first_name
    self.score = score

The re.MULTILINE new lines treated as individual strings
