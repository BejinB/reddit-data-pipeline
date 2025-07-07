import pandas as pd
import logging

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    logging.info("🔌 Connecting to Reddit...")
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    logging.info(f"⬇️ Extracting posts from r/{subreddit}...")
    posts = extract_posts(instance, subreddit, time_filter, limit)
    if not posts:
        raise ValueError("❌ No posts were fetched from Reddit!")

    logging.info(f"🧾 Transforming {len(posts)} posts...")
    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)

    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    logging.info(f"💾 Saving data to {file_path}...")
    load_data_to_csv(post_df, file_path)

    logging.info("✅ Reddit pipeline completed successfully.")
    return file_path
