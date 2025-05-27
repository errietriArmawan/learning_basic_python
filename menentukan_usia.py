
tahun_skrng = 2025
tahun_lahir = int(input("masukan tahun_lahir = "))
usia = tahun_skrng - tahun_lahir
print("umur anda sekarang", usia, "tahun")


if usia < 0:
    print("usia tidak valid")
elif usia <= 12:
    print("anda termasuk kategori : anak-anak")
elif usia <= 17:
    print("anda termasuk kategori : remaja")
elif usia <= 35:
    print("anda termasuk kategori : Dewasa")
elif usia <= 49:
    print("anda termasuk kategori : Orang Tua")
else:
    print("anda termasuk kategori : Lansia")