import pandas as pd
import sqlite3
import os
from dotenv import load_dotenv
load_dotenv()

# Path to local yelp datasets. 
# Data Source: https://www.yelp.com/dataset

tip_path= 'data\yelp_academic_dataset_tip.json'
user_path= 'data\yelp_academic_dataset_user.json'
checkin_path = 'data\yelp_academic_dataset_checkin.json'
business_path = 'data\yelp_academic_dataset_business.json'
review_path = 'data\yelp_academic_dataset_review.json'

# Read the json file into pandas dataframe to load into the database. 

df_tips = pd.read_json(tip_path, lines=True)
df_tips = df_tips.rename(columns={
    "user_id": "user_id",
    "business_id": "business_id",
    "text": "review_text",
    "date": "review_date",
    "compliment_count": "compliment_count"
})

db_path = os.getenv('db_path')

# Create the database schema using sql migration script. 

def apply_migration_script(db_path, script_path):
    with sqlite3.connect(db_path) as conn:
        with open(script_path, 'r') as f:
            script = f.read()
        conn.executescript(script)
        conn.commit()

script_path = 'db_migrations\create_table._0001up.sql'
apply_migration_script(db_path, script_path)

conn = sqlite3.connect(db_path)
df_tips.to_sql('tips', con=conn, if_exists='append', index=False)