#!/bin/python
# -*- coding: utf-8 -*-			#To enable non ascii cherecters

import cmd, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class GetInfoShell(cmd.Cmd):
    intro = 'Welcome to the ESH4D shell.   Type help or ? to list commands.\n'
    intro += "▭▭▭▭▭▭▭▭▭▭▭▭ ▭▭▭▭▭▭▭▭▭▭▭▭▭▭ ▭▭▭▭▭▭▭▭▭▭▭▭▭ ▭▭▭▭▭▭▭▭▭▭▭▭▭"
    prompt = '(target) '
    file = None

# ----- basic script commands -----

    def do_add(self, arg):
        'Return ESH4D to the home position:  HOME'


def main():
	header = "▁▁▁▁▁▁▁▁▁▁▁▁▁ TARGET LIST ▁▁▁▁▁▁▁▁▁▁▁▁▁ ";
	print(bcolors.HEADER + header)
	GetInfoShell().cmdloop();


if __name__ == "__main__":
    main()
