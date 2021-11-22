#!/usr/bin/env python

import board
import neopixel
import psycopg

user = "postgres"
password = "postgres"
hostname = "localhost"
dbname = "postgres"

uri = f"postgresql://{user}:{password}@{hostname}/{dbname}"

with psycopg.connect(uri, autocommit=True) as connection:
    with connection.cursor() as cursor:
        cursor.execute("LISTEN table_changed")

        gen = connection.notifies()
        for notify in gen:
            print(notify)
