#!/usr/bin/env python

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
)
cur = conn.cursor()

sql = "update pixels set red=0, green=0, blue=0"
cur.execute(sql)
conn.commit()
