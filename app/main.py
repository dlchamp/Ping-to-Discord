import os
import logging
from functions import *

"""
###########################  USER CONFIGURATION  ###########################
How to get your webhook url - https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks
Paste your discord webhook channel URLs into the two variables below
If you wish for there to only be one channel for both server status and game news (patch notes),
make leave news_webhook_url = server_status_webhook_url
"""
webhook_url = "webhook-url"

"""
Assign a mention role, if you wish - Get your ID by typing \@role-you-wish-to-mention.  Copy the full ID (ex: <@&8997895432165879>)
and paste between the ''.  If you don't wish to have a role, just replace 'role-mention-id' with None (ex: mention_role = None)
"""
target_host = "google.com"  # Add your domain or IP, must be wrapped in ' '
# Mention role id '<@&1234567899876>' or use None (no quotes)
mention_role = None

###################### END OF USER CONFIGURABLE AREA   ######################


logging.basicConfig(format="%(message)s", level="INFO")
log = logging.getLogger("root)")

# Create ping.txt if not exits
if not os.path.exists("./ping.txt"):
    with open("./ping.txt", "w"):
        pass


# Get old status from txt file.
old_status = get_last_response()
if old_status == "":
    status = None

# Ping the target host and get response
response = ping(target_host)

if response == "1" and old_status == "1":
    pass

elif response == "1" and old_status == "0":
    log.info(f"{target_host} status has been updated: ✅ - Sending to Discord...")
    message = "✅ - The server is back online!"
    send_webhook(webhook_url, response, message, mention_role)
    update_status(response)

elif response == "0" and old_status == "0":
    pass

elif response == "0" and old_status == "1":
    log.info(f"{target_host} status has been updated: ❌ - Sending to Discord...")
    message = "❌ - The server has gone offline"
    send_webhook(webhook_url, response, message, mention_role)
    update_status(response)

else:
    update_status(response)
