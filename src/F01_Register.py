import csv
import custom_command

def registering (): #funsgi/prosedur register utama
    file_path = "K02_K_Tubes/data/user.csv"
        #input
    name=input('Masukan Username: ')
    passw=input('Masukan Password: ')
    print()
    
    if not isNameValid (name): #Validasi nama
        print("Bro, usernamenya cuma boleh, alpabet, angka, '_', dan/atau '-'. Coba lagi sana!")
        print()
    else:
        if find_name(name, file_path): #Validasi keunikan nama
            print(f"Sayang sekali... Nama '{name}' sudah terpakai, cari nama lain sana!")
            print()
        else: #Masuk ke program memilih monster
            chosen_monster=starting_monster(name)
    
    #Manyimpan data player baru
    uid=make_id(file_path)+1 #Membuat user id unik
    role = "agent"
    update_csv(file_path,[(make_id(file_path)+1),name,passw,'agent',0])
    save_updated_csv(file_path)
    
    return uid, name, role

def isNameValid(input_string): #Melihat apakah nama valid atau tidak
    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_0123456789"
    for char in input_string:
        if char not in allowed_chars:
            return False
    return True

def find_name(name, file_path): #Melihat apakah nama unik atau tidak
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if name == row[1]:
                return True
    return False
            
def update_csv(file_path, data): #Fungsi standar untuk update file csv
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
        
def make_id(file_path): #Membuat id unik untuk pemain
    last_id = 0
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            last_id = int(row['id']) #Melihat id pemain terakhir (latest id number)
    return last_id

def save_updated_csv(file_path): #Save file csv yang sudah terupdate
    try:
        with open(file_path, 'r') as original_file:
            data = list(csv.reader(original_file))

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except Exception as e:
        print(f"An error occurred while saving the updated CSV file: {e}")
        print()
        

def starting_monster(name): #Funsgi/Prosedur memilih monster pertama
    file_path="K02_K_Tubes/data/monster.csv" #File_Path
    
    while True:
        mon=[] #List akan diisi dengan starting monster
        with open(file_path, 'r', newline='') as file: #Mengisi starting monster ke list
            reader = csv.reader(file)
            next(reader)  # Skip header 
            for i, row in enumerate(reader, start=1):
                if i > 3:
                    break
                mon.append(row[1])
        
        #Suruh Player milih monster nya
        print("Silahkan pilih SATU 'monster' dari 3 monster berikut, sebagai 'monster' pertama kau!")
        for i in range (1,len(mon)+1):
            print(f"{i}. {mon[i-1]}")        
        print()
        
        choose=int(input("Monster Pilihanmu: "))
        
        print()
        
        #validasi monster yang dipilih
        if choose<1 or choose>len(mon):
            print(f"Bro... Really... There is No {choose}th option!")
            print()
        else:
            chosen_monster=mon[choose-1]
            print(f"Selamat datang Agent {name}! Mari kita kalahkan Omega dengan {chosen_monster}!")
            print()
            break
    
    #save monster yang dipilih ke inventory
    data=[(make_id("K02_K_Tubes/data/user.csv")+1),choose,1]
    update_csv("K02_K_Tubes/data/monster_inventory.csv", data)
    save_updated_csv("K02_K_Tubes/data/monster_inventory.csv")
        
    return chosen_monster    