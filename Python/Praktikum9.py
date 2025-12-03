#celcius_ke_fahrenheit
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))  # Output: 32.0
print(celcius_ke_fahrenheit(100))  # Output: 212.0


#is_genap
def is_genap(angka):
    return angka % 2 == 0
print(is_genap(4))  # Output: True
print(is_genap(7))  # Output: False


#lulus/tidak_lulus
def lulus(nilai):
    if nilai > 60:
        return "Lulus"
    else:
        return "Tidak Lulus"
print(lulus(80))  # Output: Lulus
print(lulus(60))  # Output: Tidak Lulus


#bialngan_ganjil_yang_ada_dalam_argument
def bilangan(angka):
    for i in range(1, angka):
        if i % 2 != 0:
            print(i , end=', ')

bilangan(50)  # Output: 1,2,3,...,49 (hanya bilangan ganjil)
