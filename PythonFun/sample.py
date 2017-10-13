
#Lists

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']

fruits_and_vegetables = fruits + vegetables

print fruits_and_vegetables

salad = 3 * vegetables
print salad

print fruits[0]

fruits.append('blueberry')

print fruits

my_list = [1, 'Zen', 'hi']
print len(my_list)
# output
3
#enumerate(sequence) used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
#map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
#min(sequence) returns the lowest value in a sequence.
#sorted(sequence) returns a sorted sequence
#list.extend(list2) adds all values from a second sequence to the end of the original sequence.
#list.pop(index) remove a value at given position. if no parameter is passed, defaults to final value in the list.
#list.index(value) returns the index position in a list for the given parameter.
