from termcolor import colored
import getpass,os
from tkinter import *

class App:
    def __init__(self,user_id='dummy',pwd='dummy'):
        self.base_path = f"/home/{getpass.getuser()}/PythDiary"
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
            os.chdir(self.base_path)
        if self.auth(user_id,pwd) :
            self.open_dialog(action='w')
            # option = int(input(colored("\nChoose your Option : \n1. Write Diary\n2. Browse Diary\n3. Exit\n>>> ","magenta","on_white",attrs=['bold'])))
            # if option == 1:
            #     self.open_dialog(action='write')
            # elif option == 2:
            #     self.open_dialog(action='browse')
            # else:
            #     print(colored("\nThank You !\nQuitting Programm .. ","green",attrs=['bold']))
    
    def open_dialog(self,action):
        root = Tk()
        # width= root.winfo_screenwidth() 
        # height= root.winfo_screenheight()
        # root.geometry("1000x600")
        root.resizable(0,0)
        root.title("Diary-Online")
        root.config(bg='white')

        text_box = Text(padx=2,pady=2,borderwidth=2,yscrollcommand=True)
        text_box.pack()


        root.mainloop()
    
    def auth(self,uname,pwd):
        return True


def login():
    # uname = input(colored('Username : ','white',attrs=['bold']))
    # pwd = getpass.getpass()
    App()


if __name__ == "__main__":
    text_banner = '''
########  ##    ## ######## ##     ##    ########  ####    ###    ########  ##    ## 
##     ##  ##  ##     ##    ##     ##    ##     ##  ##    ## ##   ##     ##  ##  ##  
##     ##   ####      ##    ##     ##    ##     ##  ##   ##   ##  ##     ##   ####   
########     ##       ##    #########    ##     ##  ##  ##     ## ########     ##    
##           ##       ##    ##     ##    ##     ##  ##  ######### ##   ##      ##    
##           ##       ##    ##     ##    ##     ##  ##  ##     ## ##    ##     ##    
##           ##       ##    ##     ##    ########  #### ##     ## ##     ##    ##    
  
'''
    print(colored(text_banner,'red',attrs=['bold']))

    login()

    
