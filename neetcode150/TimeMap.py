from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list) 
        # { key1: [(timestamp, value), (timestamp, value)],
        #   key2: [(timestamp, value), (timestamp, value)] }

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        # 2 cases:  - when the key doesn't exist
        if key not in self.dictionary: return ""
        #           - when the key exist, but timestamp too early

        items = self.dictionary[key]
        left, right = 0, len(items) - 1
        
        while left <= right:
            middle = left + (right - left) // 2 # to avoid integer overflow
            # current timestamp too big
            if items[middle][0] > timestamp:
                right = middle - 1
            # current timestamp not big enough
            else:
                left = middle + 1
        
        return items[right][1] if right >= 0 else ""
