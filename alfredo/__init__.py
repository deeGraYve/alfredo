#encoding: utf-8

import sys
from PyGtalkRobot import GtalkRobot

import plugnplay
import base64


__all__ = ['ICommand']

Plugin = plugnplay.Plugin


class ICommand(plugnplay.Interface):

  '''
   Returns true if the command name passed as a paramater
   matches the command implemented by this interface
  '''
  def match_name(self, command):
    pass

  '''
   Run the specific command. Returns a string.
   Receives the username of the sender and any parameters
   passed on the message, eg:

    sender: process arg0 arg1 arg2

   would be translated to: run(sender, 'process', arg0, arg1, arg2)
  '''
  def run(self, user, command, *args):
    pass

class InvertCommand(Plugin):
  implements = [ICommand]


  def match_name(self, command):
    return 'inv' == command

  def run(self, user, *args):
    if len(args) == 0:
      return "inv command needs at least one argument"
    return " ".join(s[::-1] for s in args[::-1])

class Base64Command(Plugin):

  implements = [ICommand]

  def match_name(self, command):
    return command in ('b64e', 'b64d')

  def run(self, user, command=None, *data):
    if len(data) == 0:
      return "{0} command needs one argument".format(command)
    return getattr(self, "_{0}".format(command))(data[0])


  def _b64e(self, data):
    return base64.b64encode(data)

  def _b64d(self, data):
    return base64.b64decode(data)




