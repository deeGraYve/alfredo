Alfredo - Born to serve!
************************


Alfredo is a simple, extensible gtalk bot. It's cabaple of doing any kind of tasks, implemented as separated commands.

Here is a typical session: ::

    you: inv some text
    alfredo: called inv some text -> txet emos
    

Implementing a new command
**************************

Commands are implemented as Plugins (se more at `plugnplay <https://github.com/daltonmatos/plugnplay>_`). Just create a new class:

    from alfredo import Plugin, ICommand

    class SomeCommand(Plugin):
      implements = [ICommand]

      def match_name(self, command):
        return 'mycommand' == command

      def run(self, user, *args)
        # process some logic
        return result


In this case we create a new command named 'mycommand'. If we send this message to alfredo:

   mycommand p1 p2 p3


the ``run()`` method would be called like this: ``run('user@domain.com', 'p1', 'p2', 'p3')``. This method must return a string, that will be sent back to the original user.

