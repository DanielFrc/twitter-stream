import logging

from twitter_api_handler.MapStatusToDataFrame import MapStatusToDataFrame 
from twitter_api_handler.GetTwitterCursorQueryProccesor import GetTwitterCursorQueryProccesor 
from util.DataFrameToFile import DataFrameToFile


"""
Class to handle tweepy cursor request
"""
class TweetCursorHandler:
    #Initializing variables for objects
    status_to_dataframe = ""
    twitter_cursor_query = ""
    dataframe_to_file = ""

    def __init__(self):
        super().__init__()
        #Object to map status to dataframe
        self.status_to_dataframe = MapStatusToDataFrame()
        #Object to obtain a query tweepy cursor
        self.twitter_cursor_query = GetTwitterCursorQueryProccesor()
        #Object to convert dataframe to file
        self.dataframe_to_file = DataFrameToFile()
    

    def cursor_handler(self, 
                       query,
                       items, 
                       generate_files=False,
                       file_name=""):

        """
        Function to handle a cursor request
            Parameters:
                query (str): String with a twitter query to retrieve tweets
                items (int): Amount of tweets to retrieve, a huge amount can cause errors
                generate_files (boolean): Set True to generate CSV and Parquet
                file_name (str): The name for the csv and parquet file, it must be without path and extension
            
            Return
                df (pandas.DataFrame): Dataframe with the tweets
        """
        #Request for tweepy cursor
        logging.info("Requesting for cursor")
        tweets = self.twitter_cursor_query.get_tweepy_list(query = query,
                                                            items=items)

        #Converting tweepy cursor to Data Frame
        logging.info("Converting cursor to DF")
        df = self.status_to_dataframe.generate_tweets_dataframe(tweets)

        
        #Genereting csv and parquet files
        if(generate_files):
            logging.info("Generating Files")
            self.dataframe_to_file.generate_csv(df,file_name)
            self.dataframe_to_file.generate_parquet(df,file_name)


        return df
    
