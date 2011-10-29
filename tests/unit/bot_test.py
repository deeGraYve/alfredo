

import unittest


from alfredo.PyGtalkRobot import GtalkRobot

from mock import patch, Mock

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
      message = Mock()
      message.getBody = Mock(return_value="somecommand arg0 arg1")
      message.getFrom = Mock(return_value="user@domain.com")

      self.bot._processMessage(Mock(), message)
      self.bot._replyMessage.assert_called_with('user@domain.com', "somecommand is not a valid command. Try help to know more")

