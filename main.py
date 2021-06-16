import pandas as pd
import logging 
from datetime import datetime

from twitter_api_handler.TweetStreamHandler import TweetStreamHandler 
from twitter_api_handler.TweetCursorHandler import TweetCursorHandler 
from util import constants as constants 


def main():
    #Getting the date for files
    date = datetime.now().strftime(constants.DATE_FOR_FILES)
    
    #Initialize Logging
    logging.basicConfig(filename=constants.LOG_FOLDER + 
                                 constants.LOG_NAME + 
                                 date + constants.LOG_EXTENSION,
                        level=logging.INFO,
                        format=constants.LOG_FORMAT,
                        encoding=constants.UTF8_ENCODING)

    logging.info("Process started")

    
    tweet_stream_handler = TweetStreamHandler()

    tracks = constants.TRACKS

    tweet_stream_handler.start_stream_by_track(tracks)

    """

    twitter_cursor_handler = TweetCursorHandler() 
    
    tweets = twitter_cursor_handler.cursor_handler(query="amlo",
                                                   items=10,
                                                   generate_files=True,
                                                   file_name="amlo_tweets")
    tweets.head()
    
    """
    logging.info("Process ended")


if __name__ == '__main__':
    main()