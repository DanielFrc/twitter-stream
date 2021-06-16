# Twitter Stream
***
Twitter Stream is a python process that connects to Twitter API to get tweets of a given track. Also, will give an option to connect with Kinesis to put data in streams (Firehose or Kinesis).

The Twitter Stream project use **tweepy** to connect with Twhitter API and boto3 to connect with Aws services.

## Table of contents
***
-Support
-Before you start
-Installation Guide
-Configuration
-Usage
-License

## Support
***
This project is under construction, if you need help feel free to contact me in [Link](hola@danielfranco.me)

## Before you start
***

Before you start, you may have an Twitter Developer account and Amazon Web Services account.

Also, for AWS connection, you need to set your credentials with aws cli, pleas reffer to AWS docs for this

## Installation Guide

This proyect has some dependencies like pandas, tweepy, parquet and boto3. To install the dependencies you must use pip3 command like this:

```
pip3 install pandas --user
pip3 install tweepy --user
pip3 install json --user
pip3 install boto3 --user
pip3 install parquet --user
```

## Configuration

For usage, you may edit the util/constants.py to set your twitter secrets.

```
TWITTER_CONSUMER_KEY = "TWITTER_CONSUMER_KEY"
TWITTER_CONSUMER_SECRET = "TWITTER_CONSUMER_SECRET"
TWITTER_ACCESS_KEY = "TWITTER_ACCESS_KEY"
TWITTER_ACCESS_SECRET = "TWITTER_ACCESS_SECRET"
TWITTER_BEARER_TOKEN = "TWITTER_BEARER_TOKEN"
```

*__Note:__ in a next realese, the password management may change to AWS secrets.*

Also, you need to configure tweepy as you need on util/constants.py :

-__MAX_CONNECTION_RETRIES:__ Maximum reconnection attempts before the process end,  10 by default
-__MAX_CONNECTION_SLEEP:__ = Time to wait in seconds before a connection attempt, 30 by default
-__CSV_MAX_RECORDS:__ = Number of tweets before a csv is generated, 500 generates a file every 5 min aprox.
-__TRACKS:__ Python list with topics or hashtags to listen in the stream.

```
#Tweepy Connection configuration
MAX_CONNECTION_RETRIES = 10  
MAX_CONNECTION_SLEEP = 30    
CSV_MAX_RECORDS = 500        

#Topics to catch with stream
TRACKS = ["python", "aws"] #Topics or hashtags to listen in the stream.
```
*__Note:__ in next realeses, a process will concatenate the csv.*


Optionaly, you can customize the file management in utils/constants.py, by deffault the parameters are by following

```
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
```

*__Note:__ To prevent file duplications and errors, every filename concatenates the date in the format YYYMMDD_HHMISS, if is needed you can modify the date format as follows:*

```
#format constants
DATE_FOR_FILES = "_%Y%m%d_%H%M%S"
```

For logging options, the projects option the Logging library of python. You can modify the template in util/constants.py

```
#format constants
DATE_FOR_FILES = "_%Y%m%d_%H%M%S"
LOG_FORMAT = "%(asctime)s %(message)s"
```

## Usage

For usage, you may execute the main.py script from command line:

```
python main.py
```

The process continues runnig until a key interruption is detected `Ctrl + c`, in future versions you may configure the time tha proccess will capture data.