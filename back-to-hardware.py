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
SELECT *
FROM information_schema.tables
WHERE table_schema NOT IN ('pg_catalog', 'information_schema');
"""

with psycopg.connect(uri) as connection:
    with connection.cursor() as cursor:
        for record in cursor.execute(sql_query).fetchall():
            print(record)




led_pin = board.D18
num_pixels = 300
pixels = neopixel.NeoPixel(led_pin, num_pixels, brightness=1, auto_write=True)

for i,_ in enumerate(pixels):
    pixels[i] = (0,255,0)
