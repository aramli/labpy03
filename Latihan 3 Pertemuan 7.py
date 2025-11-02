saldo = 100000

while True:
    print(f"""
==============================
Saldo anda sisa : Rp {saldo}
1. Tarik uang
2. Keluar
==============================
""")
    pilih = int(input("Pilih menu (1/2) : "))

    if pilih == 1:
        if saldo > 0:
            tarik = int(input("Masukkan jumlah penarikan : "))
            if tarik <= saldo:
                saldo -= tarik
                print("Penarikan berhasil.")
            else:
                print("Maaf, saldo anda tidak mencukupi.")
        else:
            print("Maaf, saldo anda tidak mencukupi.")
    elif pilih == 2:
        print("Terima kasih telah menggunakan ATM.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")
