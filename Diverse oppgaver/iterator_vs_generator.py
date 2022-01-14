# This is an iterator
class Range:
    def __init__(self, count):
        self.i = 0
        self.count = count

    # __iter__ and __next__ needs to be overrided.
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.count:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


# This is an iterator
def myrange(count):
    i = 0
    while i < count:
        yield i
        i += 1


r1 = Range(5)
r2 = myrange(5)


for item in r1:
    print(item)

print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))


# for item in r2:
#     print(item)

# print(next(r2))
# print(next(r2))
# print(next(r2))
# print(next(r2))
# print(next(r2))
# print(next(r2))
