i = 1
batas = int(input(" Masukan Batas = " ))
while i <= batas:
# for i in range(1, 6):
    angka = int(input(f"Angka ke-{i} = "))
    if i == 1:
        maks = angka
        min = angka
    else:
        if angka > maks:
            maks = angka
        if angka < min:
            min = angka
    i += 1
print(f"Nilai Max: {maks}")
print(f"Nilai Min: {min}")
