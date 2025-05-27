baris = int(input("Masukan jumlah Baris = "))

for i in range(baris):
    print(" " * (baris - i- 1) + "*" * (2 * i) + "*")