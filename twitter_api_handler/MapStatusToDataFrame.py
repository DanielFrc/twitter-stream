import pandas as pd

"""
Class to mapping tweepy status object to Dataframe
"""
class MapStatusToDataFrame:
    # Array with column definition for dataframe
    columns = ["created_at",
               "id",
               "id_str",
               "text",
               "source",
               "source_url",
               "in_reply_to_status_id",
               "in_reply_to_status_id_str",
               "in_reply_to_user_id",
               "in_reply_to_user_id_str",
               "in_reply_to_screen_name",
               "user",
               "location",
               "geo",
               "coordinates",
               "place",
               "contributors",
               "is_quote_status",
               "retweet_count",
               "favorite_count",
               "favorited",
               "retweeted",
               "lang"]
    
    def generate_tweets_dataframe (self, tweets):
        """
        Function to convert tweet list to pandas.Dataframe
            Parameters:
                tweets(object): Tweet list to convert.
            
            Return:
                tweets_df(pandas.DataFrame):  Dataframe with tweets
        """
        tweets_df = pd.DataFrame(data=tweets,
                                 columns=self.columns)
        return tweets_df

    

