"""
File to manage constants for the process
"""
#TWITTER_CREDENTIALS_CONSTANTS


TWITTER_CONSUMER_KEY = "TWITTER_CONSUMER_KEY"
TWITTER_CONSUMER_SECRET = "TWITTER_CONSUMER_SECRET"
TWITTER_ACCESS_KEY = "952423405-TWITTER_ACCESS_KEY"
TWITTER_ACCESS_SECRET = "TWITTER_ACCESS_SECRET"
TWITTER_BEARER_TOKEN = "TWITTER_BEARER_TOKEN"


#FIREHOSE_DATA
STREAM_NAME = "tweet-delivery-stream"
CLIENT_FIREHOSE_NAME = "firehose"

#Tweepy Connection configuration
MAX_CONNECTION_RETRIES = 3
MAX_CONNECTION_SLEEP = 10
CSV_MAX_RECORDS = 500

#Topics to catch with stream
TRACKS = ["amlo"]

#File management constants
CSV_FOLDER = "data/csv/"
JSON_FOLDER = "data/json/"
PARQUET_FOLDER = "data/parquet/"
CSV_EXTENSION = ".csv"
PARQUET_EXTENSION = ".parquet.gzip"
UTF8_ENCODING = "utf-8"
GZIP_COMPRESSION="gzip"
LOG_FOLDER = "logs/"
LOG_NAME = "twitter_stream"
LOG_EXTENSION = ".log"

#format constants
DATE_FOR_FILES = "_%Y%m%d_%H%M%S"
LOG_FORMAT = "%(asctime)s %(message)s"
