class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data[key]
        if not arr or timestamp < arr[0][0]:
            return ""
        l, r = 0, len(arr)-1
        ans = l
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            if arr[mid][0] < timestamp:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return arr[ans][1]