# from itertools import product

# a=[1,3]
# b=[2,4]
# print(list(product(a,b)))

# from itertools import permutations,combinations,combinations_with_replacement

# Output all possible orderings of input

# a=[1,2,3,4]
# print(list(permutations(a)))

# print(list(combinations(a,2)))
# print(list(combinations_with_replacement(a,2)))

# from itertools import accumulate
# import operator
# a=[1,2,3,4]

# print(a)
# print(list(accumulate(a)))
# print(list(accumulate(a, func=operator.mul)))
# b=[1,2,4,3,5,6,2]
# print(list(accumulate(b,func=max)))

# from itertools import groupby

# a=[1,3,2,4]
# def evenodd(x):
#     return x%2==0

# grpObj = groupby(a,key=lambda x:x%2==0)
# for key,value in grpObj:
#     print(key,list(value))

# from itertools import count,cycle,repeat

# for i in count(10): #count from 10 till infinite
#     print(i)
#     if i==19:
#         break

# a=[1,2,3]
# for j in cycle(a):
#     print(j)

# for z in repeat(1,7):
#     print(z)



