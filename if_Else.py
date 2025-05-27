
'''
siswa_masuk = int(input("Siswa yang hadir : "))
jml_siswa = 10

if siswa_masuk == 10 :
    print ("Kelas Penuh")
elif siswa_masuk > jml_siswa:
    print(f"Murid Kelebihan atau ada murid palsu sebanyak{siswa_masuk - jml_siswa}")
else:
    print(f"Kelas kurang {jml_siswa - siswa_masuk}")
'''

# nilai = int(input("Masukan nilai : "))
# if nilai >= 90 and nilai <= 100:
#     print("predikat = A")
# elif nilai >= 80 and nilai <= 89:
#     print("predikat = B")
# elif nilai >= 70 and nilai <= 79:
#     print("predikat = C")
# elif nilai >= 50 and nilai <= 69:
#     print("predikat = D")
# elif nilai >= 0 and nilai <= 49:
#     print("predikat = E")
# else:
#     print("nilai tidak valid")

jml_siswa_masuk = int(input("Masukkan jumlah siswa yang masuk: "))

if jml_siswa_masuk > 20:
    print('Kelas penuh')
    terlambat = input("Apakah ada siswa yang terlambat? (Y/n): ")
    if terlambat.lower() == 'y':
        print("Siswa yang terlambat akan dihukum")
    else:
        print("Siswa yang datang tepat waktu akan mendapatkan hadiah")
else:
    print("Kelas kurang")
