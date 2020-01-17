import pyperclip
import random
import sys
import os
from termcolor import colored

def main():
    chars = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*'

    os.system('cls' if os.name == 'nt' else 'clear')
        
    print colored("=======================================")

    print colored("\n> > >",'red'), colored("The Formatting is Fully Randomized",'white'), colored("< < <",'red')
    #print colored("> > > Fully Randomized.",'green')
	
    try:
        length = int(sys.argv[1])
        print colored("\n[*]",'yellow'), colored("Password length set to [",'white'), colored(sys.argv[1],'yellow'), colored("]",'white')
    except:
        print colored("\n[*]",'yellow'), colored("No arguments passed, password length set to [",'white'), colored("20",'yellow'), ("]")
        length = 20

    password = ''
    for c in range(length):
	password += random.choice(chars)

    print colored("\n[+]",'green'), ("Password:"), colored("\033[4m{0}\033[0m".format(password),'white')
			
    pyperclip.copy(password)
		
    end()

def end():
    print colored("\n[+]",'green'), ("Copied to clipboard!")

    print colored("\n[*] ",'yellow'), colored("Press ",'white'), colored("ENTER ",'red'),colored("for a new password...",'white')
    print colored("        Or ",'white'), colored("Ctrl+D",'red'), colored(" to quit :)",'white')

    print colored("\n=======================================")

    try:
	n = raw_input()

        if n == '':
	    main()
        #else:
        #    sys.exit()
    except (KeyboardInterrupt, EOFError):
        sys.exit()

if __name__ == "__main__":
    main()

