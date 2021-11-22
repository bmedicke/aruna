#!/usr/bin/env python

import psycopg2
import random
import time


def update_pixel(conn, cur, id, color):
    sql = f"update pixels set red={color[0]}, green={color[1]}, blue={color[2]} where id = {id}"
    cur.execute(sql)
    conn.commit()


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres",
)
cur = conn.cursor()

max_brightness = 10
num_pixels = 300

while True:
    id = random.randint(0, num_pixels)
    colors = (
        random.randint(0, max_brightness),
        random.randint(0, max_brightness),
        random.randint(0, max_brightness),
    )
    update_pixel(conn, cur, id, colors)
    time.sleep(1)
