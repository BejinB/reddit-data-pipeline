# reddit-data-pipeline

## 🚀End-to-End Reddit Data Pipeline using Apache Airflow, Celery, PostgreSQL and AWS Services(S3, Glue, Crawler, Athena, Redshift & QuickSight)

This project is a fully orchestrated, production-style data pipeline built to extract Reddit post data, transform it, and visualize insights using various AWS services. The pipeline simulates a real-world scenario by integrating tools for scheduling, processing, storing, and visualizing data at scale.
## 📊 Architecture
Reddit API (via PRAW)
        ↓
Airflow DAG (Scheduled Extract)
        ↓
PostgreSQL (Raw data storage)
        ↓
Airflow + Celery Executor (Task orchestration inside Docker)
        ↓
PySpark Job (Data Transformation)
        ↓
AWS S3 (Raw & Transformed data storage)
        ↓
AWS Glue Job (Further transformation/cleaning)
        ↓
AWS Glue Crawler (Schema discovery, creates Data Catalog tables)
        ↓
AWS Athena (Query data from S3 and validate)
        ↓
Load into AWS Redshift (Native tables)
        ↓
Amazon QuickSight (Visualization & Dashboard)

##  Tech Stack
- **Apache Airflow** – Workflow orchestration
- **Celery** – Distributed task queue
- **PostgreSQL** – Intermediate database
- **AWS S3** – Data lake (raw & transformed storage)
- **AWS Glue** – Data ETL jobs using PySpark
- **AWS Crawler** – Metadata cataloging
- **AWS Athena** – SQL querying on S3
- **Amazon Redshift** – Data warehousing
- **Amazon QuickSight** – Data visualization
- **Docker** – Containerization & environment setup
- **PRAW** (Python Reddit API Wrapper) – Reddit data extraction

## 🔄Workflow Overview
### 1️⃣Reddit Data Extraction
- Reddit posts are extracted using PRAW via a custom Airflow DAG.
- Stored as CSV in local storage.
### 2️⃣Upload to AWS S3
Raw CSV data is uploaded to s3://reddit-pipeline-bejin/raw/.

### 3️⃣AWS Glue ETL
A Glue job processes the CSV data, combines columns, and writes transformed data to s3://reddit-pipeline-bejin/transformed/.

### 4️⃣Crawler & Athena
- AWS Glue Crawler catalogs the transformed data.
- AWS Athena is used for query verification.

### 5️⃣Redshift Integration
Athena data is loaded into Redshift (reddit_namespace → reddit-workgroup) as reddit_data_eng.

### 6️⃣Data Visualization

QuickSight connects to Redshift and visualizes insights such as:
- 📊 Top 10 Reddit Authors by Total Score (Bar Chart)
- 📉 Hourly Average Reddit Score Trend (Line Chart)
- 📈 Distribution of Reddit Post Scores (Histogram)
- 🥧 NSFW Status of Reddit Posts (Pie Chart – All SFW Content)

### 7️⃣Docker Setup for Local Development
To run the Airflow DAGs locally:
```
docker-compose up --build
```
Access the Airflow UI at:
```
 http://localhost:8081
```









