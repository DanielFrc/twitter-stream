from util import constants as constants

class MapStatusToList:
    def map_tweepy_list (self, tweets):
        """
        Function to map status object to a simple list (csv compatible)
            Params: 
                tweets(obj): List of tweets in raw format
            Return:
                tweets_list(Array): Array of tweets in a clean format.
        """
        tweets_lists = [[tweet.created_at,
                          tweet.id,
                          tweet.id_str,
                          tweet.truncated,
                          tweet.text,
                          str(constants.TRACKS),
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

    def map_tweepy_array (self, tweet):
        """
        Function to map status object to a simple list (csv compatible)
            Params: 
                tweet(str): List of tweets in raw format
            Return:
                tweets_list(Array): Array of tweets in a clean format.
        """
        new_tweet = [tweet.created_at,
                     tweet.id,
                     tweet.id_str,
                     tweet.truncated,
                     tweet.text,
                     str(constants.TRACKS),
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
                     tweet.lang ]

        return new_tweet