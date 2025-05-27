#aritmatika sederhana
'''
    Penjumlahan
    Pengurangan 
    Perkalian
    Pembagian
'''
'''
a = int(input("Masukan angka pertama\t: "))
b = int(input("Masukan angka kedua\t: "))

print("Output\nPenjumlahan","\t=", a+b, "\nPengurangan","\t=",a-b, "\nPerkalian","\t=",a*b, "\nPembagian","\t=",a/b)
'''

#Mengitung luas Persegi
'''
sisi = int(input("Masukan Panjang sisi persegi = "))
luas = sisi * sisi

print("Luas Persegi =", luas)  # Output: Luas Persegi = 16
'''
#menghitung luas lingkaran
'''
phi = 3.14
r = int(input("Masukan panjang jari-jari = "))
keliling = 2 * phi * r
luas = phi * r * r

print("Keliling Lingkaran = ", keliling, "\nLuas Lingkaran = ",luas)  # Output: Keliling Lingkaran =  18.5
'''

'''
#Menghitung konversi suhu celcius ke fahrenheit
celcius = int(input("Masukan Suhu Celcius = "))
fahrenheit = (celcius * (9/5)) + 32

print("Suhu Fahrenheit =", fahrenheit)  # Output: Suhu Fahrenheit =
'''

detik = int(input("masukan detik = "))
menit = detik // 60
detikLebih = detik % 60

print(detik,"detik =",menit,"menit",detikLebih,"detik")  # Output: