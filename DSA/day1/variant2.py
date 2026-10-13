#  3 SUM

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

nums = [-1,0,1,2,-1,-4]

def threeSum(arr):
    sortedArr=merge_sort(arr)
    res=[]

    for i, a in enumerate(sortedArr):
        if a > 0:
            break

        if i > 0 and a == sortedArr[i - 1]:
            continue

        l, r = i + 1, len(sortedArr) - 1
        while l < r:
            threeSum = a + sortedArr[l] + sortedArr[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, sortedArr[l], sortedArr[r]])
                l += 1
                r -= 1
                while sortedArr[l] == sortedArr[l - 1] and l < r:
                    l += 1

    return res

print(threeSum(nums))

