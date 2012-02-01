import plugnplay
from alfredo.PyGtalkRobot import GtalkRobot

plugnplay.set_plugin_dirs('commands')
plugnplay.load_plugins()

bot = GtalkRobot()
bot.start('your_gmail_account', 'your_password')