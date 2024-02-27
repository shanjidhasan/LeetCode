class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        ans = [-1]*n
        i = 0
        left = []
        right = []
        for row in intervals:
            left.append([row[0],i])
            right.append([row[1],i])
            i+=1
        left = sorted(left, key=lambda x:x[0])
        right = sorted(right, key=lambda x:x[0])
        ptr = 0
        p = 0
        for i in range(n):
            for j in range(ptr,n):
                if left[j][0]>=right[i][0]:
                    p = j
                    ans[right[i][1]]=left[j][1]
                    break
                ptr=p
        return ans        
