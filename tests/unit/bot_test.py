

import unittest


from alfredo.PyGtalkRobot import GtalkRobot
from alfredo import Plugin, ICommand

from mock import patch, Mock

import plugnplay


class PrintCommand(Plugin):
  implements = [ICommand]

  def match_name(self, command):
    return command == 'print'

  def run(self, user, command, *args):
    if len(args) < 1:
      return "one arg required"
    return "{0} {1}".format(*args)


def _mock_message(user, body):
  message = Mock()
  message.getBody = Mock(return_value=body)
  message.getFrom = Mock(return_value=user)
  return message

class BotTest(unittest.TestCase):


  def setUp(self):
    self.bot = GtalkRobot()

  '''
   Should parse the original message:
    "inv arg0 agr1" becomes ('inv', ('arg0, 'arg1))
  '''
  def test_parse_message_more_than_one_argument(self):
    self.assertEquals(('inv', ('arg0', 'arg1')), self.bot._parse_message('inv arg0 arg1') )
  
  def test_parse_message_more_one_argument(self):
    self.assertEquals(('inv', ('arg0',)), self.bot._parse_message('inv arg0') )

  def test_parse_message_more_no_arguments(self):
    self.assertEquals(('inv', ()), self.bot._parse_message('inv') )
    self.assertEquals(('inv', ()), self.bot._parse_message('inv  ') )

  '''
   Alfredo mystr return "command not found" when it does not
   find a command implementor
  '''
  def test_command_not_found(self):
    with patch.object(GtalkRobot, '_replyMessage'):
      message = _mock_message('user@domain.com', 'somecommand arg0 arg1')

      self.bot._processMessage(Mock(), message)
      self.bot._replyMessage.assert_called_with('user@domain.com', "somecommand is not a valid command. Try help to know more")

  def test_call_command(self):
    class EchoCommand(Plugin):
      implements = [ICommand]

      def match_name(self, command):
        return 'echo' == command

      def run(self, user, command, *args):
        pass

    with patch.object(ICommand, 'implementors'):
      echo = Mock()
      echo.match_name.return_value = True
      ICommand.implementors.return_value = [echo]
      self.bot.conn = Mock()
      self.bot._processMessage(Mock(), _mock_message('user@domain', 'echo arg0 arg1'))
      echo.run.assert_called_with('user@domain', 'echo', 'arg0', 'arg1')

  def test_reply_command_output_to_user(self):
    with patch.object(GtalkRobot, '_replyMessage'):
      message = _mock_message('user@domain.com', 'print arg0 arg1')

      self.bot._processMessage(Mock(), message)
      self.bot._replyMessage.assert_called_with('user@domain.com', "arg0 arg1")

  def test_call_command_zero_arguments(self):
    with patch.object(GtalkRobot, '_replyMessage'):
      message = _mock_message('user@domain.com', 'print')

      self.bot._processMessage(Mock(), message)
      self.bot._replyMessage.assert_called_with('user@domain.com', "one arg required")

  def test_call_command_raise_exception(self):
     with patch.object(ICommand, 'implementors'):
       with patch.object(GtalkRobot, '_replyMessage'):
          echo = Mock()
          echo.match_name.return_value = True
          echo.run.side_effect = Exception("Boom")
          ICommand.implementors.return_value = [echo]
          self.bot.conn = Mock()
          self.bot._processMessage(Mock(), _mock_message('user@domain', 'echo arg0 arg1'))
          self.bot._replyMessage.assert_called_with('user@domain', 'Error running command: echo arg0 arg1')
