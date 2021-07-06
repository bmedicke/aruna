#!/usr/bin/env python3

import board
import neopixel
import psycopg2
import realtime_py

server = "192.168.0.114"
url = f"ws://{server}:8000"
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXBhYmFzZSIsImlhdCI6MTYwMzk2ODgzNCwiZXhwIjoyNTUwNjUzNjM0LCJyb2xlIjoiYW5vbiJ9.36fUebxgx1mcBo4s19v0SzqmzunP--hm_hep0uLX0ew"

led_pin = board.D18
num_pixels = 300
pixels = neopixel.NeoPixel(led_pin, num_pixels, brightness=1, auto_write=False)


def check_id(id):
    if not id in range(num_pixels):
        print(
            f"error: pixel {id} out of range (valid range is from 0 to {num_pixels-1})"
        )
        return False
    return True


def check_colors(colors):
    for color in colors:
        if color not in range(0, 256):
            print(
                f"error: wrong color value {color} (valid range is from 0 to 255)"
            )
            return False
    return True


def restore_last_state():
    conn = psycopg2.connect(
        host=server,
        database="postgres",
        user="postgres",
        password="postgres",
    )
    cur = conn.cursor()

    sql = "select * from pixels order by id"
    cur.execute(sql)

    pixels.auto_write = False

    for pixel in cur.fetchall():
        id = pixel[0]
        colors = (pixel[1], pixel[2], pixel[3])

        if check_id(id) and check_colors(colors):
            pixels[id] = colors

    pixels.show()
    pixels.auto_write = True


def on_change(payload):
    table = payload["table"]

    if table == "pixels":
        pixel = payload["record"]
        id = int(pixel["id"])
        colors = (int(pixel["red"]), int(pixel["green"]), int(pixel["blue"]))

        if not check_id(id):
            return

        if not check_colors(colors):
            return

        pixels[id] = colors
        print(f"pixel {id} changed to: {colors}")


def on_delete(payload):
    table = payload["table"]

    if table == "pixels":
        id = int(payload["old_record"]["id"])

        print(f"pixel {id} deleted, setting to (0, 0, 0)")

        if check_id(id):
            pixels[id] = (0, 0, 0)


if __name__ == "__main__":
    restore_last_state()

    URL = f"{url}/realtime/v1/websocket?apikey={key}&vsn=1.0.0"
    s = realtime_py.connection.Socket(URL)
    s.connect()

    channel = s.set_channel("realtime:*")
    channel.join().on("UPDATE", on_change)
    channel.join().on("INSERT", on_change)
    channel.join().on("DELETE", on_delete)
    s.listen()
