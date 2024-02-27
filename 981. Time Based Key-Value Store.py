class TimeMap(object):
    dct = {}
    last = {}
    lastV = {}

    def __init__(self):
        self.dct = {}
        self.last = {}
        self.lastV = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        prev = self.dct.get(key)
        if prev == None:
            self.dct[key] = {timestamp: value}
        else:
            for i in range(self.last[key], timestamp):
                prev[i] = self.lastV[key]
            prev[timestamp] = value
        self.last[key] = timestamp
        self.lastV[key] = value
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        lst = self.dct.get(key)
        if lst == None:
            return ""
        else:
            if lst.get(timestamp) == None:
                if timestamp>=self.last[key]:
                    return self.lastV[key]
                else:
                    return ""
            else:
                return lst.get(timestamp)
                

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
