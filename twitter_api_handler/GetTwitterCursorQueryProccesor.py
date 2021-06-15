from twitter_api_handler.TweepyConnection import TweepyConnection
import tweepy as tw

"""
Class to encapsulate the proccess to retrieve a tweepy cursor and mapping to a tweet object ready for dataframe
"""

class GetTwitterCursorQueryProccesor: 
    #Initializing variables for objects
    tweepy_connection = ""

    def __init__(self):
        super().__init__()
        #Object to handle tweepy Connection
        self.tweepy_connection = TweepyConnection()
    
    def get_tweepy_list (self, query, items=10):
        """
        Function to connect to twitter API and get a list of tweets (Status Object)
            Params: 
                query(str): Query in twitter format (see https://docs.tweepy.org)
                items(int): Number of tweets to get
            Return:
                tweets_list(Array): The result of the query
        """
        api = self.tweepy_connection.connect_api()
        tweets = tw.Cursor(api.search, q=query).items(items)

        tweets_lists = self.map_tweepy_list(tweets)

        return tweets_lists
    
    def map_tweepy_list (self, tweets):
        """
        Function to map status object to a simple list (csv compatible)
            Params: 
                tweets(str): List of tweets in raw format
            Return:
                tweets_list(Array): Array of tweets in a clean format.
        """
        tweets_lists = [[tweet.created_at,
                          tweet.id,
                          tweet.id_str,
                          tweet.text,
                          tweet.source,
                          tweet.source_url,
                          tweet.in_reply_to_status_id,
                          tweet.in_reply_to_status_id_str,
                          tweet.in_reply_to_user_id,
                          tweet.in_reply_to_user_id_str,
                          tweet.in_reply_to_screen_name,
                          tweet.user.screen_name,
                          tweet.user.location,
                          tweet.geo,
                          tweet.coordinates,
                          tweet.place,
                          tweet.contributors,
                          tweet.is_quote_status,
                          tweet.retweet_count,
                          tweet.favorite_count,
                          tweet.favorited,
                          tweet.retweeted,
                          tweet.lang ] for tweet in tweets]

        return tweets_lists
