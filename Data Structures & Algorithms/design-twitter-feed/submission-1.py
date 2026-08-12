class Twitter:

    def __init__(self):
        # List of tweets, likely need to be maxHeaped based on num of operations
        self.tweets = [] # [opNum, userId, tweetId]
        heapq.heapify_max(self.tweets)

        # dictionary of followers -> followees
        self.userFollowers = defaultdict(set)
        self.opNum = 0
    

    # User of userId posts tweet of tweetId, tweetId is unique
    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush_max(self.tweets, [self.opNum, userId, tweetId])
        self.opNum += 1

    
    # fetches up to 10 most recent tweet Ids, must be from usrs that are being followed or by the user itself, most recent -> least recent
    def getNewsFeed(self, userId: int) -> List[int]:
        analyzed = []
        res = []

        while len(res) < 10 and self.tweets:
            followers = self.userFollowers[userId]

            tweet = heapq.heappop_max(self.tweets)
            analyzed.append(tweet)

            if tweet[1] in followers or tweet[1] == userId:
                res.append(tweet[2])
            
        while analyzed:
            heapq.heappush_max(self.tweets, analyzed.pop())
        
        return res

    
    # follow the user
    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowers[followerId].add(followeeId)
    
    # unfollow the user
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollowers[followerId]:
            self.userFollowers[followerId].remove(followeeId)

    

        
