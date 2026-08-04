from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.hashmap[key]) - 1

        res = ""
        while l <= r:
            m = (l + r) // 2
            if self.hashmap[key][m][0] <= timestamp:
                res = self.hashmap[key][m][1]
                l = m + 1
            else:
                r = m - 1

        return res

