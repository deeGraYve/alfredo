import plugnplay
from alfredo.PyGtalkRobot import GtalkRobot

try:
    from bot_config import gmail_account, gmail_pass
except:
    gmail_account = 'your_gmail_account'
    gmail_pass = 'your_password'

plugnplay.set_plugin_dirs('commands')
plugnplay.load_plugins()

bot = GtalkRobot()
bot.start(gmail_account, gmail_pass)