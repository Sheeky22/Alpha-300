*Primary: SINGLE NUMBER*
When 2 numbers are opreated with XOR(^), it cancels out. Hence, number that is not cancelled is a Single Number 

TIME - O(n)
SPACE - O(1)

*Variant 1: MISSING NUMBER*
As numbers are in range [0,n], operate both the index and the numbers in the array with XOR. 

TIME - O(n)
SPACE - O(1)

*Variant 2: FIND THE DIFFERENCE*
Convert the character to integers using ord(). Apply XOR operation as done above. Convert the resultant integer to character.

TIME - O(s+t)
SPACE - O(1)

*Variant 3: SINGLE NUMBER 2*
Initiate 2 variables ones & twos to 0. For every iteration, ones=(ones^i)&(~twos) and twos=(twos^i)&(~ones)

TIME - O(n)
SPACE - O(1)

*Variant 4: SINGLE NUMBER 3*
Operate XOR on complete array. Seperate out the rightmost bit. Split the elements into two buckets depending on whether their rightmost bit is 0 or 1. Operate XOR on each bucket seperately. Return values of both buckets.

TIME - O(n)
SPACE - O(1)

*Variant 5: SINGLE ELEMENT IN A SORTED ARRAY*
We use Binary Search. If element of previous index of an odd index is same, then eliminate the left. If element of previous index of an even index is same, eliminate the right half. 

TIME - O(log n)
SPACE - O(1)