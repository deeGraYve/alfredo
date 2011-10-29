

import unittest


from alfredo.PyGtalkRobot import GtalkRobot

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
