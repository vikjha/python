#tuple_data = ('physics', 'chemistry', 1997, 2000)
#tuple_num = (1, 2, 3, 4, 5 )
#tuple_letters = "a", "b", "c", "d"

#dog = ("Canis Familiaris", "dog", "carnivore", 12)

#print dog[2]

#for data in dog:
#     print data

#dog = dog + ("domestic",)

#dog = dog[:3] + ("man's best friend",) + dog[4:]

#print dog
import math

def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)

print get_circle_area(9)

import language
print language.translate(dog)
# output would look something like: ("dog", "chien", "perro")
