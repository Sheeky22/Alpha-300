class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandy=0
        result=[]
        for i in candies:
            if maxCandy<i:
                maxCandy=i
        for i in candies:
            if i==maxCandy:
                result.append(True)
            elif i+extraCandies>=maxCandy:
                result.append(True)
            else:
                result.append(False)
        return result