*Primary: RUNNING SUM OF 1D ARRAY*
Iterate thru the array. Add each element to the previous sum and update the element with the array. 

TIME - O(n)
SPACE - O(1)

*Variant 1: LEFT AND RIGHT SUM DIFFERENCES*
In first iteration over array, we find the sum of all the elements on the left of the position. In second traversal,we find the sum of all elements on the right and store the difference in the array. 

TIME - O(n)
SPACE - O(1)

*Variant 2: RICHEST CUSTOMER WEALTH*
Sum all accounts for the current customer. Compare current customer's wealth with the tracked maximum. Keep the higher value between current maximum and new wealth. Final maximum represents the richest customer's wealth

TIME - O(m*n)
SPACE - O(1)

*Variant 3: SHUFFLE THE ARRAY*
Loop through the array. If even, the element should be in nums[i/2]. If odd, jump t0 second half using formula [n+i/2]

TIME - O(n)
SPACE - O(n)

*Variant 4: BUILD ARRAY 3*
Core formula used: nums[i] = original value + 1000 × new value

TIME - O(n)
SPACE - O(1)
