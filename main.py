import os
import time
import csv
import datetime
import argparse
import sys
import math
from typeguard import typechecked

#importing other codes
sys.path.append('K02_K_Tubes/src')
import custom_command
import ascii_art
import play_center_admin
import play_center_agent
from F00_RNG import random_int
import F01_Register
import F02_Login
import F04_Help

#PROGRAM O.W.C.A Agent
'''Program utama (mother file) dari keseluruhan program, bisa dilihat setiap sub program di 'src' untuk detail lebih lanjut'''


#KAMUS
# option_pre_login, option_post_login, option_logging_out, state    = Array of string
# user_input                                                        = string
# uid                                                               = integer


#ALGORITMA
option_pre_login=['REGISTER','LOGIN','EXIT','HELP']
option_post_login_agent=['HELP','INVENTORY','BATTLE','ARENA','SHOP','ELITE','FINAL','LABORATORY','SAVE']
option_post_login_admin=['HELP', 'MONSTER', 'SHOP','ELITE','FINAL','SAVE']
option_logging_out=['EXIT','LOGOUT']


state=['out','in'] #Status player, login atau tidak. Default 'out'
ProgramIsRunning=True #Status apakah program sedang running

#Gimmick loading program
print()
print("Initializing program...")
time.sleep(random_int(1,3))
print()
print("Program started!")
time.sleep(1)
print()
print("type 'help' for help! :D")
print()


while ProgramIsRunning: #Mulai program
    current_state=state[0]
    user_input=custom_command.uppercase(input(">>> "))
    
    #Check input valid atau tidak
    if user_input in option_pre_login:
        
        if user_input == 'EXIT': #Check apakah player mau exit
            ProgramIsRunning=False
            
        elif user_input=='HELP': #Ketika minta help
            F04_Help.help("out")
            print()
            
        else: #Player bisa masuk, lanjut ke program utama game
            if user_input=='LOGIN':
                try:
                    uid, user_name, role = F02_Login.login()
                    current_state=state[1]
                except:
                    current_state=state[0]
            else:
                try:
                    uid, user_name, role = F01_Register.registering()
                    current_state=state[1]
                except:
                    current_state=state[0]
            
            if current_state==state[1]:

                ascii_art.main_menu(role, user_name)
                print()
                
                while current_state==state[1]:
                    
                    user_input=custom_command.uppercase(input(">>> "))
                    print()
                    
                    if user_input in option_logging_out:
                        print('Verifying save state...')
                        time.sleep(3)
                        print("You have been logged out.")
                        print()
                        current_state=state[0]
                        
                        if user_input=='EXIT':
                            ProgramIsRunning=False
                    
                    elif user_input == 'HELP' and role=='agent':
                        F04_Help.help('in')
                        print()
                    
                    elif user_input == 'HELP' and role == 'admin':
                        F04_Help.help('admin')
                        print()
                    
                    elif user_input in option_pre_login [:2]:
                        print(f"You're already logged in as {user_name}, can't take user input. Try logging out first.")
                        print()
                    
                    elif role == 'agent' and user_input in option_post_login_agent: #Continue as Agent
                        play_center_agent.main(user_input, uid, user_name, role)
                    
                    elif role == 'admin' and user_input in option_post_login_admin: #Continue as Admin
                        play_center_admin.main(user_input, uid, user_name, role)
                    
                    else:
                        print("Wrong command, please retry or type 'help'")
                        print()

    elif user_input in option_post_login_agent or user_input in option_post_login_admin or user_input=='LOGOUT': #Ketika player mau log-out tapi mereka belum login
        print("Input cannot be taken, you're already logged out.")
        print()

    else: #ketika command yang mereka masukkan, tidak sesuai command yang ada
        print("Wrong command, please retry or type 'help'")
        print()
        
    if ProgramIsRunning==False:
        print("Closing program...")
        time.sleep(2)
        print()

print('Program has successfully been closed')