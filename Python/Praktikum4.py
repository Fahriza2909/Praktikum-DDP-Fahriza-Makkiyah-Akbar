#soal 1: Bilangan Genap atau ganjil

bilangan = int(input("masukkan bilangan "))

if bilangan % 2 == 0:   
    print(bilangan, "adalah bilangan genap")
else:
    print(bilangan, "adalah bilangan ganjil")

#Soal 2: Nilai Ujian

nilai = int(input("masukkan nilai ujian "))

if nilai >= 75 :
    print ("Lulus")
else:
    print("Tidak Lulus")

#Soal 3: Konversi Nilai

umur= int(input("masukkan umur anda "))

if umur >= 18 :
    print("Dewasa")
elif umur >= 13 and umur <= 17 :
    print("remaja")
else:
    print("Anak-anak")

#Soal 4: Cek Keanggotaan

warna = input("masukkan warna favorit anda ")

if warna == "gold" or warna == "silver" :
    print ("Selamat anda mendapatkan diskon")
else :
    print("Maaf, anda tidak mendapatkan diskon")

#Soal 5: Pembelian Diskon

jumlah_beli = int(input("masukkan jumlah pembelian "))

print("selamat anda dapat diskon 10%") if jumlah_beli > 100 else print("maaf anda tidak mendapatkan diskon")