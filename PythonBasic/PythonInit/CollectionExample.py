# Python Collection	                      Java Equivalent
# Lists 	                              ArrayList
# Tuples 	                              (Immutable ArrayList)
# Sets                                    HashSet
# Dictionaries                      	  HashMap
# Deque
# Counter (Specialized Dictionary for Counting)

############################################### Lists ######################################################################
from collections import Counter

# Lists (Ordered, Mutable)
# Think of grocery lists. You can add/remove items and access them by position (index).
shopping_list = ["bread", "milk", "eggs"]
############################################### Tuples ######################################################################
# Tuples (Ordered, Immutable)
# Imagine coordinates where order matters but can't be modified.
point = (3, 4) # (x-coordinate, y-coordinate)

fruits = ("apple", "banana", "cherry")
first_fruit = fruits[0] # Accessing first element Elements
# fruits[0] = "mango" #You cannot modify elements after creating a tuple.

empty_tuple = () # Empty tuples are created using empty parentheses.

# Advantages of Tuples:
    # Immutability: Ensures data integrity as you can't accidentally modify the content.
    # Efficiency: Tuples are often more memory-efficient than lists due to their immutability.
    # Hashing: Since tuples are immutable, their content can be hashed (used for comparisons), making them useful for dictionary keys.

# Good use-cases of Using Tuples:
# Storing fixed data:
    # Example: coordinates = (10, 20) (x and y coordinates that shouldn't change)
# Returning multiple values from functions in contrast to Java:
def get_name_and_age():
    return ("Alice", 30)
name, age = get_name_and_age()  # Unpacking the returned tuple
print(f"Name: {name}, Age: {age}")

# Using as dictionary keys:
    # Example: student = {"name": "Bob", "grades": (85, 90, 78)} (since grades shouldn't be modified)
############################################### Sets ######################################################################

# Sets (Unordered, Unique Elements)
# Picture a collection of unique badges. Order doesn't matter, and duplicates are ignored.
# unique_chars = {'a', 'b', 'c', 'b'} # (only 'a', 'b', 'c' remain)

############################################### Dictionaries ###############################################################
# Dictionaries (Unordered, Key-Value Pairs)
phonebook = {"Alice": "123-4567", "Bob": "890-1234"}

############################################### Deque #######################################################################
# Deque (Double-Ended Queue)
# Think of a fast-food line where you can add people at the front or back efficiently.
# tasks = deque([wash_dishes, do_laundry]) #add new tasks at either end

############################################### Counter ######################################################################
# Counter (Specialized Dictionary for Counting)
# Imagine tracking how many times you see different colored cars.
color_counts = Counter(['red', 'blue', 'red', 'green'])
###############################################################################################################################

