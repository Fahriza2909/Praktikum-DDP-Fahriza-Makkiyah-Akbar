# 1 identitas saya

Nama = "Fahriza Makkiyah Akbar"
NIM = "0110125118"
Kelas = "SI-01"
Nomor_Telfon = "0895337569196"
Alamat = "JL. Garuda 5 No. 85, beji depok"

print("\n===Identitas Saya =====")
print("\nNama         :", Nama)
print("NIM          :", NIM)
print("Kelas        :", Kelas)
print("Nomor_Telfon :", Nomor_Telfon)
print("alamat       :", Alamat)

print("\n===Identitas Teman Saya =====")
# 2 identitas teman saya
Nama = "Zidan Naufal Aziz"
NIM = "0110125056"
Kelas = "SI-01"
Nomor_Telfon = "083129751350"
Alamat = "Bojonggede, Bogor"

print ("\nNama         :",Nama)
print ("NIM          :",NIM)
print ("Kelas        :",Kelas)
print ("Nomor_Telfon :",Nomor_Telfon)
print ("alamat       :",Alamat)

# 3 Berat badan ideal
tinggi_badan = float(input("\nMasukkan Tinggi Badan Anda (cm) : "))
berat_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.1)

print("\n===Berat Badan Ideal =====")
print("\nTinggi Badan Anda :",tinggi_badan,"cm")
print("Berat Badan Ideal Anda :",berat_ideal,"kg")

# 4 Konversi Celcius ke Fahrenheit

#celcius = 30
celcius = float(input("\nMasukkan Suhu Dalam Celcius : "))
fahrenheit = (celcius * 9/5) + 32
print("\n===Konversi Celcius ke Fahrenheit =====")
print("\nSuhu Dalam Celcius :",celcius,"°C")
print("Suhu Dalam Fahrenheit :",fahrenheit,"°F")

# 5 Luas dan Keliling Tabung
Jari2 =  int(input("Masukkan Jari-jari Tabung (cm) : "))
tinggi = int(input("Masukkan Tinggi Tabung (cm) : "))
# Rumus Luas Tabung
Luas = 2 * 22/7 * Jari2 + tinggi
# Rumus Keliling Tabung
keliling = 2 * 22/7 * Jari2

print("\n===Luas dan Keliling Tabung =====")
print("luas Tabung :",Luas,"cm")
print("keliling Tabung :",keliling,"cm")