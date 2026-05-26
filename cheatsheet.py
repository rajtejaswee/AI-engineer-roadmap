# ----- Variables -------#

name = "Raj"        # string
age = 25            # int 
pi = 3.14           # float 
is_active = True    # boolean
nothing = None      # null/undefined


# -------- Collections ----------#

my_array = [1,2,3,4] #mutable, ordered
my_tuple = (1,2,3) #immutable list 
my_dict = {"name" : "Raj", "age": 25} # objects, key are hasable
my_set = {1,2,3,4}


# ---------- String Formatting-----------#
greetings = f"Hello, {name}, you are {age} years old"


# ---------- Conditonals -----------#
if age >= 18:
    print("adult")
elif age >= 13:
    print("teen")
else:
    print("kid")

# --------- Loops ------------#

for item in my_array:
    print(item)  #printing just the items inside it

for i, item in enumerate(my_array):
    print(i, item) # printing the index as well as items

for key, value in my_dict.items():
    print(key, value) # iterating in the dictionary


# ----------- Functions --------#
def add(a,b):
    return a + b

# Default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"


# ------ List comprehensions (The Python idioms) ----------#
squares = [x * x for x in range(10)]
even = [x for x in range(20) if x % 2 == 0]

# -------- For checking Nothing -----------#
result = None
if result is None: # use `is`, not `==`, for None
    print("Nothing is here")

# ---------- Extra Notes ------------#
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # True  — same values
print(a is b)   # False — different objects in memory

x = None
print(x is None)   # ✅ correct
print(x == None)   # works, but linters will yell