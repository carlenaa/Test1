import custom_command
import time
import F04_Help

def inventory (uid, user_name):
    while True:
        in_inventory=True
        option_back = ['RETURN', 'BACK', 'KELUAR', 'CANCEL', 'EXIT']
        
        inventory=list_invetory(uid, user_name) #Print list invetory dan membuat data sementara
        
        while in_inventory:
            
            print("Ketikkan id untuk menampilkan detail item: ")
            user_input=custom_command.uppercase(input(">>> "))
            
            if user_input in option_back or user_input=='INVENTORY':
                in_inventory=False
            
            elif user_input == 'HELP':
                F04_Help.help('inv')
                print()
            
            else:  
                try:
                    if 1<=int(user_input)<=len(inventory):
                        inventory_detail(int(user_input), inventory)
                    else:
                        print(f"Tidak ada id ke-{user_input}")
                        print()
                except:
                    print("Command tidak diketahui, ulangi!")
                    print()
    
        if user_input in option_back:
            print('Keluar dari inventory...')
            print()
            time.sleep(1)
            break
    
def list_invetory (uid, user_name):
    inv=[] #type inv
    data_mon = custom_command.read_csv("K02_K_Tubes/data/monster_inventory.csv")
    data_pot = custom_command.read_csv("K02_K_Tubes/data/item_inventory.csv")
    coin = custom_command.from_x_take_y(str(uid), "K02_K_Tubes/data/user.csv", 'id', 'oc')
    
    for i in range (1,len(data_mon)):
        if data_mon[i][0] == str(uid):
            inv.append([data_mon[i], 'monster'])
            
                 
    for j in range (1+i,len(data_pot)+i):
        if data_pot[j-i][0] == str(uid):
            inv.append([data_pot[j-i], 'potion'])
            
    print(f"============= Inventory (Player (ID): {user_name} ({uid})) =============")
    print(f"Jumlah O.W.C.A Coin-mu adalah: {coin}")
    print()
    
    if len(inv) == 0:
        print("Tidak ada apa-apa disini. Kita kembali ke main menu saja yuk!")
        print()
    
    else:
    
        print("ID | Type         | Specs")
        
        
        for i in range (len(inv)):
            if inv[i][1] == 'monster':
                
                monster_name = custom_command.from_x_take_y(inv[i][0][1], "K02_K_Tubes/data/monster.csv", 'id', 'type')
                monster_level = int(inv[i][0][2])
                monster_HP = int(custom_command.from_x_take_y(inv[i][0][1], "K02_K_Tubes/data/monster.csv", 'id', 'hp'))
                # monster_HP += monster_HP * (monster_level-1) * 0.1                # Apakah perlu kalkulasi sesuai levelnya?
                
                print(f"{i+1}.  Monster        (Name: {monster_name}, Lvl: {monster_level}, HP: {monster_HP})")
                
            elif inv[i][1] == 'potion':
                
                pot_type = custom_command.capitalize_first_letter(inv[i][0][1])
                qty = inv[i][0][2]
                
                print(f"{i+1}.  Potion         (Type: {pot_type}, Qty: {qty})")
            
        print()
    
    return inv
    

def inventory_detail (input, data):
    accessed_data = data[input-1]
    if accessed_data[1] == 'monster':
        temp_data = custom_command.read_csv("K02_K_Tubes/data/monster.csv")
        for i in range (1,len(temp_data)):
            if accessed_data[0][1] == temp_data[i][0]:
                print("Monster")
                print(f"Name        : {temp_data[i][1]}")
                print(f"ATK Power   : {temp_data[i][2]}")
                print(f"DEF Power   : {temp_data[i][3]}")
                print(f"HP          : {temp_data[i][4]}")
                print(f"Level       : {accessed_data[0][2]}")
                print()
            
    elif accessed_data[1] == 'potion':
            print("Potion")
            print(f"Type        : {accessed_data[0][1]}")
            print(f"Quantity    : {accessed_data[0][2]}")
            print()