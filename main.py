import random
from misskey import Misskey
import os
import time

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

max = random.randint(2, 5)
post_text = ""
for i in range (max):
    post_text = post_text + random.choice(alphabet_list)

print(post_text)
while True:
    try:
        # Misskey
        misskey_address = os.environ.get("MISSKEY_SERVER_ADDRESS")
        misskey_token = os.environ.get("MISSKEY_TOKEN")
        api = Misskey(misskey_address)
        api.token = misskey_token
        api.notes_create(text=post_text)
    except:
        time.sleep(300)
    else:
        break
