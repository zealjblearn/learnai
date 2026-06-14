# Normal Function

def get_numbers():
    return [1, 2, 3, 4, 5]

print(get_numbers()) # [1, 2, 3, 4, 5]

numbers = get_numbers()

for num in numbers:
    print(num)

'''In Python, 

Generators are a way to create iterators without storing all values in memory at once. 

They generate values lazily (on demand), making them efficient for large datasets.

The yield keyword is used to create a generator.'''

def get_numbers():
    yield 1
    yield 2
    yield 3

numbers = get_numbers()

for num in numbers:
    print(num)

squares = (x * x for x in range(5))

print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4

squares = (x * x for x in range(5))
print(type(squares))

print(next(squares))