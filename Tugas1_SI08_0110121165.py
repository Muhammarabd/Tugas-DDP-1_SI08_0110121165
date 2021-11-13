def check():
    email = input("Masukkan email: ")
    import re
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        print("Email Tidak Valid, Ulangi")
        return check()
def password_check():
    password = input("Masukkan password: ")
    chaeSept = ["!", "@", "#", "$"]
    if len(password) >= 8:
        if any(word.isnumeric() for word in password):
            if any(word.islower() for word in password):
                if any(word.isupper() for word in password):
                    if any(word in chaeSept for word in password):
                        return True
                    else:
                        print("Password tidak valid")
                        return password_check()
                else:
                    print("Password tidak valid")
                    return password_check()
            else:
                print("Password tidak valid")
                return password_check()
        else:
            print("Password tidak valid")
            return password_check()
    else:
        print("Password tidak valid")
        return password_check()

def kepersetaan():
    level = input("Masukkan Level Keanggotaan Anda(Silver/Gold/Diamond): ")
    while level != "Silver" and level != "Gold" and level != "Diamond":
        level = input ("Enter invalid, repeat: ")
    else:
        if level == "Silver":
            if u < 5:
                diskon = i * (5/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 5%")
            else:
                diskon = i * (10/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
        elif level == "Gold":
            if u < 5:
                diskon = i * (10/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 10%")
            else:
                diskon = i * (15/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
        elif level == "Diamond":
            if u < 5:
                diskon = i * (15/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 15%")
            else:
                diskon = i * (20/100)
                print("Selamat! Anda mendapatkan potongan harga sebesar 20%")
        setelah_diskon = i - diskon
        print("Total Harga yang harus dibayar: ", float(setelah_diskon))
        quit()
u = 0
i = 0
while True:
    j = input("Masukkan nama produk yang akan dibeli atau X untuk selesai: ")
    if j == "X" and u == 0:
        print("Terima Kasih,Sampai Jumpa")
        quit()
    if j == "X" and u > 0:
        print("Total produk yang dibeli:", u)
        print("Total harga produk: ", i)
        break
    else:
        y = int(input("Masukkan harga produk: "))
        print("Berhasil menambahkan", j, "dengan harga", y)
        u += 1
        i += y
h = input("Apakah Anda seorang anggota? (Y/T): ")
if h == "Y":
    if check():
        if password_check():
            kepersetaan()
                
        else:
            password_check()
else:
    print("Total harga yang harus dibayar:", i)
    print("Terima kasih telah berbelanja di NFElectrics.")
print("Terima kasih. Sampai jumpa.")
