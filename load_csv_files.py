# The below code helps you to load csv into your PostgreSQL 
# These are the simple steps that you need to follow
 
import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection details
username = "postgres"
password = "root"
hostname = "localhost"
portnumber = "5432"
database_name = "painting"

# Create the connection string
connection_string = f"postgresql://{username}:{password}@{hostname}:{portnumber}/{database_name}"

# Create the engine
engine = create_engine(connection_string)

# Test the connection
try:
    with engine.connect() as connection:
        print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)

# Corrected file path with double backslashes or raw string literal
df = pd.read_csv(r'C:\SQL Case Study\artist.csv')
df.to_sql('artist',con=connection_string,if_exists='replace',index=False)

df = pd.read_csv(r'C:\SQL Case Study\canvas_size.csv')
df.to_sql('canvas_size',con=connection_string,if_exists='replace',index=False)

df = pd.read_csv(r'C:\SQL Case Study\image_link.csv')
df.to_sql('image_link',con=connection_string,if_exists='replace',index=False)

df = pd.read_csv(r'C:\SQL Case Study\museum_hours.csv')
df.to_sql('museum_hours',con=connection_string,if_exists='replace',index=False)

df = pd.read_csv(r'C:\SQL Case Study\museum.csv')
df.to_sql('museum',con=connection_string,if_exists='replace',index=False)

df = pd.read_csv(r'C:\SQL Case Study\product_size.csv')
df.to_sql('product_size',con=connection_string,if_exists='replace',index=False)

df = pd.read_csv(r'C:\SQL Case Study\subject.csv')
df.to_sql('subject',con=connection_string,if_exists='replace',index=False)

df = pd.read_csv(r'C:\SQL Case Study\work.csv')
df.to_sql('work',con=connection_string,if_exists='replace',index=False)
