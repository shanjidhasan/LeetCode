class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                top = stack.pop()
                if abs(top) == abs(asteroid):
                    break
                elif abs(top) > abs(asteroid):
                    stack.append(top)
                    break
            else:
                stack.append(asteroid)

        return stack
