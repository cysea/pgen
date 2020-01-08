def main():
	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

        print colored("\n==========================")
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
        print colored("\nPress ENTER for a new password...", 'red')
	n = raw_input()

        if n == '':
	    main()
        else:
            exit()

if __name__ == "__main__":
    import pyperclip
    import random
    import sys
    from termcolor import colored
    main()

