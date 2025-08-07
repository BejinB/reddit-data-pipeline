# reddit-data-pipeline

## 🚀End-to-End Reddit Data Pipeline using Apache Airflow, Celery, PostgreSQL and AWS Services(S3, Glue, Crawler, Athena, Redshift & QuickSight)

This project is a fully orchestrated, production-style data pipeline built to extract Reddit post data, transform it, and visualize insights using various AWS services. The pipeline simulates a real-world scenario by integrating tools for scheduling, processing, storing, and visualizing data at scale.
## 🛠️Architecture


<img width="1525" height="529" alt="Reddit flow2" src="https://github.com/user-attachments/assets/8e1a0462-2545-4927-980e-fd362695d150" />



## 🧪Tech Stack
- **PRAW** (Python Reddit API Wrapper) – Reddit data extraction
- **Apache Airflow** – Workflow orchestration
- **Docker** – Containerization & environment setup
- **Celery** – Distributed task queue
- **PostgreSQL** – Intermediate database
- **AWS S3** – Data lake (raw & transformed storage)
- **AWS Glue** – Data ETL jobs using PySpark
- **AWS Crawler** – Metadata cataloging
- **AWS Athena** – SQL querying on S3
- **Amazon Redshift** – Data warehousing
- **Amazon QuickSight** – Data visualization



## 🔄Workflow Overview
#### 1️⃣Docker Setup for Local Development
To run the Airflow DAGs locally:
```
docker-compose up --build
```
Access the Airflow UI at:
```
 http://localhost:8081
```
#### 2️⃣Reddit Data Extraction
- Reddit posts are extracted using PRAW via a custom Airflow DAG.
- Stored as CSV in local storage.
#### 3️⃣Upload to AWS S3
Raw CSV data is uploaded to the S3 bucket
```
s3://reddit-pipeline-bejin/raw/.
```

#### 4️⃣AWS Glue ETL
- An AWS Glue Job reads the raw CSV from S3.
- It performs transformations such as Column merging, Data cleaning.
- The cleaned data is saved to:
```
s3://reddit-pipeline-bejin/transformed/.
```

#### 5️⃣Crawler & Athena
- An AWS Glue Crawler scans the transformed S3 data and creates or updates tables in the AWS Glue Data Catalog.
- AWS Athena is used to validate schema and perform test queries on the transformed data.

#### 6️⃣Redshift Integration
Athena data is loaded into Redshift (reddit_namespace → reddit-workgroup) as reddit_data_eng.

#### 7️⃣Data Visualization

QuickSight connects to Redshift and visualizes insights such as:
- 📊 Top 10 Reddit Authors by Total Score (Bar Chart)
- 📉 Hourly Average Reddit Score Trend (Line Chart)
- 📈 Distribution of Reddit Post Scores (Histogram)
- 🥧 NSFW Status of Reddit Posts (Pie Chart – All SFW Content)

## 📸Airflow DAG – Successful Execution (Graph View)
![WhatsApp Image 2025-07-05 at 22 51 12_163c16ca](https://github.com/user-attachments/assets/9c42226d-34f3-4868-b224-7e00d75b90a3)

## ✅AWS Glue Job Success – reddit_glue_job
![WhatsApp Image 2025-07-06 at 01 00 55_1adb49b3](https://github.com/user-attachments/assets/e8c26d7d-13eb-4242-a27e-4fc35c9c2339)

## ✅ AWS Glue Crawler – reddit_crawler Run Completed
![WhatsApp Image 2025-07-06 at 01 15 36_34e3bcc9](https://github.com/user-attachments/assets/93a5218b-94b1-444d-b7d2-1488828f6058)

## ✅ AWS Athena Output – Query Results from Transformed Data
**Query Used:**
```sql
SELECT * FROM "AwsDataCatalog"."reddit_db"."transformed" LIMIT 10;
```
![WhatsApp Image 2025-07-06 at 11 02 44_ca2f94f7](https://github.com/user-attachments/assets/860ccafd-600a-48ce-9faa-3a8a7ea229d9)

## 📄Before Redshift (Athena External Table)
AWS Redshift – Querying External Table from AWS Glue/Athena

**Query Used:**
```sql
SELECT * FROM "awsdatacatalog"."reddit_db"."transformed";
```
![WhatsApp Image 2025-07-06 at 11 22 40_44a6c46c](https://github.com/user-attachments/assets/ed5054db-6ba8-4148-8c3a-cee54ed853e7)

## 📄After Redshift (Redshift Native Table)
AWS Redshift – Querying Native Table after Data Load

**Query Used:**
```sql
SELECT * FROM "dev"."public"."reddit_data_eng";
```
![WhatsApp Image 2025-07-06 at 11 32 23_0f74737d](https://github.com/user-attachments/assets/77134d03-97e7-43bc-bfcd-e704da8bead4)

## 📊 Amazon QuickSight Visualizations
#### 📊 QuickSight – Top 10 Reddit Authors by Score (Bar Chart)
![WhatsApp Image 2025-07-06 at 13 41 37_24ae112f](https://github.com/user-attachments/assets/916c4f7b-eb38-497b-a5d5-0d3f40cce1b3)
 
#### 📈 QuickSight – Hourly Average Reddit Score Trend (Line Chart)
![WhatsApp Image 2025-07-06 at 13 54 16_a15a8e81](https://github.com/user-attachments/assets/f01dbdcd-3646-42c3-ab58-fa039acb2d6d)

#### 📉 QuickSight – Distribution of Reddit Post Scores (Histogram)
![WhatsApp Image 2025-07-06 at 14 06 10_76df9c33](https://github.com/user-attachments/assets/20302789-671a-4bae-833c-a941bd596369)

#### 🥧 QuickSight – NSFW vs SFW Posts (Pie Chart)
![WhatsApp Image 2025-07-06 at 14 24 44_2c601654](https://github.com/user-attachments/assets/d3dc2beb-7c21-4dd5-9a5a-955089fa7eb9)

