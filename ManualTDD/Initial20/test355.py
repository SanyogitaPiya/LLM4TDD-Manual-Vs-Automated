def test_basic_functionality():
    twitter = Twitter()

    twitter.postTweet(1, 5)
    result1 = twitter.getNewsFeed(1)  # [5]

    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    result2 = twitter.getNewsFeed(1)  # [6, 5]

    twitter.unfollow(1, 2)
    result3 = twitter.getNewsFeed(1)  # [5]

    assert result1 == [5]
    assert result2 == [6, 5]
    assert result3 == [5]