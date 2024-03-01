class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        radiant = deque()
        dire = deque()

        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            radiant_senator = radiant.popleft()
            dire_senator = dire.popleft()

            if radiant_senator < dire_senator:
                radiant.append(radiant_senator + len(senate))
            else:
                dire.append(dire_senator + len(senate))

        return "Radiant" if radiant else "Dire"
