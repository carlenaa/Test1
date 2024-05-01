import os
import time
import csv
import datetime
import argparse
import sys
import math
from typeguard import typechecked

import F07_Invetory
import ascii_art

def main (option, uid, user_name, role):
    option_post_login_agent=['HELP','INVENTORY','BATTLE','ARENA','SHOP','ELITE','FINAL','LABORATORY','SAVE']
    
    if option in option_post_login_agent:
        print("Input is currently being processed...")
        print()
        time.sleep(1)
        
        if option == 'INVENTORY':
            ascii_art.inventory_art()
            F07_Invetory.inventory(uid, user_name)
        
        time.sleep(1)
        
        ascii_art.main_menu(role, user_name)
        print()