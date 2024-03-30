##attrib +h +s +r name_of_the_file_with_extension

# Importing the required modules
import maskpass,base64,time,os,bcrypt,json
from colorama import Fore

color = {
    'RED'             : '\033[1;91m',
    'UNDERLINE_PURPLE' : '\033[4;34m',
    'GREEN'           : '\033[1;92m',
    'YELLOW'          : '\033[1;33m',
    'CYAN'            : '\033[0;36m',
    'PURPLE'            : '\033[0;34m',
    'MAGENTA'         : '\033[0;35m',
    'DEFAULT'         : '\033[0m',
    'TWITTER_BLUE'            : '\033[38;5;33m',
}

# starting the main menu 
def start():
	header=color['PURPLE']+'''
Choose any one of the option to begin! 
+--------+-------------------------------------+
| 1   |    Login to use Folder lock 		|
+--------+-------------------------------------+
| 2   |    Signup to use Folder lock   		|
+--------+-------------------------------------+
| 3   |    exit Folder lock 	            |
+--------+-------------------------------------+
'''
	print(header+color['DEFAULT'])
	main()

#main loop for the execution
def main():
	maininput = input(color['TWITTER_BLUE'] + 'Folder Lock> ' + color['DEFAULT']).lower()
	while True:
		if maininput=='1':
			logIn()
		elif maininput=='2':
			signUp()
		elif maininput=='3':
			print('exiting folder lock')
			exit_menu()
		else:
			print('select any one of the options [1,2,3] from the list')
			start()
			
def signUp():
	os.system('cls')
	check_file = os.stat('cred.json').st_size
	if(check_file == 0):
		pass
	else:
		print("Already Master User present!!! Login to proceed")
		time.sleep(2)
		logIn()
	print("\n===========Create Account============")
	name = input("Username : ")
	pwd = maskpass.askpass("Password : ")
	encpwd = base64.b64encode(pwd.encode("utf-8"))
	salt = bcrypt.gensalt()
	hashed_password = bcrypt.hashpw(encpwd, salt).decode()
	data={}
	data[name]=hashed_password
	with open('cred.json','w') as json_file1:
		json.dump(data,json_file1)
	print('signup successful')
	os.system('attrib +h +s +r '+'cred.json')
	time.sleep(1)
	logIn()
	
def logIn():
	os.system('cls')
	check_file = os.stat('cred.json').st_size
	if(check_file == 0):
		print("No master user present!!! signup to proceed")
		time.sleep(2)
		signUp()
	else:
		pass
	while True:
		json_file=open('cred.json')
		data = json.load(json_file)
		print(Fore.RESET + "\n\n============Login Page==============")
		name = input("Username : ")
		if(name not in data):
			print('Incorrect user name try again')
			time.sleep(2)
			logIn()
		else:
			hashed_password=data[name].encode("utf-8")
		pwd = maskpass.askpass("Password : ")
		encd_pwd=base64.b64encode(pwd.encode("utf-8"))
		if bcrypt.checkpw(encd_pwd, hashed_password):
			print("Please wait while we are checking the login info...")
			time.sleep(3)
			print(Fore.GREEN + "Successfully logged in.")
			print("Here you are!"+ color['DEFAULT'])
			folder_menu()
		else:
			print("Please wait while we are checking the login info...")
			time.sleep(3)
			print(Fore.RED + "Login Failed. Please try again in 3 seconds. (This is done to prevent Brute Forcing)")
			time.sleep(3)
def folder_menu():
	os.system('cls')
	head=color['YELLOW']+'''
Choose any one of the option to begin! 
+--------+-------------------------------------+
| 1   |    Lock a Folder			|
+--------+-------------------------------------+
| 2   |    Unlock a Folder			|
+--------+-------------------------------------+
| 3   |    exit Folder lock			|
+--------+-------------------------------------+
'''
	print(head)
	menuselect = input(color['TWITTER_BLUE']+'Folder Lock> '+ color['DEFAULT'])
	if "1" in menuselect.lower():
		os.system('cls')
		folder_lock()
	elif "2" in menuselect.lower():
		os.system('cls')
		folder_unlock()
	elif "3" in menuselect.lower():
		os.system('cls')
		exit_menu()
	else:
		os.system('cls')
		print('Please choose any one from 1,2 or 3')
		folder_menu()


def folder_lock():
	os.system('cls')
	print('What folder would you like to lock? Please type a Directory!')
	folderSelect = input(color['TWITTER_BLUE'] + "(e.x. ~/Desktop/FOLDER_NAME)> " + color['DEFAULT'])
	os.system('attrib +h +s +r '+folderSelect)
	print('Folder is locked')
	time.sleep(2)
	exit_menu()
def folder_unlock():
	os.system('cls')
	print('What folder would you like to unlock? Please type a Directory!')
	folderSelect = input(color['TWITTER_BLUE'] + "(e.x. ~/Desktop/FOLDER_NAME)> " + color['DEFAULT'])
	os.system('attrib -h -s -r '+folderSelect)
	print('Folder is Unlocked')
	time.sleep(2)
	exit_menu()

def exit_menu():
	print('Would you like to exit Folder Locker? Yes/no or Y/n')
	exitInput = input(color['TWITTER_BLUE'] + "Folder Locker> " + color['DEFAULT'])
	if "yes" in exitInput.lower() or "y" in exitInput.lower():
		os.system('cls')
		exit()
	elif "no" in exitInput.lower() or "n" in exitInput.lower():
		os.system('cls')
		print('Redirecting to main menu')
		folder_menu()
	else:
		os.system('cls')
		print('You may only say yes or no!')
		exit_menu()

if __name__ == "__main__":
	start()
	main()