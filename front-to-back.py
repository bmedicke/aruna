#!/usr/bin/env python

import psycopg

user = "postgres"
password = "postgres"
hostname = "localhost"
dbname = "postgres"

uri = f"postgresql://{user}:{password}@{hostname}/{dbname}"

sql_query = """
SELECT *
FROM information_schema.tables
WHERE table_schema NOT IN ('pg_catalog', 'information_schema');
"""

with psycopg.connect(uri) as connection:
    with connection.cursor() as cursor:
        for record in cursor.execute(sql_query).fetchall():
            print(record)
