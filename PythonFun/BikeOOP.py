class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def display(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print 'riding'
        self.miles + 10
        return self
    def reverse(self):
        print 'reverse'

        self.miles = abs(self.miles -5)

        return self

a = Bike("$23343", "99 mph", 12322)

b  = Bike("$66677", "150 mph", 1223)

c = Bike("$73343", "1000 mph", 1232)

a.ride().ride().ride().reverse().display()
print ""
b.ride().ride().reverse().reverse().display()
print ""
c.reverse().reverse().display()
