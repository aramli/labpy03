modal_awal = 100000000
total_laba = 0

print("Laporan Laba Usaha Selama 8 Bulan")
print("----------------------------------")

for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba_bulan = 0
    elif bulan == 3 or bulan == 4:
        laba_bulan = modal_awal * 0.01
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba_bulan = modal_awal * 0.05
    elif bulan == 8:
        laba_bulan = modal_awal * 0.03

    print("Laba bulan ke-",bulan," : ",laba_bulan)
    total_laba += laba_bulan

print("----------------------------------")
print("Total laba selama 8 bulan :",total_laba)
