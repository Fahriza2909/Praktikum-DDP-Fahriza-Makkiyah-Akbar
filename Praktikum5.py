# Jenis Kendaraan

list = ["Motor","Kopling", 155 ,"Hitam","2"]
list.append (40000000)
list.append("Sport")
list.insert(2, "Yamaha")

print(list)

# Menghitung Luas Bangun Datar

pilihan = int(input (
"""
==================================
selamat datang di mari menghitung
==================================
1 Luas Persegi 
2 Luas Lingkaran
3 luas segitiga 
apa yang ingin anda cari ? """))

match pilihan :
    case 1 :
        sisi = int(input("Masukkan sisi persegi "))
        total = sisi * sisi
        print ("luas persegi adalah ", total)

    case 2 :
        jari_jari = int(input("masukkan jari jari "))
        total = 3.14 * jari_jari * jari_jari
        print ("luas lingkaran adalah", total )
    case 3 :
        alas = int(input("masukkan alas "))
        tinggi = int(input("masukkan tinggi "))
        total = 1/2 * alas * tinggi
        print ("luas Segitia adalah ", total)

    case _ :
        print ("gatau kenapa mas")