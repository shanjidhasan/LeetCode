class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        max_altitude = 0

        for altitude_change in gain:
            current_altitude += altitude_change
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude
