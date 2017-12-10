import os,sys,shutil
from colorama import Fore
from time import sleep
os.system('clear')
print Fore.LIGHTCYAN_EX+ '''

 _   __         _   _   
| | / /        | | (_)  
| |/ /   __ _  | |  _  
|   (   /  ` | | | | |'''
print Fore.LIGHTRED_EX+'''| |\ \ | (_| | | | | | 
|_| \_\ \__,_| |_| |_| D@rk H3@v3n
'''
print(Fore.LIGHTGREEN_EX+'Author:\t Anirban Singha | Contact: https://twitter.com/iamdarkheaven')
if os.getuid()==0:
    filepath ='soft.txt'
    print '\n'
    ask=raw_input(Fore.LIGHTRED_EX+'Do you want to add Kali Linux in your system?(y/n): ')
    ask=ask.lower()
    if ask == 'y':
        print Fore.CYAN+'Adding Kali Linux repository in your system...'
        sleep(2)
        cmd1=os.system('os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6')
        cmd2=os.system("echo '# Kali linux repositories | Added by D@rk H3@v3n\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
        print 'Added Kali linux repository!'
        print 'Updating system...'
        sleep(2)
        os.system('apt-get update')
        print '\nUpdated'
        print Fore.LIGHTGREEN_EX+'Installing Kali linux software!\nThis may take some time. Seat back and relax.'
        sleep(4)
        with open(filepath) as fp:  
            line = fp.readline()
            while line:
                line = fp.readline()
                print(Fore.GREEN+ "Starting... ")
                print line
                print (Fore.YELLOW+'-------------------------------------------------')
                print(Fore.RESET)      
                install= 'apt-get install -y' +' '+ line
                print (Fore.LIGHTWHITE_EX)
                os.system(install)
                print (Fore.RESET)
                print (Fore.YELLOW+'-------------------------------------------------')
        print Fore.LIGHTGREEN_EX+'Adding some extra features for your convenience.'
        sleep(3)
        os.system("add-apt-repository ppa:diesch/testing && apt-get update")
        os.system("apt-get install kali-menu")
        print(Fore.RED+"\nIt's recomended to delete kali linux repository from your system\nFor your help script going to open source file.\nYou will find the repository at the bottom of the file\n")
        choice=raw_input('Press "y" to continue: ')
        print(Fore.RESET)
        choice=choice.lower()
        if choice =='y':
            os.system('nano /etc/apt/sources.list')
        print 'Updating and Upgrading your system....'
        sleep(3)
        os.system('apt-get update && apt-get upgrade -y')
        reboot=raw_input('\nAll features are added in your system.\nDo you want to reboot your system?(y/n)')
        reboot=reboot.lower()
        if reboot == 'y':
            print (Fore.LIGHTRED_EX+'Rebooting your system...')
            sleep(4)
            os.system('reboot')
else:
    print Fore.LIGHTRED_EX+'\nApply root permission to successfully execute the program.'
print '\t\t\tGood bye!\n\n'
