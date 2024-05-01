import csv
from F00_RNG import random_int
import time
import os
from typeguard import typechecked
import custom_command

# Function untuk buat file csv
def create_csv(file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['type', 'stock', 'price'])
        
def update_csv(file_path, data):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)


#Program
file_path = 'K02_K_Tubes/data/monster_inventory.csv'  # File path nya

#Program buat CSV
#create_csv(file_path) #Manggil function

#Program update CSV
data = custom_command.read_csv('K02_K_Tubes/data/monster.csv')
for i in range (1, len(data)):
    data2 = [1, data[i][0], 5]
    custom_command.update_csv(file_path, data2)
    custom_command.save_updated_csv(file_path)