
class Base64Command(Plugin):

  implements = [ICommand]
  SHORTHELP = 'b64d/b64e Decode/Encode form/to Base64'
  LONGHELP = 'b64d decodes from Base64, b64e Encodes to base64'

  def name(self):
    return 'b64e/b64d'

  def help(self):
    return (self.SHORTHELP, self.LONGHELP)

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
