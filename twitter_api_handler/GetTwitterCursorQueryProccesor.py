from twitter_api_handler.TweepyConnection import TweepyConnection
from twitter_api_handler.MapStatusToList import MapStatusToList

import tweepy as tw

"""
Class to encapsulate the proccess to retrieve a tweepy cursor and mapping to a tweet object ready for dataframe
"""

class GetTwitterCursorQueryProccesor: 
    #Initializing variables for objects
    tweepy_connection = ""
    map_status_list = ""


    def __init__(self):
        super().__init__()
        #Object to handle tweepy Connection
        self.tweepy_connection = TweepyConnection()
         #Object to Map Status Object to list 
        self.map_status_list = MapStatusToList()
    
    def get_tweepy_list (self, query, items=10):
        """
        Function to connect to twitter API and get a list of tweets (Status Object)
            Params: 
                query(str): Query in twitter format (see https://docs.tweepy.org)
                items(int): Number of tweets to get
            Return:
                tweets_list(Array): The result of the query
        """
        #Connecting to twitter API
        api = self.tweepy_connection.connect_api()
        
        #Request for cursor
        tweets = tw.Cursor(api.search, q=query).items(items)
        
        #Converting cursor to list
        tweets_lists = self.map_status_list.map_tweepy_list(tweets)

        return tweets_lists