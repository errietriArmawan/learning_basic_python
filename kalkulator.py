bil1 = int(input("masukan bil1 = "))
operasi = input("Pilih operasi ( + , - , * , / , % )= ")
bil2 = int(input("masukan bil2 = "))


if operasi == "+":
    print(bil1 + bil2)
elif operasi == "-":
    print(bil1 - bil2)
elif operasi == "*":
    print(bil1 * bil2)
elif operasi == "/":
    print(bil1 / bil2)
elif operasi == "%":
    print(bil1 % bil2)
else:
    print("harap masukan operasi  ( + , - , * , / , % ) ")            