def lihat_tugas(daftar_tugas):
    if len(daftar_tugas) == 0:
        print("Anda belum punya tugas")
    else:
        print("Berikut tugas Anda:")
        nomor = 1
        for dt in daftar_tugas:
            print(nomor, dt)
            nomor += 1

def tambah_tugas(daftar_tugas, tugas_baru):
    daftar_tugas.append(tugas_baru)
    print(f"Anda telah menambahkan tugas {tugas_baru}!")

def hapus_tugas(daftar_tugas):
    if len(daftar_tugas) == 0:
        print("Daftar Tugas kosong!")
        return
    else:
        print("Berikut daftar tugas Anda")
        nomor = 1
        for dt in daftar_tugas:
            print(nomor, dt)
            nomor += 1
        while True:
            opsi_hapus_tugas = (input("Masukan nomor tugas yang akan dihapus (Masukan 'X' untuk membatalkan): ")).lower()
            if opsi_hapus_tugas == "x":
                print("Tugas batal dihapus")
                break
            elif opsi_hapus_tugas.isdigit():
                nomor_hapus_tugas = (int(opsi_hapus_tugas)) 
                if 1 <= nomor_hapus_tugas <= len(daftar_tugas):
                    tugas_dihapus = daftar_tugas[nomor_hapus_tugas - 1]
                    del daftar_tugas[nomor_hapus_tugas - 1]
                    print(f"Tugas {tugas_dihapus} telah dihapus!")
                    break
                else:
                    print("Nomor tidak sesuai!")

daftar_tugas = []

running = True

while running:
    print("\n*** To-Do List ***")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")
    
    opsi = input("Pilih opsi (1-4): ")
    if opsi == "1":
        lihat_tugas(daftar_tugas)
    elif opsi == "2":
        tugas_baru = input("Masukan tugas baru: ")
        tambah_tugas(daftar_tugas, tugas_baru)
    elif opsi == "3":
        hapus_tugas(daftar_tugas)
    elif opsi == "4":
        print("Selamat tinggal!")
        running = False
    else:
        print("Mohon masukan angka 1-4")