import pandas as pd
from sqlalchemy import create_engine

def ingest_zones():
    # 1. Connect to the database (using the credentials from your docker-compose.yaml)
    # The host is 'localhost' if running outside the container, or 'pgdatabase' if running inside.
    # We use localhost assuming you are running this from your workspace terminal.
    engine = create_engine('postgresql+psycopg2://root:root@localhost:5432/ny_taxi')

    # 2. Read the CSV file
    # Adjust the path if you run the script from a different location
    csv_path = '../test/taxi_zone_lookup.csv'
    df = pd.read_csv(csv_path)

    # 3. Create the table and insert the data
    # if_exists='replace' will drop the table if it exists and recreate it
    df.to_sql(name='zones', con=engine, if_exists='replace')
    
    print(f"Successfully inserted {len(df)} rows into the 'zones' table!")

if __name__ == "__main__":
    ingest_zones()