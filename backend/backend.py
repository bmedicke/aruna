#!/usr/bin/env python

import board
import neopixel
import psycopg

user = "postgres"
password = "postgres"
hostname = "localhost"
dbname = "postgres"

uri = f"postgresql://{user}:{password}@{hostname}/{dbname}"

sql_query = """
SELECT table_schema || '.' || table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_schema NOT IN ('pg_catalog', 'information_schema');
"""

with psycopg.connect(uri) as connection:
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        for record in cursor.fetchall():
            print(record)
