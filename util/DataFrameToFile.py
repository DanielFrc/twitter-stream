#Importing constants
import logging
from util import constants as constants 

'''
Class to generate files from a dataframe            
'''
class DataFrameToFile:

    def generate_csv (self, df, csv_name):
        '''
        Generate a CSV file from a dataframe
            Parameters: 
                df (pandas.DataFrame): The dataframe source for csv (withot path and extension)
                csv_name (str): Name of the CSV generated

        '''
        try:
            #String with the full path of the csv, concatenates path,  name and extension
            full_name = constants.CSV_FOLDER + csv_name + constants.CSV_EXTENSION

            #Converting dataframe to csv with UTF-8 encoding and ignoring index
            df.to_csv(full_name,
                    index=False,
                    encoding=constants.UTF8_ENCODING)
        
        except Exception as e:
            #Handling exceptions
            logging.exception("Error ocurred generetating csv")

    def generate_parquet (self, df, parquet_name):
        '''
        Generate parquet file from a dataframe
            Parameters: 
                df (pandas.DataFrame): The dataframe source for csv (withot path and extension)
                csv_name (str): Name of the CSV generated

        '''
        try:
            #String with the full path of the parquet, concatenates path,  name and extension
            full_name = constants.PARQUET_FOLDER + parquet_name + constants.PARQUET_EXTENSION

            #Converting dataframe to csv with UTF-8 encoding, ignoring index and gzip compression
            df.to_parquet(full_name,
                                index=False,
                                compression=constants.GZIP_COMPRESSION)

        except Exception as e:
           #Handling exceptions
           logging.exception("Error ocurred generetating parquet file")