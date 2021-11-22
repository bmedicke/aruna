#!/usr/bin/env python

import board
import neopixel
import psycopg

sql_query = """
SELECT table_schema || '.' || table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_schema NOT IN ('pg_catalog', 'information_schema');
"""

with psycopg.connect(
    "postgresql://postgres:postgres@localhost/postgres"
) as connection:

    cursor = connection.cursor()
    cursor.execute(sql_query)

    for result in cursor.fetchall():
        print(result)
