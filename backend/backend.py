#!/usr/bin/env python3

import board
import datetime
import json
import neopixel
import realtime_py

server = "192.168.0.114"
url = f"ws://{server}:8000"
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXBhYmFzZSIsImlhdCI6MTYwMzk2ODgzNCwiZXhwIjoyNTUwNjUzNjM0LCJyb2xlIjoiYW5vbiJ9.36fUebxgx1mcBo4s19v0SzqmzunP--hm_hep0uLX0ew"

led_pin = board.D18
num_pixels = 300
pixels = neopixel.NeoPixel(led_pin, num_pixels, brightness=1, auto_write=True)


def on_update(payload):
    table = payload["table"]

    if table == "pixels":
        pixel = payload["record"]
        id = int(pixel["id"])
        r = int(pixel["red"])
        g = int(pixel["green"])
        b = int(pixel["blue"])

        if not id < num_pixels:
            print(f"error: pixel {id} out of range (max. is {num_pixels-1})")
            return

        for color in (r, g, b):
            if color not in range(0, 256):
                print(f"error: wrong color value '{color}', in {(r, g, b)}")
                return

        pixels[id] = (r, g, b)
        print(f"pixel {id} changed to: {r, g, b}")
    else:
        print(f'table "{table}" not handled')


URL = f"{url}/realtime/v1/websocket?apikey={key}&vsn=1.0.0"
s = realtime_py.connection.Socket(URL)
s.connect()

channel_1 = s.set_channel("realtime:*")
channel_1.join().on("UPDATE", on_update)
s.listen()
