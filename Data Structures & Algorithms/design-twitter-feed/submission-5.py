import heapq

class Twitter:

    def __init__(self):
        self.n = 0
        self.tweets = []
        self.users = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.n, userId, tweetId))
        self.n += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        for i in range(len(self.tweets)-1, -1, -1):
            if len(h) == 10:
                break
            if self.tweets[i][1] == userId or self.tweets[i][1] in self.users[userId]:
                heapq.heappush_max(h, self.tweets[i])
        out = []
        while h:
            out.append(heapq.heappop_max(h)[2])
        print(out)
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
