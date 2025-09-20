tugas = []

running = True

while running:
    print("\n*** To-Do List ***")
    print("1. Lihat tugas")
    print("2. Tambah tugas")
    print("3. Hapus tugas")
    print("4. Keluar")
    
    opsi = input("Pilih opsi (1-4): ")
    if opsi == "1":
        if len(tugas) == 0:
            print("Anda belum punya tugas")
        else:
            print("Berikut tugas Anda:")
            nomor = 1
            for lt in tugas:
                print(nomor, lt)
                nomor += 1
    elif opsi == "2":
        tugas_baru = input("Masukan tugas baru: ")
        tugas.append(tugas_baru)
        print(f"Anda telah menambahkan tugas {tugas_baru}!")
    elif opsi == "3":
        if len(tugas) == 0:
            print("Anda belum punya tugas!")
        else:
            print("Berikut tugas Anda:")
            nomor = 1
            for lt in tugas:
                print(nomor, lt)
                nomor += 1
            while True:
                opsi_hapus_tugas = (input("Masukan nomor tugas yang akan dihapus: (Ketik 'x' untuk membatalkan)")).lower()
                if opsi_hapus_tugas == "x":
                    print("Tugas batal dihapus")
                    break
                elif opsi_hapus_tugas.isdigit():
                    nomor_hapus_tugas = int(opsi_hapus_tugas)
                    if 1 <= nomor_hapus_tugas <= len(tugas):
                        del tugas[int(nomor_hapus_tugas-1)]
                        print("Tugas telah dihapus!")
                        break
                else:
                    print("Nomor tidak sesuai")
    elif opsi == "4":
        print("Selamat tinggal!")
        running = False
    else:
        print("Mohon masukan angka 1-4")