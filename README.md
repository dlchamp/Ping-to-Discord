# Ping-to-Discord

A simple python script to ping a target host (up to 3 retries) and send any status change to a Discord webhook


### Dependencies

* Built on [Python3 - 3.9.7](https://www.python.org/downloads/)
* see requirements.txt for Python dependencies


## Configuring the script
Configuration is pretty straight forward.  Follow these steps to get all of the required, and optional,
data that will be needed to get this script working perfectly.

Take one of the examples in `config.json.example` that will fit your use case and apply it to the included empty config.json

### Discord webhooks
1. Head into your Discord server where you have permissions to configure channel integrations, or webhooks.
2. Right click on the channel you wish for this webhook to post messages to
3. Click Edit channel
4. Navigate to the **Integrations** tab
5. **Create Webhook**
6. Give your new webhook a name and optional icon
7. Click **Copy Webhook Url** - you'll need this for the config file

You can find more information on webhooks here - ([Discord.com](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks))

### Selecting the target host
This script is designed to simply ping a target host.  This means that any site or direct IP address should work.
You could use 'google.com' or '8.8.8.8'
No http:// or https:// necessary

### Adding an optional "Mention" role or member
Adding this will simply @mention a role, or even target member of your choice when the webhook is sent to the channel.
You can also add more than one role, member, or a mixture of the two.
Just put them in a list - Example `["<@&12345678987654>", "<@&12345678987456>", "<@1234567898746>"]`


**Get the target role**
1. Go into a channel and type out "@role" - role being whatever your role's name is.
2. Don't send it, but move your cursor to before the @ symbol and type in a \.  Now send it.
3. This will automatically change the output in the channel message to something like <@&12345678987654>


**Get the target member**
*Discord development mode must be enabled* - [See here for instructions](https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/)
1. Right-click on the target member and click "Copy ID" from the bottom of the context menu
2. In the config.json add "<@memberid>" where member ID is the copied ID.
Should look like `<@173105961442082816>`



## Version History

* 1.1
    * Updated the readme to include configuration and setup information
    * Added a retry to failed ping - now will try up to 3 times if first attemped failed before reporting the status (if change) to Discord webhook
    * Added ability to mention 1 or more members/roles
    * Added config examples in config.json.sample

* 1.0
    * Initial commit.
