


import unittest

from alfredo import *

class InvertCommandTest(unittest.TestCase):

  def setUp(self):
    self.inv = InvertCommand()

  def test_check_name_matches(self):
    self.assertTrue(self.inv.match_name('inv'))

  def test_check_parameter_presence(self):
    self.assertEquals("inv command needs at least one argument", self.inv.run('daltonmatos@gmail.com', 'inv'))

  def test_invert_one_argument(self):
    self.assertEquals("oderfla", self.inv.run('user@domain.com', 'inv', 'alfredo'))

  def test_invert_two_arguments(self):
    self.assertEquals("reltub oderfla", self.inv.run('user', 'inv', 'alfredo', 'butler'))



class Base64EncodeTest(unittest.TestCase):

  def setUp(self):
    self.b64e = Base64Command()

  def test_check_name_maches(self):
    self.assertTrue(self.b64e.match_name('b64e'))

  def test_check_parameter_presence(self):
    self.assertEquals("b64e command needs one argument", self.b64e.run('user', 'b64e'))

  def test_encode(self):
    self.assertEquals("YWxmcmVkbyBidXRsZXI=", self.b64e.run('user', 'b64e', 'alfredo butler'))


class Base64DecodeTest(unittest.TestCase):

  def setUp(self):
    self.b64d = Base64Command()

  def test_check_name_maches(self):
    self.assertTrue(self.b64d.match_name('b64d'))

  def test_check_parameter_presence(self):
    self.assertEquals("b64d command needs one argument", self.b64d.run('user', 'b64d'))

  def test_encode(self):
    self.assertEquals("alfredo butler", self.b64d.run('user', 'b64d', 'YWxmcmVkbyBidXRsZXI='))

