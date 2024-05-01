import custom_command

#Isi code ini cuma prosedur printing art untuk instance dalam game nya aja sih

def inventory_art ():
    image =[
"          ⢀⣀⣀⣀⣀⣀⣀⣀⣀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠉⠉⠉⠉⠉⠉⠉⠉⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⣾⠀⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⠀⢷⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⢰⡏⠀⣿⣿⠀⣴⣶⣶⣶⣶⣶⣶⣶⣶⣦⠀⣿⣿⡀⢸⡆⠀⠀⠀⠀",
"⠀⠀⠀⠀⢸⡇⠀⣿⣿⣆⠘⠻⠇⢠⣤⣤⡄⠸⠟⠋⣠⣿⣿⡇⢸⡇⠀⠀⠀⠀",
"⠀⠀⠀⠀⢸⣇⠀⣿⣿⣿⣿⣶⣆⣈⣉⣉⣁⣰⣶⣿⣿⣿⣿⠃⢸⡇⠀⠀⠀⠀",
"⠀⠀⠀⠀⠈⣿⣀⣉⣉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⣉⣉⣀⣿⠀⠀⠀⠀⠀",
"⠀⠀⢀⡴⠀⣉⣉⠉⠉⠉⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠉⣉⣉⠀⢦⡀⠀⠀",
"⠀⠀⠈⣀⠀⣿⣿⠀⣿⣿⠀⠛⠛⠉⠉⠉⠉⠛⠛⠀⣿⣿⠀⣿⣿⠀⣀⠁⠀⠀",
"⠀⠀⢸⡇⢀⣿⣿⠀⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿⣿⠀⣿⣿⡀⢸⡇⠀⠀",
"⠀⠀⢸⡇⢸⣿⠀⣤⡤⢤⣄⠘⠻⠿⠿⠿⠿⠟⠃⣠⡤⢤⣤⠀⣿⡇⢸⡇⠀⠀",
"⠀⠀⢠⡄⢸⣿⠀⠛⠃⠘⠋⢸⣶⣶⣆⣰⣶⣶⡇⠙⠃⠘⠛⠀⣿⡇⢠⡄⠀⠀",
"⠀⠀⢠⡄⠸⣿⣿⠀⠷⠞⠀⠛⠛⠿⠿⠿⠿⠛⠛⠀⠳⠾⠀⣿⣿⠇⢠⡄⠀⠀",
"⠀⠀⠘⠗⠀⣿⣿⠀⣶⣶⠀⣿⣷⣶⣶⣶⣶⣾⣿⠀⣶⣶⠀⣿⣿⠀⠺⠃⠀⠀",
"⠀⠀⠀⠀⠀⠉⠉⠀⠉⠉⠀⠉⠉⠉⠉⠉⠉⠉⠉⠀⠉⠉⠀⠉⠉⠀⠀⠀⠀⠀"
    ]
    print("\n".join(image))
    

def main_menu (role, name):
    if len(name)<=22:
        multiplier1=11-(len(name)+1)//2
        multiplier2=11-(len(name)+1)//2
        
        if len(name) % 2 != 0:
            multiplier2+=1
    else:
        multiplier1=0
        multiplier2=0
    image=[
        "/   /                                     \   \ ",
        "| O |                                     | O |",
        "|   |- - - - - - - - - - - - - - - - - - -|   |",
        "| O |         M A I N    M E N U          | O |",
        "|   |                                     |   |",
        "| O |"+" "*multiplier1+f"Welcome {custom_command.capitalize_first_letter(role)} {name}!"+" "*multiplier2+"| O |",
        "|   |                                     |   |",
        "| O |- - - - - - - - - - - - - - - - - - -| O |",
        "|   |                                     |   |",
        "\   \                                     /   /",
        "",
        "     Ketik 'help' untuk mendapatkan bantuan    ",
    ]
    print("\n".join(image))