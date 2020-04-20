try:
    import sys 
    import time
except ImportError:
    print('Error importing libraries...')

configfile = open('config.py', 'w')
welcome = input('Welcome to the CustomBOT Setup! Would you like to continue? ')

def setup():
    print('OK! What is the name for your bot?')
    botname = input()

    print(f"Thanks! Lets start setting up {botname}. First off I'll need your bot token from the Discord Developer Panel")
    token = input()

    print(f'Great! What do you want the color theme to be for {botname}? (Currently I only support red green or blue)')
    colortheme = input()

    print(f'Lovely! What do you want the command prefix to be for {botname}?')
    prefix = input()

    print('Almost finished! Do you want to log all messages in your server?')
    logging = input()
    if logging == 'yes':
        logging = True
    elif logging == 'no':
        logging = False

    print(f"botname = '{botname}'; token = '{token}'; prefix = '{prefix}'; colortheme = '{colortheme}'; logging = '{logging}'", file=configfile)

if welcome == 'yes':
    setup()
elif welcome == 'no':
    sys.exit(0)