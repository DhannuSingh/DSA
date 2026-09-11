class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}  # userId -> list of (time, tweetId)
        self.following = {}  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        max_heap = []

        # Include the user's own followee list along with themselves
        user_ids = self.following.get(userId, set()) | {userId}

        # Push the most recent tweet of each followed user into the max-heap
        for uid in user_ids:
            if uid in self.tweets and self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]
                # Use negative time for max-heap behavior with Python's min-heap
                heapq.heappush(max_heap, (-time, tweetId, uid, idx))

        # Retrieve up to 10 most recent tweets
        while max_heap and len(res) < 10:
            neg_time, tweetId, uid, idx = heapq.heappop(max_heap)
            res.append(tweetId)

            # If the user has older tweets, add the next most recent one to the heap
            if idx > 0:
                prev_time, prev_tweetId = self.tweets[uid][idx - 1]
                heapq.heappush(max_heap, (-prev_time, prev_tweetId, uid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.following:
                self.following[followerId] = set()
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)