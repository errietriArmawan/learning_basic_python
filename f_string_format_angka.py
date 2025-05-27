
# var:.nf (menampilkan jumlah angka dibelakang koma)
phi = 3.14568786

print(f" phi = {phi:.3f}")
print("====================")
#memberikan pembatas pada nilai harga
harga = 1000000

print(f"harga = Rp.{harga:,}")
print("====================")
#menampilkan dalam format persentase%
diskon = 0.50

print(f"dapat diskon = {diskon:.2%}" )

#menampilkan angka dalam bentuk lainya
print("====================")
angka = 21

print(f"desimal = {angka}")
print(f"binner = {angka:b}")
print(f"oktal = {angka:o}")
print(f"hexadesimal kecil = {angka:x}")
print(f"hexadesimal besar = {angka:X}")

#mengatur teks
nama = "python"

print(f"Nama {nama:>10}")
print(f"Nama {nama:<10}")
print(f"Nama {nama:^10}")