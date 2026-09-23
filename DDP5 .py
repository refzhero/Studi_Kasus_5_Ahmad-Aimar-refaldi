def biaya_parkir(jenis_kendaraan, durasi_parkir):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000
    else:
        return 0

    total_parkir = tarif * durasi_parkir
    return total_parkir


jenis_kendaraan = input("masukkan jenis kendaraan motor/mobil: ")
jam_masuk = int(input("masukkan jam masuk: "))
jam_keluar = int(input("masukkan jam keluar: "))

durasi_parkir = jam_keluar - jam_masuk

total_biaya = biaya_parkir(jenis_kendaraan, durasi_parkir)

print("===== PARKIR =====")
print("jenis kendaraan: ", jenis_kendaraan)
print("Jam masuk: ", jam_masuk)
print("Jam keluar: ", jam_keluar)
print("lama parkir: ", durasi_parkir)
print("total parkir: ", total_biaya)



