def main():
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

        os.system('cls' if os.name == 'nt' else 'clear')
        
        print colored("=======================================")
	print colored("\n> > > The Formatting is:", 'green')
	print colored("> > > Fully Randomized.", 'green')
	
        try:
            length = int(sys.argv[1])
        except:
            print colored("\n[*] No arguments passed, password length set to 20.", 'yellow')
            length = 20

        password = ''
        for c in range(length):
	    password += random.choice(chars)

        print ("\n[+] The Password is: \033[4m{0}\033[0m".format(password))
			
	pyperclip.copy(password)
		
	end()

def end():
	
	print colored("\n[+] Copied to clipboard!", 'green')

        print colored("\n[?] Press ENTER for a new password...", 'red')
        print colored("      Or anything else to quit :)", 'green')

        print colored("\n=======================================")
        
	n = raw_input()
        
        

        if n == '':
	    main()
        else:
            exit()

if __name__ == "__main__":
    import pyperclip
    import random
    import sys
    import os
    from termcolor import colored
    main()

