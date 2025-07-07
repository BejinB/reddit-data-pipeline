from etls.aws_etl import connect_to_s3, upload_to_s3
from utils.constants import AWS_BUCKET_NAME
import os

def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids='reddit_extraction', key='return_value')
    
    print(f"📄 File path received from XCom: {file_path}")
    print(f"📂 Checking if file exists: {os.path.exists(file_path)}")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File does not exist at path: {file_path}")

    s3 = connect_to_s3()
    print("✅ Connected to S3")

    # ❌ REMOVE this line — you don't have create permission
    # create_bucket_if_not_exist(s3, AWS_BUCKET_NAME)

    s3_file_name = os.path.basename(file_path)
    upload_to_s3(s3, file_path, AWS_BUCKET_NAME, s3_file_name)
    print("✅ File uploaded successfully")
