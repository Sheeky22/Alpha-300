# 4 SUM

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

def fourSum(arr,target):
    sortedArr=merge_sort(arr)
    n = len(arr)
    res = []
    for i in range(n):
        if i > 0 and sortedArr[i] == sortedArr[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and sortedArr[j] == sortedArr[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = sortedArr[i] + sortedArr[j] + sortedArr[left] + sortedArr[right]
                if total == target:
                    res.append([sortedArr[i], sortedArr[j], sortedArr[left], sortedArr[right]])
                    left += 1
                    right -= 1
                    while left < right and sortedArr[left] == sortedArr[left - 1]:
                        left += 1
                    while left < right and sortedArr[right] == sortedArr[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return res

nums = [3,2,3,-3,1,0]
target = 3

print(fourSum(nums,target))