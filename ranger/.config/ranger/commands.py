from ranger.api.commands import *

class empty(Command):
    """:empty

    Empties the trash directory ~/.Trash
    """

    def execute(self):
        self.fm.run("rm -rf /home/habitzreuter/.local/share/Trash/files/{*,.[^.]*}")
