def add(a,b):
  x = a + b
  return x
# the return value gets assigned to the "result" variable
result = add(3,5)
print result # this should print 8


# we've named the function 'add' and we give it two parameters(inputs to the function)
def add(a,b):
  x = a + b
  return x  # we return something (more on this later)

print add(3,5) #prints 8

def add(a, b):
  x = a + b
  return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

print sum3
print sum1
print sum2 
