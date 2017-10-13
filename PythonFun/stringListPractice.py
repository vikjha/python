str = "It's thanksgiving day. It's my birthday,too!"
print (str.replace('day','month', 1)) #str.find(x, beg, end(optional))

x = [2,54,-2,7,12,98]
maximum_number = max(x)
minimum_number = min(x)
print maximum_number
print minimum_number

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0] + x[-1]


def split_(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]
a=[]
b=[]
x = [19,2,54,-2,7,12,98,32,10,-3,6]
a, b = split_(x)

print b + a
