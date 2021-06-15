#from datetime import datetime

"""
    Class to convert status object to a diccitonary to handle better the conversión to JSON
    Only to post to Kinesis Data Firehose
"""
class MapStatusToObject :
    
    def clean_status_object (self, status):
        """
        Function to convert status object to a tweet dictionary (to fit better to a json format for Firehose)
            Parameters:
                status(object): Tweepy Status object with tweet information
            Return:
                tweet(dicctionary): Dicctionary with tweet information
        """
        tweet = {
            "created_at": status.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            "id": status.id,
            "id_str": status.id_str,
            "truncated" : status.truncated,
            "text": status.text,
            "source": status.source,
            "source_url": status.source_url,
            "in_reply_to_status_id": status.in_reply_to_status_id,
            "in_reply_to_status_id_str": status.in_reply_to_status_id_str,
            "in_reply_to_user_id": status.in_reply_to_user_id,
            "in_reply_to_user_id_str": status.in_reply_to_user_id_str,
            "in_reply_to_screen_name": status.in_reply_to_screen_name,
            "user_id": status.user.id,
            "user_name": status.user.screen_name,
            "user_location": status.user.location,
            "geo": status.geo,
            "coordinates": status.coordinates,
            "place": status.place,
            "contributors": status.contributors,
            "is_quote_status": status.is_quote_status,
            "retweet_count": status.retweet_count,
            "favorite_count": status.favorite_count,
            "favorited": status.favorited,
            "retweeted": status.retweeted,
            "lang": status.lang
        }

        if status.truncated:
           tweet["text"] = status.extended_tweet['full_text']
            
        return tweet
        




