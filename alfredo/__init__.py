#encoding: utf-8

import sys
from PyGtalkRobot import GtalkRobot

import plugnplay
import base64

__all__ = ['ICommand', 'InvertCommand', 'Base64Command', 'HelpCommand', 'Plugin']

Plugin = plugnplay.Plugin

class ICommand(plugnplay.Interface):

  '''
   Returns tha command name
  '''
  def name(self):
    pass

  '''
   Returns a tuple (short-help, long-help)
   about the command
  '''
  def help(self):
    pass

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

    
from os.path import realpath
