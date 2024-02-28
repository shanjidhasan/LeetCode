class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1 and flowerbed[0]==0:
            return True
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n-=1
        prev = flowerbed[0]
        for i in range(1, len(flowerbed)):
            if i==len(flowerbed)-1 or flowerbed[i+1]==0 or i==1:
                f=True
            else:
                f=False
            if prev == 0 and flowerbed[i] == 0 and f:
                n-=1
                flowerbed[i] = 1
            prev = flowerbed[i]
        if n<=0:
            return True
        else:
            return False
