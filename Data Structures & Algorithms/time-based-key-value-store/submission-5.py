class TimeMap:

    def __init__(self):
        self.store = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        ans = -1

        l = 0
        r = len(self.store[key]) - 1

        while l <= r:
            m = (l + r) // 2

            if self.store[key][m][0] <= timestamp:
                ans = m 
                l = m + 1
            else:
                r = m - 1
        
        if ans == -1:
            return ""
        else:
            return self.store[key][ans][1]
            
