from util import constants as constants 
import tweepy as tw

"""
Class to handle connections from tweepy to twitter API
"""
class TweepyConnection:
    

    def generate_auth (self):
        """
        Function to create auth object with twitter secrets. A developer twitter account is needed
            Return:
                auth(object): Object with the acces token for twitter API
        """

        #Setting the consumer secrets with OAuthHandler
        auth = tw.OAuthHandler(constants.TWITTER_CONSUMER_KEY,
                           constants.TWITTER_CONSUMER_SECRET)

        #Request and set access token with the access keys
        auth.set_access_token(constants.TWITTER_ACCESS_KEY,
                      constants.TWITTER_ACCESS_SECRET)

        return auth

    def connect_api (self):
        """
        Function to create connection with tweeter API
            Return:
                API(object): Object with connectors method to Twitter API
        """
        return tw.API(self.generate_auth(),
                      wait_on_rate_limit=True,
                      wait_on_rate_limit_notify=True)
