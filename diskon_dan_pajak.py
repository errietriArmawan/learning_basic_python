# Pajak PPN 11%
ppn = 11 / 100

# Input total belanjaan
total_harga = int(input("Masukkan Total Belanjaan: "))
diskon = 0
isDiskon = False

# Menentukan besar diskon berdasarkan total belanja
if total_harga >= 300000:
    diskon = 15
    isDiskon = True
elif total_harga >= 200000:
    diskon = 10
    isDiskon = True
elif total_harga >= 120000:
    diskon = 7
    isDiskon = True

# Tampilan hasil perhitungan
print("\n-----------------------------")
print(f"Total Harga Awal: Rp {total_harga:,}")

if isDiskon:
    dapat_diskon = total_harga * diskon / 100
    harga_setelah_diskon = total_harga - dapat_diskon
    harga_pajak = harga_setelah_diskon * ppn
    harga_final = harga_setelah_diskon + harga_pajak

    print(f"Diskon: {diskon}%")
    print(f"Potongan Harga: Rp {dapat_diskon:,.0f}")
    print(f"Harga Setelah Diskon: Rp {harga_setelah_diskon:,.0f}")
    print(f"PPN 11%: Rp {harga_pajak:,.0f}")
    print(f"Total Bayar: Rp {harga_final:,.0f}")
else:
    harga_pajak = total_harga * ppn
    harga_final = total_harga + harga_pajak

    print("Tidak dapat diskon.")
    print(f"PPN 11%: Rp {harga_pajak:,.0f}")
    print(f"Total Bayar: Rp {harga_final:,.0f}")
