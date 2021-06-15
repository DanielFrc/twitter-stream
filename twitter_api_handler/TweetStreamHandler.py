import tweepy as tw
import logging
from time import sleep
from twitter_api_handler.TweepyConnection import TweepyConnection
from twitter_api_handler.TweetsListener import TweetsListener
from util import constants as constants 


"""
Class to handle tweepy streams. Start a stream, filter by track (topic) and manage errors and reconnections
"""
class TweetStreamHandler:
    #Initializing variables for objects
    stream_aux = ""
    tweepy_con = ""

    
    def __init__(self):
        """
        Function to instanciate the classes used by the proccess
        """
        super().__init__()

        #Object to initilize the tweepy listener with the tweepy template
        self.stream_aux = TweetsListener()

        #Object to handle the connection to twitter (from tweepy)
        self.tweepy_con = TweepyConnection()
    
    
    def start_stream_by_track (self,track_array, reconnect=0):
        """
        Function to start a stream by track (Topic in twitter)
            Parameters:
                track_array (str[]): The list of topics to capture in the stream
                reconnect (int): Aux parameter to handle reconnections. Init on 0
        """

        try: 
            #Get the API connection 
            logging.info("Getting connection to Twitter API")
            api_tweet = self.tweepy_con.connect_api()
            
            #Initialize the stream
            logging.info("Connecting to Stream")
            streaming_api = tw.Stream(auth = api_tweet.auth,
                                      listener=self.stream_aux)
            
            logging.info("Setting filter for stream")
            #filter the stream wit track array
            streaming_api.filter(track=track_array)

        except Exception as e:
            #Handling exception
            logging.exception("Error while connecting to the stream, trying to connect again")

            #Reconnecting to stream
            if(reconnect < constants.MAX_CONNECTION_RETRIES): 
                sleep(constants.MAX_CONNECTION_SLEEP)
                self.start_stream_by_track(track_array,
                                           reconnect + 1 )
        
        finally:
            logging.info("Ending connection to Twitter Stream")
