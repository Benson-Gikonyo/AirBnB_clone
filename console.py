#!/usr/bin/env python3
""" Defines HBNBCCommand class"""

import cmd
import os


class HBNBCommand(cmd.Cmd):
    """ Console class for AirBnb project"""
    
    prompt = "(hbnb)"

    def do_quit(self, line):
        """ quit console"""
        return True

    def do_EOF(self, line):
        """Quit console"""
        return True

    def emptyline(self):
        """ empty line + ENTER"""
        print()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
