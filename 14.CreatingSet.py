#Creating a Set 

# a. Using Curly Brackets
print("First Way")
set1 = {1, 2, 3, 4}
print(set1)


# b. Using the set() function 
print("\n\nSecond Way")

# Creating a Set
set1 = set()
print(set1)

set1 = set("AbcdForAbcd")
print(set1)

# Creating a Set with the use of a List
set1 = set(["Abcd", "For", "Abcd"])
print(set1)

# Creating a Set with the use of a tuple
tup = ("Abcd", "for", "Abcd")
print(set(tup))

# Creating a Set with the use of a dictionary
d = {"Abcd": 1, "for": 2, "Abcd": 3}
print(set(d))
