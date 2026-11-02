# FIND THE DIFFERENCE

s = "abcd"
t = "abcde"

def findTheDifference(s,t):
    sum=0
    for i in s + t:
        sum^=ord(i)
    return chr(sum)

print(findTheDifference(s,t,))