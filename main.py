import pandas as pd
import logging 
from datetime import datetime

from twitter_api_handler.TweetStreamHandler import TweetStreamHandler 
from twitter_api_handler.TweetCursorHandler import TweetCursorHandler 
from util import constants as constants 


def main():
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    logging.basicConfig(filename=constants.LOG_FOLDER + constants.LOG_NAME + date + constants.LOG_EXTENSION,
                        level=logging.INFO,
                        format="%(asctime)s %(message)s",
                        encoding='utf-8',
                        filemode='w')

    logging.info("Process started")


    tweet_stream_handler = TweetStreamHandler()

    tracks = ["amlo"]

    tweet_stream_handler.start_stream_by_track(tracks)

    #twitter_cursor_handler = TweetCursorHandler() 
    """
    tweets = twitter_cursor_handler.cursor_handler(query="amlo",
                                                   items=10,
                                                   generate_files=True,
                                                   file_name="amlo_tweets")

    tweets.head()
    """
    logging.info("Process ended")


if __name__ == '__main__':
    main()


