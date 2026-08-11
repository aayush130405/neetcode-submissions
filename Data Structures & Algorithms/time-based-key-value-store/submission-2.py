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

        left = 0
        right = len(self.store[key]) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.store[key][mid][0] <= timestamp:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        if ans == -1:
            return ""
        else:
            return self.store[key][ans][1] 
