# Variables

name = "Bharathi"
age = 37
salary = 500000.50
is_active = True

# Strings
print(name.upper())
print(name.lower())
print(len(name))

# Lists
stores = ["Store1", "Store2", "Store3"]
print(stores[0])

stores.append("Store4")

for store in stores:
    print(store)

# Dictionary

employee = {
    "name": "Bharathi Raja",
    "age": 37,
    "city": "Sattur"
}

print(employee["city"])

# Find even numbers
# ---------------------
numbers = [1, 2, 4, 5, 10, 12, 15]
print("Even Numbers are:")
for number in numbers:
    if number%2 == 0:
        print(number)

# Reverse a string
# --------------------
def reverse_string(name):
    reversed_name = ""
    for letter in name:
        reversed_name = letter + reversed_name
    return reversed_name

print(reverse_string("Bharathi"))

# write a function that returns only the vowels from a string.
def find_vowels(name):
    vowels_letters = ""
    for letter in name.lower():
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowels_letters = vowels_letters + letter
    print(vowels_letters)

print(find_vowels("BharathiyoUtot"))