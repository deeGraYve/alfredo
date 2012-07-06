#-*- coding: utf-8 -*-
import alfredo

from random import choice

CONTACTS = ["buddy@example.com"]
CONTACTS_NAME = {"buddy@example.com": "Fulano"}

class CafezinhoCommand(alfredo.Plugin):

  implements = [alfredo.ICommand,]
  SHORTHELP = 'Pede pra alguem fazer um cafezinho no escritório'

  def help(self):
    return (self.SHORTHELP, self.SHORTHELP)

  def name(self):
    return 'cafezinho'

  def match_name(self, command):
    return "cafe" in command

  def run(self, user, command, *data):
    if len(data) == 0:
      return {"message": "{0} precisa de um contato válido".format(command)}

    chosen = choice(CONTACTS)
    return {"message": "{0} vai fazer um cafezinho".format(CONTACTS_NAME[chosen]), "otherUser": "{0}".format(chosen), "otherMessage": "faz cafe ai"}
