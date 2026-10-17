class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        num_boats = 0
        left, right = 0, n-1
        while left <= right:
            remain = limit - people[right]
            right -= 1
            num_boats += 1
            if left <= right and remain >= people[left]:
                left += 1
        return num_boats