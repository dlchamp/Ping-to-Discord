import platform
import time
import random
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed


def ping(host):
    """
    Pings the target and returns 1 if up, or 0 if not up
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    for i in range(3):
        # Retry until pass, up to 3 times
        ping_response = subprocess.call(command, stdout=subprocess.DEVNULL)

        if ping_response == 0:
            return "1"
            break
        else:
            # If failed and on last attempt, return 0 (failed)
            if i == 2:
                return "0"
            else:
                # if not last attempt, sleep for random time between 1 and 3 seconds before trying again
                sleep = random.uniform(1, 3)
                time.sleep(sleep)


def update_status(response):
    """
    Updates the simple ping.txt with 1 or 0 for last status
    """
    with open("./ping.txt", "w") as f:
        f.write(response)


def get_last_response():
    """
    Returns the most recent last status for target host
    """
    with open("./ping.txt") as f:
        return f.read()


def send_webhook(webhook_url, response, message, mention_target):
    """
    Sends a simple embed to the target webhook url
    Embed will have a green color of target is online,
    or red if target is not online

    """
    if response == "1":
        status_color = "00cf00"
    else:
        status_color = "ffaa00"

    if isinstance(mention_target, str):
        target = mention_target

    elif isinstance(mention_target, list):
        target = ', '.join(mention_target)
    else:
        target = None

    webhook = DiscordWebhook(
        url=webhook_url, content=target, rate_limit_retry=True)
    embed = DiscordEmbed(title="Server Status",
                         description=f"**{message}**", color=status_color)
    webhook.add_embed(embed)
    webhook.execute()
