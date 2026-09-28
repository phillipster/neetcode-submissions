class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def collide(s, a):
            while s:
                if s[-1] < 0:
                    s.append(a)
                    return
                if s[-1] < abs(a):
                    s.pop()
                elif s[-1] == abs(a):
                    s.pop()
                    return
                else:
                    return
            s.append(a)
        s = []
        for a in asteroids:
            if not s:
                s.append(a)
            else:
                if a > 0:
                    s.append(a)
                else:
                    collide(s, a)
                    
        return s