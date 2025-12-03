nilai1 = int(input("Masukkan angka pertama: "))
nilai2 = int(input("Masukkan angka kedua: "))

operator = input("Masukkan operator (tambah, kurang, kali, bagi, pangkat): ")

if operator == "tambah":
    hasil = nilai1 + nilai2

elif operator == "kurang":
    hasil = nilai1 - nilai2

elif operator == "kali":
    hasil = nilai1 * nilai2

elif operator == "bagi":
    hasil = nilai1 / nilai2

elif operator == "pangkat":
    hasil = nilai1 ** nilai2

else:
    hasil = "Operator tidak valid"

print("Angka pertama :", nilai1)
print("Angka kedua :", nilai2)
print("pilihan operator :", operator)   
print("Hasil :", nilai1, operator, nilai2, "=", hasil)