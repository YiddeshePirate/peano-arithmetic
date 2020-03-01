




class number():

    def __init__(self, name, successor=None):
        self.name = name
        if successor:
            self.successor = successor
            successor.previous = self

    def s(self):
        return self.successor

    def p(self):
        return self.previous

    def __repr__(self):
        return self.name

    @staticmethod
    def add(first, second):
        if second == zero:
            return first
        else:
            try:
                return number.s(number.add(first, number.p(second)))
            except AttributeError:
                return "need more numbers"
    @staticmethod
    def multiply(first, second):
        if second == zero:
            return zero
        else:
            return number.add(first, number.multiply(first, number.p(second)))

    @staticmethod
    def subtract(first, second):
        if first == second:
            return zero
        else:
            return number.s(number.subtract(first, number.s(second)))

seven = number("seven")
six = number("six", seven)
five = number("five", six)
four = number("four", five)
three = number("three", four)
two = number("two", three)
one = number("one", two)
zero = number("zero", one)

def s(num):
    return num.s()

#print(number.add(five, two))
#print(number.multiply(three, two))
#print(number.subtract(six, two))
