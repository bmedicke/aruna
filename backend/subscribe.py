#!/usr/bin/env python

import datetime
import json
import realtime_py

url = "ws://localhost:8000"
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXBhYmFzZSIsImlhdCI6MTYwMzk2ODgzNCwiZXhwIjoyNTUwNjUzNjM0LCJyb2xlIjoiYW5vbiJ9.36fUebxgx1mcBo4s19v0SzqmzunP--hm_hep0uLX0ew"


def on_update(payload):
    print(datetime.datetime.now(), "on_update")
    print(json.dumps(payload['record'], indent=4, sort_keys=True))
    print(''.join('#' for _ in range(30)))


URL = f"{url}/realtime/v1/websocket?apikey={key}&vsn=1.0.0"
s = realtime_py.connection.Socket(URL)
s.connect()

channel_1 = s.set_channel("realtime:*")
channel_1.join().on("UPDATE", on_update)
s.listen()
