#!/usr/bin/env python

import psycopg2


def fetch_pixels(cursor):
    cur.execute("select * from pixels")
    return cur.fetchall()


def create_entries(cursor, connection, num_pixels=300):
    for id in range(num_pixels):
        sql = f"insert into pixels(id, red, green, blue) values({id}, 10, 10, 10) on conflict do nothing"
        cursor.execute(sql)
        connection.commit()


if __name__ == "__main__":
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres",
    )
    cur = conn.cursor()
    create_entries(cur, conn)
    for pixel in fetch_pixels(cur):
        print(pixel)
