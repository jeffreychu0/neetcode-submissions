class Twitter:

    def __init__(self):
        # List of tweets, likely need to be maxHeaped based on num of operations
        self.userTweets = defaultdict(list)

        # dictionary of followers -> followees
        self.userFollowers = defaultdict(set)
        self.opNum = 0
    

    # User of userId posts tweet of tweetId, tweetId is unique
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append([self.opNum, tweetId])
        self.opNum += 1

    
    # fetches up to 10 most recent tweet Ids, must be from usrs that are being followed or by the user itself, most recent -> least recent
    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        res = []

        for tweet in self.userTweets[userId]:
            max_heap.append(tweet)

        for follower in self.userFollowers[userId]:
            for tweet in self.userTweets[follower]:
                max_heap.append(tweet)

        heapq.heapify_max(max_heap)

        while len(res) < 10 and max_heap:
            tweet = heapq.heappop_max(max_heap)
            res.append(tweet[1])

        return res

    
    # follow the user
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.userFollowers[followerId].add(followeeId)
    
    # unfollow the user
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowers[followerId]:
            self.userFollowers[followerId].remove(followeeId)

    

        
