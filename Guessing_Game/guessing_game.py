# Importing the required modules
import time,random,math,os

# defining custom exceptions
class lowerband_exception(Exception):
    ...
    pass

# getting user input
def get_input():
    while True:
        try:
            lower_band=int(input("Enter the Lower band value: "))
            break
        except:
            print("\nYou have entered a invalid integer!!! Enter a valid integer\n")
            time.sleep(2)
            os.system('cls')
    while True:
        try:
            upper_band=int(input("Enter the Upper band value: "))
            os.system('cls')
            if(upper_band<=lower_band):
                raise lowerband_exception
            break
        except lowerband_exception:
            print("\nYou have entered a value less than the lower bound\n")
            time.sleep(2)
            os.system('cls')
        except:
            print("\nYou have entered a invalid integer!!! Enter a valid integer\n")
            time.sleep(2)
            os.system('cls')
    random_num=random.randint(lower_band,upper_band)
    guess_atempt=round(math.log(upper_band - lower_band + 1, 2))
    return random_num,guess_atempt,lower_band,upper_band

# guessing logic method

def start_guess(rand_num):
    count=0
    while True:
        try:
            print("\n\tYou've only have ",rand_num[1]-count ," chances to guess the integer!\n")
            guess_num=int(input("Try guessing the number :- "))
            if(guess_num>rand_num[3] or guess_num<rand_num[2]):
                raise Exception
            count+=1
        except:
            print("\nGuessing number is not in range or invalid !!! Enter a valid number\n")            
            time.sleep(2)
            os.system('cls')
            continue
        if(guess_num==rand_num[0]):
            print("\nCongrats you guessed it correct!!! ,Numer of Guesses used :",count,"\n")
            time.sleep(2)
            os.system('cls')
            break
        elif(count==rand_num[1]):
            print("\nyou failed to guess the number!!! Better luck next time\n")
            time.sleep(2)
            os.system('cls')
            break
        elif(guess_num>rand_num[0]):
            print("\nGuessed number is too high! try entering a lesser number\n")
            time.sleep(2)
            os.system('cls')
        elif(guess_num<rand_num[0]):
            print("\nGuessed number is too low! try entering a greater number\n")
            time.sleep(2)
            os.system('cls')

if __name__=='__main__':
    rand_num=get_input()
    start_guess(rand_num)

