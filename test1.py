daftar_angka_jadi = [i for i in range(100)]

def kurangi_3_sirkular(x):
    return (x - 3) % 10

def proses_angka(input_4digit):
    angka_str = str(input_4digit).zfill(4)

    pasangan = [
        int(angka_str[0:2]),
        int(angka_str[1:3]),
        int(angka_str[2:4])
    ]

    print(f"Pasangan dua digit: {[f'{p:02d}' for p in pasangan]}")

    pasangan_valid = [p for p in pasangan if p in daftar_angka_jadi]

    print(f"Pasangan yang valid (ada di daftar): {[f'{p:02d}' for p in pasangan_valid]}")

    tebakan = []

    for p in pasangan_valid:
        d1 = p // 10
        d2 = p % 10
        d1_baru = kurangi_3_sirkular(d1)
        d2_baru = kurangi_3_sirkular(d2)
        if d1_baru != d2_baru:
            angka_baru = d1_baru * 10 + d2_baru
            tebakan.append(angka_baru)
        else:
            print(f"Angka {d1_baru}{d2_baru} diabaikan karena digit kembar")

    print("Tebakan angka baru (setelah pengurangan sirkular dan filter kembar): ", end="")
    print(", ".join([f"{x:02d}" for x in tebakan]))

# Contoh penggunaan
angka_keluar = input("Masukkan angka 4 digit terakhir hasil lotre: ")
proses_angka(angka_keluar)
