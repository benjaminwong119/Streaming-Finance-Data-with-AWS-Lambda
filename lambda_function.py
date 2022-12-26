import pandas as pd
import json
import boto3
import yfinance as yf
from time import sleep
import os
from datetime import date

REGION=os.environ["REGION"]
STREAMNAME=os.environ["STREAMNAME"]

kinesis = boto3.client('kinesis', REGION)


def getReferrer():
    tickers_list = ["AMZN","BABA", "WMT", "EBAY", "SHOP", "TGT", "BBY", "HD", "COST","KR"]
    data= {}
    temp_data = []
    for ticker in tickers_list:
        ticker_object = yf.Ticker(ticker)
        ticker_object_df = ticker_object.history(start="2022-10-24", end="2022-11-05", interval="5m").reset_index()
        ticker_object_df["volatility"] = round(ticker_object_df['High'] - ticker_object_df['Low'],2)
        ticker_object_df["ts"]=ticker_object_df["Datetime"].astype(str)
        ticker_object_df["name"]=str(ticker)
        ticker_object_df=ticker_object_df.drop(columns=["Datetime","Open","Close","Volume","Dividends","Stock Splits"])
        ticker_object_df=ticker_object_df.rename(columns={"High": "high", "Low": "low","Datetime":"ts"})
        temp_data.append(ticker_object_df)
    temp_data=pd.concat(temp_data).reset_index(drop=True)
    data = temp_data.to_dict(orient="records")
    return data

def lambda_handler(event,context):
    today = str(date.today())
    getReferrer()
    for x in getReferrer():
        if x['ts'][:10]=="2022-12-16": #avoid code pulling date incorrectly
            continue
        else:
            data1 = json.dumps(x)+"\n"
            kinesis.put_record(StreamName=STREAMNAME,Data=data1,PartitionKey="partitionkey")
            print(data1)
            sleep(0.05)
    return {'statusCode': 200,    'body': json.dumps('Done!')}
