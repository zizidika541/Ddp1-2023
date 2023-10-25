kendaraan = ["Suzuki R3","Mobil","1462 cc","Putih","4 roda"]
print(kendaraan)

#dari program diatas ditambahkan: diakhir (harga kendaraan dan tipe kendaraan), stelah jenis kendaraan(merk kendaraan)

kendaraan.append("262 juta")
kendaraan.append("otomatis")
kendaraan.insert(2,"Suzuki")
print("kendaraan ini saya gunakan untuk pergi kekampung halaman")
print(kendaraan)

#menghitung luas bangun datar

menghitung = input("PILIH OPERASI: \n 1.hitung luas persegi \n 2.hitung luas lingkaran \n 3.hitung luas segitiga")
match menghitung:
    case "1":
        sisi=int (input("masukan nilai sisi"))
        luas= sisi*sisi
        print(luas)
    case "2":
        jari_jari =int (input("masukan nilai jari-jari: "))
        luas = 3.14*jari_jari*jari_jari
        print(luas)
    case "3":
        alas=int (input("masukan nilai alas: "))
        tinggi=int (input("masukan nilai tinggi: "))
        luas = alas*tinggi
        print(luas)
    case _:
        print("salah pilih")
