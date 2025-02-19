from dotenv import load_dotenv
import os
import toml

# Load environment variables
load_dotenv()
with open("settings.toml", "r")as f: # Load the config file
    config = toml.load(f)

CHECK_OLD_ENTRIES_ENABLED = config["features"]["check_old_entries"]

# Bot information
TOKEN = os.getenv("TOKEN")  # Discord Token. Loads the token from the .env file
BOT_ID = 1218682240947458129  # User id of the bot

# Channel IDs
ASSIGNMENT_CHANNEL = config["channels"]["assignment_channel"] # Channel ID of the assignment channel
CHECKUP_CHANNEL = config["channels"]["checkup_channel"] # Channel ID of Hdydrometer
ONESHOT_CHANNEL = config["channels"]["oneshot_channel"] # Channel ID of the oneshot channel

# Role dictionary
role_dict = config["roles"]
role_dict_reaction = {emojis[0]: role for role, emojis in role_dict.items()}

Hiatus = config["assignments"]["hiatus"]
# Other configurations
COMMAND_PREFIX = '$'
