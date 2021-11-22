#!/usr/bin/env python

import board
import neopixel
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
)

sql = """
SELECT table_schema || '.' || table_name
FROM information_schema.tables
WHERE table_type = 'BASE TABLE'
AND table_schema NOT IN ('pg_catalog', 'information_schema');
"""

cur = conn.cursor()
cur.execute(sql)

for result in cur.fetchall():
    print(result)
