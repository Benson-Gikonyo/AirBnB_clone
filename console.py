#!/usr/bin/env python3
""" Defines HBNBCCommand class"""

import cmd
import os


class HBNBCCommand (cmd.Cmd):
    """ Console class for AirBnb project"""

    def do_quit(self):
        """ quit console"""
        return True

    def do_EOF(self):
        """Quit console"""
        return True

    def emptyline(self):
        """ empty line + ENTER"""
        pass

    prompt = '(hbnb) '


if __name__ == '__main__':
    HBNBCommand().cmdloop()
