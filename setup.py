try:
    import sys
    import json
except ImportError:
    print('Error importing libraries...')

print('Welcome to the CustomBOT Setup! Would you like to continue? (yes/no)')
welcome = input(">> ")

def setup():
    with open("config.json", "w+") as configfile:
        print('OK! What is the name for your bot? ')
        botname = input(">> ")

        print(f"Thanks! Lets start setting up {botname}. First off I'll need your bot token from the Discord Developer Panel (You can get one at https://discord.com/developers/applications) ")
        token = input(">> ")

        print(f'Great! What do you want the color theme to be for {botname}? (Currently I only support red green or blue)')
        colortheme = input(">> ")

        print(f'Lovely! What do you want the command prefix to be for {botname}?')
        prefix = input(">> ")

        print('Almost finished! Do you want to log all messages in your server? (yes/no)')
        logging = input()
        if logging == 'yes':
            logging = True
        elif logging == 'no':
            logging = False

        info = {
            "botname": botname,
            "token": token,
            "theme": colortheme,
            "prefix": prefix,
            "logging": logging
        }

        json.dump(info, configfile, indent=4)

if welcome == 'yes':
    setup()
elif welcome == 'no':
    sys.exit(0)