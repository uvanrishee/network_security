import os
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from network_security.exception.exception import NetworkSecurityException
from network_security.logging.logger import logging
load_dotenv()
mongo_url=os.getenv("MONGO_URL")

ca=certifi.where()
class networkdataextract:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def csv_json(self,filepath):
        try:
            data=pd.read_csv(filepath)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def insert_to_mongo(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
            self.mongo_client=pymongo.MongoClient(mongo_url)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return "success"
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
if __name__=="__main__":
    file="C:\\Academic\\networksecurity\\network_data\\phisingData.csv"
    database="uvandb"
    collection="networksec"
    obj=networkdataextract()
    rec=obj.csv_json(file)
    status=obj.insert_to_mongo(rec,database,collection)
    print(status)