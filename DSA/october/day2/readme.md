*Primary:*
Hashmap(dict) have access time constant. We iterate over the array. If element is seen in hashmap, duplicate found. Else, element is added to the hashmap. 

TIME - O(n)
SPACE - O(n)

*Variant 1: CONTAINS DUPLICATE II*
Used sliding window of size k. Instead of checking every contiguous triplet, move the window one step at a time, remove the element that is out of the window and add the new element. Check the seen set. 

TIME - O(n)
SPACE - O(k)

*Variant 2: Duplicate Zeros*
First calculate the number of zeros. Have one pointer at end of array and second pointer at length of array plus number of zeros. Exchange jth element with ith element if ith element is 0 or j is less then len(arr).

TIME - O(n)
SPACE - O(1)

*Variant 3: FIND ALL DUPLICATES IN AN ARRAY*
As we can't use hashset, for every number, take the number as index, and make that element negative. For every element, if that number is negative, then append it to result.

TIME - O(n)
SPACE - O(1)

*Variant 4:*
Same logic as above.

TIME - O(n)
SPACE - O(1)