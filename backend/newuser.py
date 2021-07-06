#!/usr/bin/env python

import json
import random
import string
import supabase_py

url = "http://localhost:8000"
key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJzdXBhYmFzZSIsImlhdCI6MTYwMzk2ODgzNCwiZXhwIjoyNTUwNjUzNjM0LCJyb2xlIjoiYW5vbiJ9.36fUebxgx1mcBo4s19v0SzqmzunP--hm_hep0uLX0ew"
supabase = supabase_py.create_client(url, key)


def randstring():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(6))


random_email = randstring() + "@random.mail"
random_password = randstring()

user = supabase.auth.sign_up(email=random_email, password=random_password)
print(json.dumps(user, indent=4, sort_keys=True))  # pretty print dict.
