# i = 1

# while i <= 100:
#     print(i, end=" ")
#     i += 1

# while True:
#     i = input("Ketik Stop Untuk berhenti : ")
#     if i == "Stop":
#         break

# while True:
#     pin = input("masukan pin : ")
#     if pin == "1234":
#         print ("berhasil")
#         break
#     else:
#         print("gagal")
        
        

# #Hitung Mundur

# i = int(input("masukan angka "))

# while i >= 0:
#     print(i)
#     i -= 1

# while True:
#     print("1. Tetap disini\n 2. Keluar")
#     pilih = input("Pilih : ")
#     if pilih == "1":
#         print("Selamat datang di program ini")
#     else:
#         print("Terima kasih telah menggunakan program ini")
#         break

#tebak angka

angka = 56

while True:
    jawaban = int(input(" masukan tebakan anda = "))
    if jawaban > angka:
        print("Terlalu besar")
    elif jawaban < angka:
        print("Terlalu Kecil")
    if jawaban == angka:
        print("Selamat Anda menemukan angka yang benar")
        break
    else:
        print("anda salah, coba lagi")