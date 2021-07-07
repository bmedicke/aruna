#!/usr/bin/env python3

import board
import neopixel
import psycopg2
import time

server = "localhost"

led_pin = board.D18
num_pixels = 300
pixels = neopixel.NeoPixel(led_pin, num_pixels, brightness=1, auto_write=False)
old_state = list()


def id_ok(id):
    if not id in range(num_pixels):
        print(
            f"error: pixel {id} out of range (valid range is from 0 to {num_pixels-1})"
        )
        return False
    return True


def colors_ok(colors):
    for color in colors:
        if color not in range(0, 256):
            print(
                f"error: wrong color value {color} (valid range is from 0 to 255)"
            )
            return False
    return True


def update_leds(cursor):
    global old_state

    cursor.execute("select * from pixels")
    state = cursor.fetchall()

    if state != old_state:
        for pixel in state:
            id = pixel[0]
            colors = (pixel[1], pixel[2], pixel[3])

            if id_ok(id) and colors_ok(colors):
                pixels[id] = colors

        pixels.show()

    old_state = state


def connect():
    print("connecting")
    connection = psycopg2.connect(
        host=server,
        database="postgres",
        user="postgres",
        password="postgres",
    )
    return connection


def main():
    # connection-loop:
    while True:
        try:
            cursor = connect().cursor()
            print("connected")
            break
        except psycopg2.OperationalError:
            print("error: connection failed. retrying...")
            time.sleep(2)
        except Exception as e:
            print("[connection-loop] unhandled error:", e)

    # polling-loop:
    while True:
        try:
            update_leds(cursor)
            time.sleep(0.5)
        except Exception as e:
            print("[update-loop]  unhandled error:", e)
            break  # back to the connection-loop.


if __name__ == "__main__":
    while True:
        main()
