# dictionaries: Key-Value pairs, unordered , mutable

# initialization
my_dict = {"name": "Sree", "age": 20, "city": "Singapore"}
print(my_dict)

# alternative creation using dict() constructor
my_dict_2 = dict(name="Avi", age=25, city="US")
print(my_dict_2)

# 2. Accessing values
print("Name:", my_dict["name"])
# my_dict["lastname"]  

# adding, modifying, and deleting items
my_dict["email"] = "max@xyz.com"   # Adds new key-value pair
my_dict["email"] = "coolmax@xyz.com" # Overwrites existing key
print(my_dict)

del my_dict["name"]                
popped_age = my_dict.pop("age")   
popped_pair = my_dict.popitem()    
print("After deletions:", my_dict)

# 4. Checking key existence
test_dict = {"name": "Sreekesh", "age": 18, "city": "Delhi"}

# Method A: in keyword
if "name" in test_dict:
    print("Found key 'name':", test_dict["name"])

# Method B: try-except block
try:
    print(test_dict["lastname"])
except KeyError:
    print("KeyError: 'lastname' not found")

# 5. Iterating through a dictionary
for key in test_dict:              
    print("Key:", key)

for key in test_dict.keys():       
    print("Key explicitly:", key)

for value in test_dict.values():   
    print("Value:", value)

for key, value in test_dict.items(): 
    print(f"{key}: {value}")

# Copying dictionaries 
dict_org = {"name": "Max", "age": 28, "email": "max@xyz.com"}
dict_copy = dict_org.copy()        
dict_copy["email"] = "changed@xyz.com"
print("Original email:", dict_org["email"])
print("Copied email:", dict_copy["email"])

# merging dictionaries with update()
dict_a = {"name": "Mary", "age": 27, "email": "mary@xyz.com"}
dict_b = {"name": "Mary", "age": 28, "city": "Boston"}
dict_a.update(dict_b) 
print("Merged dict:", dict_a)

#valid key types (must be immutable and hashable)
# integers as keys:
int_dict = {3: 9, 6: 36, 9: 81}
print("Value at key 3:", int_dict[3]) 

# tuples as keys (valid because tuples are immutable):
coord_dict = {(8, 7): 15}
print("Tuple key lookup:", coord_dict[(8, 7)])

# lists as keys are NOT allowed because lists are mutable:
# invalid_dict = {[8, 7]: 15}  