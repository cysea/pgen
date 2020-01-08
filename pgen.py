def rand():

	chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

	print ("\n> > > The Formatting is:")
	print ("> > > Fully Randomized.")
	
	length = 20
	password = ''

        for c in range(length):
		password += random.choice(chars)

	print ("\nThe Password is: " + password)
			
	pyperclip.copy(password)
		
	end()

def end():
	
	print ("\nPassword Copied To Clipboard!")	
	n = raw_input("Press ENTER for a new password...\n")

        if n == '':
	    rand()
        else:
            exit()

if __name__ == "__main__":
	import pyperclip
	import random
        rand()
