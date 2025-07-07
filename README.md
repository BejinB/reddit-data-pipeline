# reddit-data-pipeline

## 🚀End-to-End Reddit Data Pipeline using Apache Airflow, Celery, PostgreSQL and AWS Services(S3, Glue, Crawler, Athena, Redshift & QuickSight)

This project is a fully orchestrated, production-style data pipeline built to extract Reddit post data, transform it, and visualize insights using various AWS services. The pipeline simulates a real-world scenario by integrating tools for scheduling, processing, storing, and visualizing data at scale.
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
