#!/usr/bin/env python3

import board
import neopixel
import realtime_py

server = "192.168.0.114"
url = f"ws://{server}:8000"
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXBhYmFzZSIsImlhdCI6MTYwMzk2ODgzNCwiZXhwIjoyNTUwNjUzNjM0LCJyb2xlIjoiYW5vbiJ9.36fUebxgx1mcBo4s19v0SzqmzunP--hm_hep0uLX0ew"

led_pin = board.D18
num_pixels = 300
pixels = neopixel.NeoPixel(led_pin, num_pixels, brightness=1, auto_write=True)


def on_change(payload):
    table = payload["table"]

    if table == "pixels":
        pixel = payload["record"]
        id = int(pixel["id"])
        colors = (int(pixel["red"]), int(pixel["green"]), int(pixel["blue"]))

        if not id in range(num_pixels):
            print(
                f"error: pixel {id} out of range (valid range is from 0 to {num_pixels-1})"
            )
            return

        for color in colors:
            if color not in range(0, 256):
                print(
                    f"error: wrong color value {color} (valid range is from 0 to 255)"
                )
                return

        pixels[id] = colors
        print(f"pixel {id} changed to: {colors}")
    else:
        print(f'table "{table}" not handled')


def on_delete(payload):
    id = int(payload["old_record"]["id"])
    print(f"pixel {id} deleted, setting to (0, 0, 0)")
    pixels[id] = (0, 0, 0)


URL = f"{url}/realtime/v1/websocket?apikey={key}&vsn=1.0.0"
s = realtime_py.connection.Socket(URL)
s.connect()

channel = s.set_channel("realtime:*")
channel.join().on("UPDATE", on_change)
channel.join().on("INSERT", on_change)
channel.join().on("DELETE", on_delete)
s.listen()
