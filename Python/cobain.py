# PROGRAM PYTHON LENGKAP

print("=" * 50)
print("DASAR DASAR PEMROGRAMAN")
print("=" * 50)

# 1. PROFIL PRIBADI
print("\n1. PROFIL PRIBADI")
print("-" * 20)

nama = "Mufarid Adnan"
nim = "0110125062"
kelas = "SI001"
no_telp = "089687231733"
alamat = "Kp sawah rt003/008, Bojonggede Bogor"

print(f"Nama    : {nama}")
print(f"NIM     : {nim}")
print(f"Kelas   : {kelas}")
print(f"No Telp : {no_telp}")
print(f"Alamat  : {alamat}")

# 2. PROFIL TEMAN
print("\n2. PROFIL TEMAN SAYAA")
print("-" * 20)

nama_teman = "Akmal Ikram Khairullah"
nim_teman = "0110125128"
kelas_teman = "SI001"
no_telp_teman = "087811957988"
alamat_teman = "Tajurhalang perum graha tama indah3, Bogor"

print(f"Nama    : {nama_teman}")
print(f"NIM     : {nim_teman}")
print(f"Kelas   : {kelas_teman}")
print(f"No Telp : {no_telp_teman}")
print(f"Alamat  : {alamat_teman}")

# 3. BERAT BADAN IDEAL
print("\n3. PROGRAM BERAT BADAN IDEAL")
print("-" * 30)

tinggi_badan = float(input("Masukkan tinggi badan anda: "))
jenis_kelamin = input("Masukkan jenis kelamin anda (L/P): ").upper()

if jenis_kelamin == "L":
    berat_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.1)
else:
    berat_ideal = (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.15)

print(f"Berat Badan Ideal: {berat_ideal:.2f} kg")

# 4. KONVERSI CELCIUS KE FAHRENHEIT
print("\n4. PROGRAM KONVERSI SUHU")
print("-" * 25)

celcius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = (celcius * 9/5) + 32
print(f"{celcius}°C = {fahrenheit:.2f}°F")

# 5. LUAS DAN KELILING TABUNG
print("\n5. PROGRAM TABUNG")
print("-" * 20)

import math

jari_jari = float(input("Masukkan jari-jari tabung (7cm): "))
tinggi = float(input("Masukkan tinggi tabung (cm): "))

luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi)
volume = math.pi * (jari_jari ** 2) * tinggi
keliling_alas = 2 * math.pi * jari_jari

print(f"Luas Permukaan: {luas_permukaan:.2f} cm²")
print(f"Volume: {volume:.2f} cm³")
print(f"Keliling Alas: {keliling_alas:.2f} cm")

print("\n" + "=" * 50)
print("PROGRAM SELESAI")
print("=" * 50)