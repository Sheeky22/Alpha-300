# SHUFFLE THE ARRAY

nums = [2,5,1,3,4,7]
n = 3

def shuffle(nums,n):
    for i in range(len(nums)):
            ans = [0] * (2 * n)
            for i in range(2 * n):
                if i % 2 == 0:
                    ans[i] = nums[i // 2]
                else:
                    ans[i] = nums[n + i // 2]
            return ans

print(shuffle(nums,n))