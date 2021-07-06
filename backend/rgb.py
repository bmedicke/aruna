#!/usr/bin/env python

import psycopg2
import time


def update_pixel(id, color):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres",
    )
    cur = conn.cursor()

    sql = f'update pixels set red={color[0]}, green={color[1]}, blue={color[2]} where id = {id}'
    cur.execute(sql)
    conn.commit()

for i in range(300):
    if i % 3 == 0:
        update_pixel(i, (20, 0, 0))
    elif i % 3 == 1:
        update_pixel(i, (0, 20, 0))
    else:
        update_pixel(i, (0, 0, 20))
