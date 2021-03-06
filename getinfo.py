#!/bin/python2
# -*- coding: utf-8 -*-			#To enable non ascii cherecters

import cmd, sys, os
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#------------- partial commands-----------------
#------------------------ DB Connection ---------
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn   
#----------------------------------

#------------ Insert sqlite --------------
def insert(info):
    cnn = create_connection("getinfo.db");

#------------------------------------------

def head():
    header = "▁▁▁▁▁▁▁▁▁▁▁▁▁ TARGET LIST ▁▁▁▁▁▁▁▁▁▁▁▁▁ \n";
    intro = 'Welcome to the ESH4D shell.   Type help or ? to list commands.\n'
    intro += "▭▭▭▭▭▭▭▭▭▭▭▭ ▭▭▭▭▭▭▭▭▭▭▭▭▭▭ ▭▭▭▭▭▭▭▭▭▭▭▭▭ ▭▭▭▭▭▭▭▭▭▭▭▭▭"
    print(bcolors.HEADER + header);
    print (bcolors.HEADER + intro);

def add():
    print (bcolors.BOLD + "******** Person Details **************\n");
    print (bcolors.UNDERLINE);
    name = raw_input("?Name: ");
    names = name.split()
    
    try:
        firstname = names[0];
        lastname= names[1];
    except:
        if (len(names) <= 1):
            lastname = 'NULL';

    gender = raw_input("?Gender: ");
    dob = raw_input("?Date: ");
    marital_status = raw_input("?Un/Married: ");
    child = raw_input("?Kid(Number): ");
    mobile = raw_input("?Mobile: ");
    email = raw_input("?Email: ");
    present_address = raw_input("?Present Address: ");
    permanent_address = raw_input("?Permanent Address: ");


    mother = raw_input("?Mother: ");
    father = raw_input("?Father: ");
    sibling = raw_input("?Siblings(number): ");
    
    
    os.system('clear');
   
    head();
#-----------------------------------------------

class GetInfoShell(cmd.Cmd):
    intro = 'Welcome to the ESH4D shell.   Type help or ? to list commands.\n'
    intro += "▭▭▭▭▭▭▭▭▭▭▭▭ ▭▭▭▭▭▭▭▭▭▭▭▭▭▭ ▭▭▭▭▭▭▭▭▭▭▭▭▭ ▭▭▭▭▭▭▭▭▭▭▭▭▭"
    prompt = '(target) '
    file = None
    
# ----- basic script commands -----

    def do_add(self, arg):
        'Return ESH4D to the home position:  HOME'
        add();

  
    def do_find(self, arg):
        'Return ESH4D to the home position:  HOME'
    
    def do_remove(self, arg):
        'Return ESH4D to the home position:  HOME'

    def do_exit(self, arg):
	print (bcolors.WARNING + "Bye...")
	exit()
def main():
	header = "▁▁▁▁▁▁▁▁▁▁▁▁▁ TARGET LIST ▁▁▁▁▁▁▁▁▁▁▁▁▁ \n";
	print(bcolors.HEADER + header)
	GetInfoShell().cmdloop();


if __name__ == "__main__":
    main()
