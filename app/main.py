import os
import logging
import json
from functions import *


# Get config data from config.json if no config data, print error and exit
with open('./config/config.json') as f:
    config = json.load(f)
if not bool(config):
    print('No configuration data found. Please update config.json with required data.')
    print('Exiting program...')
    exit()


webhook_url = config['webhook_url']
target_host = config['target_host']
mention_target = config['mention_target']

# Check for ping.txt, if not exists, create it
if not os.path.exists("./ping.txt"):
    with open("./ping.txt", "w"):
        pass

logging.basicConfig(format="%(message)s", level="INFO")
log = logging.getLogger("root)")


# Get old status from txt file.
old_status = get_last_response()
if old_status == "":
    status = None

# Ping the target host and get response
response = ping(target_host)

if response == "1" and old_status == "1":
    pass

elif response == "0" and old_status == "0":
    pass

elif response == "1" and old_status == "0":
    log.info(f"{target_host} status has been updated: ✅ - Sending to Discord...")
    message = "✅ - The server is back online!"
    send_webhook(webhook_url, response, message, mention_target)
    update_status(response)

elif response == "0" and old_status == "1":
    log.info(f"{target_host} status has been updated: ❌ - Sending to Discord...")
    message = "❌ - The server has gone offline"
    send_webhook(webhook_url, response, message, mention_target)
    update_status(response)

else:
    update_status(response)
