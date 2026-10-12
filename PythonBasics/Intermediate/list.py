#INITIALIZATION
myList = ["banana", "cherry", "apple"]
print(myList)

# EMPTY LIST CREATION
myList2 = list()

#DIFFERENT DATA TYPES AND DUPLICATES
mixedList = [5, True, "apple", "apple"]
print(mixedList)

#ACCESSING ELEMENTS BY INDEX
item = myList[0]      
lastItem = myList[-1] 
print(item, lastItem)

#ITERATING AND MEMBERSHIP CHECK
for fruit in myList:
    print(fruit)

if "banana" in myList:
    print("Yes, banana is in the list")

# LIST METHODS
print("Length:", len(myList))
myList.append("lemon")             
myList.insert(1, "blueberry")  
poppedItem = myList.pop()         
myList.remove("cherry")            
# myList.clear()                   

#SORTING
numbers = [4, 2, 3, 1, -1, -5, 10]
numbers.sort()                      
newSorted = sorted(numbers)        

#REPETITION AND CONCATENATION
zeros = [0] * 5
combined = zeros + [1, 2, 3]

#SLICING: [START:STOP:STEP]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub = nums[1:5]                     
stepSlice = nums[::2]                
reversedNums = nums[::-1]          

# COPYING (PREVENT MODIFYING ORIGINAL REFERENCE)
original = ["banana", "cherry", "apple"]
copyList = original.copy()         

#  LIST COMPREHENSION
squared = [x * x for x in [1, 2, 3, 4, 5, 6]]
print("Squared numbers:", squared)