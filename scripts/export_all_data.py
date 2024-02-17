import argparse, psycopg2, os
import pandas as pd

from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(description='Export data from a PostgreSQL database')
    parser.add_argument('table', type=str, help='Table name')
    parser.add_argument('output', type=str, help='Output file name')
    args = parser.parse_args()

    conn = psycopg2.connect(host=os.getenv('PGHOST'), database=os.getenv('PGDATABASE'), user=os.getenv('PGUSER'), password=os.getenv('PGPASSWORD'))
    query = f'SELECT * FROM {args.table}'
    df = pd.read_sql(query, conn)
    df.to_csv(f"./data/{args.output}", index=False)
    conn.close()