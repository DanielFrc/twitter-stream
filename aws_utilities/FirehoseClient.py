import boto3
import logging

from util import constants as constants 

"""
Class to manage connectios with firehose
"""
class FirehoseClient:

    def get_firehose_client(self):
        """
        Function to get the Kinesis Data Firehose cliente
        Return:
            boto3.client: Firehose client
        """
        #Create and returning a boto3 client 
        return boto3.client(constants.CLIENT_FIREHOSE_NAME)
    
    def put_record(self, client, data):
        """
        Function to put record to Firehose
        Parameters:
            client(boto3.client): Client with AWS Credentials
            data(JSON): Data in JSON format to put in firehose
        """
        logging.info("Connecting to Kinesis Data Firehose")

        try:
            client.put_record(
                DeliveryStreamName=constants.STREAM_NAME,
                Record={'Data': data }
            )

        except Exception as e:
            logging.exception("Error putting record to firehose")
        
        finally:
            logging.info("Ending connection with Kinesis Data Firehose")
        

