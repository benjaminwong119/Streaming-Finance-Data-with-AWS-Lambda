# Streaming-Finance-Data-with-AWS-Lambda

## Introduction

The purpose of this project is to use “real-time” data, process the data, and then transform it into a format that facilitates querying and further analysis in real time or near real time capacity. A Lambda function is used to collect and process the data and is pushed to a Kinesis Delivery Stream that uploads to an AWS S3 Bucket to emulate near real-time finance data records for downstream processing and interactive querying. AWS Glue is then used on the AWS S3 Bucket to allow querying of the data using AWS Athena to gain insight into the streamed data. 

## Data Transformation

The data is collected using yfinance which will grab pricing information for each of the following e-commerce stocks from Yahoo finance:
* Amazon (AMZN)
* Alibaba Group (BABA)
* Walmart (WMT)
* eBay (EBAY)
* Shopify (SHOP)
* Target (TGT)
* Best Buy (BBY)
* The Home Depot (HD)
* Costco (COST)
* Kroger (KR)

Collect one full day’s worth of stock HIGH and LOW prices for each company listed above between Nov Oct 24th, 2022, and Nov 04th, 2022, at a five-minute interval.
	Example of a single record:
{
  "high": 67.5, 
  "low": 64.61, 
  "volatility": 2.89,
  "ts": "2020-05-13 09:30:00-04:00", 
  "name": "AMZN"
}
	Volatility refers to difference between high and low values and ts is a string of the date and time.


## Data Collecting
Push the data from the AWS Lambda function to a Kinesis delivery stream which then stores the data into an AWS S3 bucket.

## Data Analysis
Set up an AWS Glue crawler so AWS Athena queries can run against the data. Write and run a query that gives us the average volatility, the highest volatility, and the lowest volatility per company per day from the list above.  

## Data Visualization
1. Graph the average volatility trend per company. (A single Line Chart: Each line refers to a company)
Which company is the most volatile?

2. Graph the daily highest volatility per company. (A Grouped Bar Chart: Each group refers to a company and the bars refer to the daily highest volatility)
Do the findings from this graph support your conclusion from the first graph?

3. Graph the normalized average volatility per company. (A Bar Chart: Each bar refers to a company)
Calculate the average of Normalized Average per company. Normalization allows the comparison of quantities or objects on an appropriate scale. In this case, which company is actually the most volatile?
Normalized Average = (Average Volatility – Minimum Volatility) / (Maximum volatility – Minimum Volatility)

4. Graph the normalized average volatility on October 24th, 2022. (A Bar Chart: Each bar refers to a company)
Which company is the most volatile on October 24th, 2022?

## Screenshots
S3 Bucket page:
![image](https://user-images.githubusercontent.com/103864579/209571946-0f164c76-69ae-4056-9c2a-bbcea4765e03.png)

AWS Kinesis Monitoring page: 
![image](https://user-images.githubusercontent.com/103864579/209572024-6b321cb2-0fac-44f3-a663-27f38296d389.png)

Execution Results in AWS Lambda Management Console: 
![image](https://user-images.githubusercontent.com/103864579/209572032-28d302f3-cfcc-4024-9320-ad07fe6078f7.png)

Athena Results: 
![image](https://user-images.githubusercontent.com/103864579/209572038-d6ec9e32-12f2-4456-8e2f-f7da9990758c.png)

## Answers to visualization questions:

1. Which data is the most volatile?

![image](https://user-images.githubusercontent.com/103864579/209572209-144daec7-d642-42cd-ba08-76b89e72bb88.png)

Based on the line graph, Costco ($COST) is the most volatile stock.

2. Does the daily highest volatility per company support the previous graph?

![image](https://user-images.githubusercontent.com/103864579/209572225-a25a7328-6ae3-47d3-9e4f-5d1898c6550f.png)

This graph supports the last one as Costco ($COST) has the highest volatility for a majority of the days

3. Normalization allows the comparison of quantities or objects on an appropriate scale. In this case, which company is actually the most volatile?

![image](https://user-images.githubusercontent.com/103864579/209572232-4d54a521-014f-4401-8cec-1b0c757d3f5c.png)

After normalizing the volatility, Amazon ($AMZN) is now the most volatile.

4. Which company was the most volatile on October 24th, 2022?

![image](https://user-images.githubusercontent.com/103864579/209572245-779508a8-de38-4522-9529-d495e2eeeaa0.png)

Kroger ($KR) was the most volatile company on October 24, 2022.
