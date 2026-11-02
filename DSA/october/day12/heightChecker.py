class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        countSort=[0]*101
        expected=[]
        for i in heights:
            countSort[i]+=1
        for i in range(101):
            for j in range(countSort[i]):
                expected.append(i)
        count=0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count+=1
        return count