def profil(nama, alamat, gender, umur, hoby):
    """Menampilkan data diri"""
    print("Nama:", nama)
    print("Alamat:", alamat)
    print("Jenis Kelamin:", gender)
    print("Umur:", umur)
    print("Hobi:", hoby)


#pemanggilan
profil("Daffa Andika", "Citayam, Indonesia", "Laki-laki", 20, "Membaca, Tidur, dan Makan")
print()
print()
def kelulusan(nilai):
    """Mencari kelulusan nilai"""
    if nilai < 60:
        return "Gagal"
    elif nilai <= 70:
        return "Baik"
    elif nilai <= 80:
        return "Sangat Baik"
    else:
        return "Istimewa"


#pemanggilan
nilai = 80
print(kelulusan(nilai))
print()
print()
def bilangan_ganjil(n):
    """Mencetak bilangan ganjil dari 1 hingga n"""
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)


#pemanggilan
n = 5
bilangan_ganjil(n)