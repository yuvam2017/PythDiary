from termcolor import colored
import getpass,os
from tkinter import *
from Database import Database
from time import sleep
from CryptTool import CryptTool

db = Database()
crypt = CryptTool()

class App:
    def __init__(self,user_id='dummy',pwd='dummy',mode='dummy'):
        self.base_path = f"/home/{getpass.getuser()}/PythDiary"
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
            os.chdir(self.base_path)

        bool,msg = self.auth(user_id,pwd,mode)

        if bool:
            option = int(input(colored("\nChoose your Option : \n1. Write Diary\n2. Browse Diary\n3. Exit\n>>> ","white",attrs=['bold'])))
            if option == 1:
                self.open_dialog(action='write')
            elif option == 2:
                self.open_dialog(action='browse')
            else:
                print(colored("\nThank You !\nQuitting Programm .. ","green",attrs=['bold']))
                pass
        else : 
            print(colored(msg,'red',attrs=['bold']))
    
    def open_dialog(self,action):
        if action == "write":
            self.write_dialog()
        elif action == "browse": 
            self.browse_dialog()
        else: 
            print("Invalid Actions")

    def browse_dialog(self):
        print("browse")

    def write_dialog(self):
        
        self.root = Tk()
        # width= root.winfo_screenwidth() 
        # height= root.winfo_screenheight()
        # root.geometry("1000x600")
        # root.resizable(0,0)
        self.root.title("Diary-Online")
        self.root.config(bg='white')

        # Label
        label = Label(text="Dear Diary",bg='white',fg='black',font=["Montserrat",20,"bold"])
        label.grid(row=0,column=0,columnspan=2,sticky=W)

        text_box = Text(padx=2,pady=2,borderwidth=2,yscrollcommand=True,fg="black",font=["Montserrat"],width=80)
        text_box.grid(row=1,column=0,columnspan=2,sticky=NSEW)

        # button
        btn = Button(text="Save",fg="white",bg="green",command=self.onSave,activebackground="green",activeforeground="white",borderwidth=0.5,font=["Ubuntu",20,"bold"])
        btn.grid(row=2,column=0)

        btn_quit=Button(text="Cancel Diary",fg="white",bg="red",command=self.quit,activebackground="red",activeforeground="white",font=["Ubuntu",20,"bold"])
        btn_quit.grid(row=2,column=1,pady=5)

        self.root.mainloop()
    
    def onSave(self):
        db.write

    def quit(self):
        self.root.destroy()

    def auth(self,uname,pwd,mode):
        user_exists = db.user_exists("users",uname)

        if user_exists and mode == "login":
            return True,"good"

        elif user_exists and mode == "loginAutoSave":
            return True,"good"

        elif user_exists and mode == "signup":
            return False,"User Exists, Please Login"

        elif not user_exists and mode == "loginAutoSave":
            return False,"User doesn't exists"

        elif not user_exists and mode == "login":
            return False,"User doesn't exists"

        elif not user_exists and mode == "signup":
            hash_pwd = crypt.get_hash("pwd")
            result = db.write_one("users",uname,{'_id':0 , "Password":hash_pwd})
            print(colored("New User Added",attrs=['bold']))
            return True,"good"
    
        else :
            return False


def login():

    choice = int(input(colored('1. Login\n2. Sign up\n3. Exit\n>>> ',attrs=["bold"])))
    if choice == 1:
        uname = input(colored('Username : ','white',attrs=['bold']))
        pwd = getpass.getpass()
        choice_autologin = input("Remeber password for Autologin [y/N] : ")
        if choice_autologin == "" or choice_autologin == "N" or choice_autologin == "n":
            App(uname,pwd,mode='login')
        elif choice_autologin == "y" or choice_autologin == "Y":
            App(uname,pwd,mode='loginAutoSave')
    elif choice == 2:
        uname = input(colored('Username : ','white',attrs=['bold']))
        pwd = getpass.getpass()
        print(colored('Password will be invisible in 3 seconds\nYour Password is : ','green',attrs=['bold']))
        print(colored(pwd,'red',attrs=['bold']),end='\r')
        sleep(1)
        print(colored('!!!!!!!!! Omitted Your Password !!!!!!!!!','green',attrs=['bold']))
        App(uname,pwd,mode='signup')
    elif choice == 3:
        print(colored("\nThank You !\nQuitting Programm .. ","green",attrs=['bold']))
        pass
    else:
        print("\nInvalid Option\n")
        login()

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

    
