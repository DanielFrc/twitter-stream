import tweepy
import json
import logging

from aws_utilities.FirehoseClient import FirehoseClient
from twitter_api_handler.MapStatusToObject import MapStatusToObject
from twitter_api_handler.MapStatusToDataFrame import MapStatusToDataFrame
from twitter_api_handler.MapStatusToList import MapStatusToList
from util.DataFrameToFile import DataFrameToFile
from util import constants as constants 

"""
Class needed to handle events in a tweepy Stream
"""

class TweetsListener(tweepy.StreamListener):
    #Initializing variables for objects
    firehose_handler = ""
    firehose_client = ""
    map_status_obj = ""
    map_status_df = ""
    map_status_list = ""
    dataframe_to_file = ""
    tweets_dataframe = []
    CSV_NAME = "tweet_stream"


    def __init__(self, api=None):
        super().__init__(api=api)
        
        #Object to manage firehose connections
        self.firehose_handler = FirehoseClient()
        #Object  to Map Status Object to Dicctionary (cleaning data)
        self.map_status_obj = MapStatusToObject()
        #Object  to Map Status Object to dataframe (cleaning data)
        self.map_status_df = MapStatusToDataFrame()
        #Object to Map Status Object to list 
        self.map_status_list = MapStatusToList()
        #Object  to generate files from dataframe
        self.dataframe_to_file = DataFrameToFile()

        

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

            #logging.info(tweet_json)
            
            #Putting record to firehose
            logging.info("Putting data to firehose")
            #self.firehose_handler.put_record(self.firehose_client, tweet_json)

            #Putting data to dataframe
            self.generate_dataframe(status)

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


    def generate_dataframe(self, status):
        """
        Function to handle the generation of csv files
            Parameters:
                status (obj): Status object with all tweet information
        """

        #Appending tweet to tweet array
        self.tweets_dataframe.append(self.map_status_list.map_tweepy_array(status))

        #Verify if records are enough to make csv
        if(len(self.tweets_dataframe) == constants.CSV_MAX_RECORDS ):
            self.generate_csv()
            
           
    
    def generate_csv(self):
        """
        Function to trigger CSV generatio every constants.CSV_MAX_RECORDS
        """
        logging.info("Creating new csv with %d records", constants.CSV_MAX_RECORDS)
        #Creating a dataframe from array
        df = self.map_status_df.generate_tweets_dataframe(self.tweets_dataframe)
            
        #generating CSV from dataframe
        self.dataframe_to_file.generate_csv(df,
                                                self.CSV_NAME)
        #reinitialize array
        self.tweets_dataframe = []