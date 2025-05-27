# jml_angka = int(input("Masukan Jumlah angka = "))
# total = 0
# for i in range(jml_angka):
#     angka = int(input(f"Angka ke {i + 1} = "))
#     total += angka

# rata_rata = total / jml_angka
# print(f"total = {total}")
# print(f"rata-rata = {rata_rata}")

jml_angka = int(input("Masukan Jumlah angka = "))
total = 0
i = 0
while i < jml_angka:
    angka = int(input(f"Angka ke {i + 1} = "))
    total += angka
    i += 1
rata_rata = total / jml_angka
print(f"total = {total}")
print(f"rata-rata = {rata_rata}")