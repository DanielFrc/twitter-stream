import tweepy
import json
import logging

from aws_utilities.FirehoseClient import FirehoseClient
from twitter_api_handler.MapStatusToObject import MapStatusToObject


"""
Class needed to handle events in a tweepy Stream
"""

class TweetsListener(tweepy.StreamListener):
    #Initializing variables for objects
    firehose_handler = ""
    firehose_client = ""
    map_status_obj = ""

    def __init__(self, api=None):
        super().__init__(api=api)
        
        #Object to manage firehose connections
        self.firehose_handler = FirehoseClient()
        
        #Object  to Map Status Obcjet to Dicctionary (cleaning data)
        self.map_status_obj = MapStatusToObject()

    def on_connect(self):
        """
        Function to handle actions when tweepy connects to Stream
        """
        logging.info("Begin connection to tweepy stream")
        
        #Obtain the firehose client to connect while the stream is active
        #self.firehose_client = self.firehose_handler.get_firehose_client()

    def on_status(self, status):
        """
        Function to handle actions every time the stream gets an object (status)
            Parameters:
                status (obj): Status object with all tweet information
        """
        try:

            logging.info("Cleaning data for firehose")
            #Clean and transform the status to fit better with a json structure
            tweet = self.map_status_obj.clean_status_object(status)
            
            #Convert tweet information to json 
            logging.info("Converting data to json")
            tweet_json = json.dumps(tweet,ensure_ascii=False)
            logging.info(tweet_json)
            
            #Putting record to firehose
            logging.info("Putting data to json")
            #self.firehose_handler.put_record(self.firehose_client, tweet_json)
        
        except Exception as e:
            #Handling exception
            logging.exception("Error while converting data to JSON")

        
    def on_error(self, status_code):
        """
        Function to handle errors from twitter data
            Parameters: 
                status_code: Error code 
        """
        logging.error("Error %s", str(status_code))
    
