import os
import time
import csv
import datetime
import argparse
import sys
import math
from typeguard import typechecked

def main (option, uid, user_name, role):
    option_post_login_admin=['HELP', 'MONSTER', 'SHOP','ELITE','FINAL','SAVE']
    
    if option in option_post_login_admin:
        print("Input is currently being processed...")
        print()
        time.sleep(1)
    