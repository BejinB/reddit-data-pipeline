import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import concat_ws
from awsglue import DynamicFrame

# Get job args
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Spark & Glue context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Initialize job
job.init(args['JOB_NAME'], args)

# 📥 Read from S3 (raw)
input_dynamic_frame = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": ["s3://reddit-pipeline-bejin/raw/reddit_20250705.csv"],
        "recurse": True
    },
    transformation_ctx="input_dynamic_frame"
)

# Convert to DataFrame
df = input_dynamic_frame.toDF()

# 🧠 Combine edited, spoiler, stickied into ESS_updated
df_combined = df.withColumn(
    "ESS_updated",
    concat_ws("-", df["edited"], df["spoiler"], df["stickied"])
).drop("edited", "spoiler", "stickied")

# Convert back to DynamicFrame
output_dynamic_frame = DynamicFrame.fromDF(df_combined, glueContext, "output_dynamic_frame")

# 📤 Write to S3 (transformed)
glueContext.write_dynamic_frame.from_options(
    frame=output_dynamic_frame,
    connection_type="s3",
    format="csv",
    connection_options={
        "path": "s3://reddit-pipeline-bejin/transformed/",
        "partitionKeys": []
    },
    transformation_ctx="output_to_s3"
)

# ✅ Commit job
job.commit()
