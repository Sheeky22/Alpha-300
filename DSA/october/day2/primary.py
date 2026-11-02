#  CONTAINS DUPLICATE

# arr = [1,2,3,3,4,2,6,7]
# arr = [1,2,3,4,2,6,7]
arr = [1,2,3,4,6,7]



def containDuplicate(arr):
    hashmap={}
    for i in range(len(arr)):
        if arr[i] in hashmap:
            return True
        else:
            hashmap[arr[i]]=i
    return False

print(containDuplicate(arr))
        