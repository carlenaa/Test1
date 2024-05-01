import F00_RNG

def help (state):
    if state == 'out': #Ketika player di state logged out dan mengetik 'HELP'
        print()
        print("=============================HELP=============================")
        print()
        print("Kamu belum login! Silahkan login dengan mengetik:")
        print()
        print("     'Login'      : Masuk ke akun yang telah terdaftar")
        print("     'Register'   : Membuat akun baru")
        print()
        print("                    atau")
        print()
        print("     'Exit'       : Keluar dari program")
        print()
        print("Note:")
        print("- Mohon memasukkan nama fungsi yang terdaftar diatas!")
        print()
        print("==============================================================")
        
    elif state == "in": #Help ketika player telah login
        print()
        print("===============================================HELP============================================")
        print()
        print(f"Tip:{tip()}")
        print()
        print("Selamat, anda sudah login! Berikut hal yang agent dapat lakukan!")
        print()
        print("     'Logout'         : Keluar dari akun ini")
        print("     'Inventory'      : Melihat banyak Coin, Barang, dan Monster yang sekarang kamu miliki!")
        print("     'Battle'         : Melawan monster secara random.")
        print("     'Arena'          : Kalahkan monster di arena untuk menjadi semakin kuat!")
        print("     'Elite'          : Melawan monster elite untuk mendapatkannya! (Not yet available!)")
        print("     'Final'          : Kalahkan Omega untuk menjadi yang terkuat! (Not yet available!)")
        print("     'Shop'           : Melihat apa stock shop saat ini.")
        print("     'Laboratory'     : Gunakan coin mu untuk menaikan level monster kamu!")
        print("     'Save'           : Menyimpan data saat ini.")
        print("     'Exit'           : Keluar dari program.")
        print()
        print("Note:")
        print("- Mohon memasukkan nama fungsi yang terdaftar diatas!")
        print()
        print("===============================================================================================")
        
    elif state == 'admin': #Help ketika admin telah login
        print()
        print("=========================================HELP======================================")
        print()
        print("Selamat, anda sudah login! Berikut hal yang agent dapat lakukan!")
        print()
        print("     'Logout'         : Keluar dari akun ini")
        print("     'Monster'        : Melakukakn Perubahan terhdapan O.W.C.A-dex")
        print("     'Elite'          : Setting monster elite. (Not yet available!)")
        print("     'Final'          : Setting stat Omega. (Not yet available!)")
        print("     'Shop'           : Management shop.")
        print("     'Save'           : Menyimpan data saat ini.")
        print("     'Exit'           : Keluar dari program.")
        print()
        print("Note:")
        print("- Mohon memasukkan nama fungsi yang terdaftar diatas!")
        print()
        print("===================================================================================")
        
    elif state == 'inv': #Help ketika player berada di inventory
        print()
        print("=========================================HELP======================================")
        print()
        print(f"Tip:{tip()}")
        print()
        print("     'Inventory'      : Melihat inventory secara keseluruhan")
        print("      {id}            : Menampilkan detail item sesuai nomor input")
        print("     'Exit/Keluar'    : Keluar menu inventory.")
        print()
        print("Note:")
        print("- Mohon memasukkan nama fungsi yang terdaftar diatas!")
        print()
        print("===================================================================================")
        

def tip ():
    tips = [
        "Berapa banyak orang yang membaca tips ini, ya?",
        "Apakah kalian tahu monster di game ini terinspirasi dari grup komedian?",
        "Tahukah kamu, bahwa ada 3 monster yang dibuat oleh admin sebagai monster paling kuat?",
        "Setiap 60 detik di loading screen, 1 menit telah terlewati di dunia nyata."
    ]
    return (tips[F00_RNG.random_int(0,len(tips)-1)])