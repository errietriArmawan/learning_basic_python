
# for angka in range(10): #menggunakan range untuk mengulang perulangan 0-9
#     print(angka, end=",")

# for angka in range(1,10): #menggunakan range untuk mengulang perulangan 1-9
#     print(angka, end=",")

# for angka in range(2,100,2): #menggunakan range untuk mengulang perulangan 1-9 dengan langkah
#     print(angka, end=",")

# for angka in range(10): #menggunkan continue untuk skip angka 0
#     if angka == 0:
#         continue
#     print(angka, end=",")

# for angka in range(10): #menggunkan continue untuk skip angka 0
#     if angka == 6:
#         break
#     print(angka, end=",")

#membuat urutan ganjil 
ganjil_list = [angka for angka in range(1,16) if angka % 2 == 1]
print("Angka Ganjil dari 1 sampai 15 = ",end="")
for i, angka in enumerate(ganjil_list):
    if i < len(ganjil_list) - 1:
        print (angka, end = ",")
    else:
        print(angka)

print()

# kelipatan 5 - 50
print(f'Angka kelipatan 5 =', end=" ")
for i, kelipatan in enumerate(range(5,51,5)):
        if i < 9:
            print(kelipatan, end=",")
        else:
            print(kelipatan)

#habis bagi 3
habis_bagi_3 = [angka for angka in range (1,21) if angka % 3 == 0]
print(f'Angka yang habis dibagi 3 =', end=" ")
for i, angka in enumerate(habis_bagi_3):
    if i < len(habis_bagi_3) - 1:
        print(angka, end=",")
    else: 
        print(angka)

#menghitung jumlah total dari 1 - 50
# Menghitung jumlah total dari 1 sampai 50
total = 0
for i in range(1, 51):
    total += i

print("Jumlah total dari 1 sampai 50 adalah:", total)

jumlah_genap = 0
for i in range(1, 51):
    if i % 2 == 0:
        jumlah_genap += 1

print("Banyaknya bilangan genap dari 1 sampai 50 adalah:", jumlah_genap)
