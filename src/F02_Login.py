import csv
import custom_command

def login ():
    name = input("Username: ")
    passw = input("Password: ")
    print()
    
    if find_name(name, "K02_K_Tubes/data/user.csv") and check_pass(passw, "K02_K_Tubes/data/user.csv"):
        
        uid=take_id(name,"K02_K_Tubes/data/user.csv")
        role = custom_command.take_role(uid, "K02_K_Tubes/data/user.csv")
        
        if role == 'agent':
            print(f"Selamat datang, Agent {name}!")
            
        else:
            print(f"Selamat datang Professor {name}! Ada yang bisa kami bantu?")    

        print()
        
    else:
        
        if not find_name(name, "K02_K_Tubes/data/user.csv"):
            print("Username tidak terdaftar!")
            print()
            
        elif not check_pass(passw, "K02_K_Tubes/data/user.csv"):
            print("Password salah!")
            print()
    
    return uid, name, role

def find_name(name, file_path): #Melihat ketersediaan nama di database
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if name == row[1]:
                return True
    return False

def check_pass(passw, file_path): #ngecheck password benar atau salah
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if passw == row[2]:
                return True
    return False

def take_id(name, file_path): #Mengambil uid pemain
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if name == row['username']:
                uid= row['id']
                break
    return uid