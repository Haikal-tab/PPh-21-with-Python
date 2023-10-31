print("---PERHITUNGAN PPH 21 (1721-A1)---", "\n")

income_per_bulan = float(input(f"Masukkan Income per Bulan Anda: Rp"))
income_1_tahun = income_per_bulan*12
print(f"Penghasilan Anda 1 tahun: Rp{income_1_tahun:,}", "\n", "\n")


print("---PENAMBAH PENGHASILAN BRUTO (per tahun)---","\n")

print("TUNJANGAN PPh, 6% dari gaji per bln")
tunjangan_1_bulan = income_per_bulan*(6/100)
print(f"Tunjangan Per Bulan: Rp{tunjangan_1_bulan:,.0f}")
tunjangan_1_tahun = tunjangan_1_bulan*12
print(f"Tunjangan Per Tahun: Rp{tunjangan_1_tahun:,.0f}", "\n")


print("TUNJANGAN Lainnya/uang lembur, 3% dari gaji per bln")
tunjangan_lainnya_1_bulan = income_per_bulan*(3/100)
print(f"Tunjangan Lainnya per Bulan: Rp{tunjangan_lainnya_1_bulan:,.0f}")
tunjangan_lainnya_1_tahun = tunjangan_lainnya_1_bulan*12
print(f"Tunjangan Lainnya Per Tahun: Rp{tunjangan_lainnya_1_tahun:,.0f}", "\n")


print("Premi Asuransi, 5% dari gaji per bln")
premi_asuransi_1_bulan = income_per_bulan*(5/100)
print(f"Premi Asuransi per Bulan: Rp{premi_asuransi_1_bulan:,.0f}")
premi_asuransi_1_tahun = premi_asuransi_1_bulan*12
print(f"Premi Asuransi Per Tahun: Rp{premi_asuransi_1_tahun:,.0f}", "\n")


print("Tantiem/Bonus/THR, 3% dari gaji per bln")
bonus_1_bulan = income_per_bulan*(3/100)
print(f"Bonus per Bulan: Rp{bonus_1_bulan:,.0f}")
bonus_1_tahun = bonus_1_bulan*12
print(f"Bonus Per Tahun: Rp{bonus_1_tahun:,.0f}","\n")


total_penghasilan_kotor_1_th = income_1_tahun + tunjangan_1_tahun + tunjangan_lainnya_1_tahun + premi_asuransi_1_tahun + bonus_1_tahun 
print(f"Total Penghasilan Kotor dalam 1 Tahun: Rp{total_penghasilan_kotor_1_th:,.0f}", "\n", "\n")



print("---PENGURANG PENGHASILAN BRUTO (per tahun)---", "\n")

print("Iuran Pensiun, 7% dari gaji per bln")
iuran_pensiun_1_bulan = income_per_bulan*(7/100)
print(f"Iuran Pensiun per Bulan: Rp{iuran_pensiun_1_bulan:,.0f}")
iuran_pensiun_1_tahun = iuran_pensiun_1_bulan*12
print(f"Iuran Pensiun per Tahun: Rp{iuran_pensiun_1_tahun:,.0f}", "\n")

# iuran_pensiun_per_bln = income_per_bulan*(1/100)
# print("Iuran Pensiun per Bulan Anda (3% dari gaji perbln, tp yg mengurangi penghasilan adalah 1%): ", iuran_pensiun_per_bln)

# Utk iuran pensiun, 3% terdiri dari: 1% ditanggung oleh si pekerja, 2% ditanggung oleh perusahaan
# 1% mengurangi penghasilan, sedangkan 2% nya tanpa mengurangi penghasilan

# iuran_pensiun_per_th = iuran_pensiun_per_bln*12
# print("Iuran Pensiun per Tahun Anda: ", iuran_pensiun_per_th, "\n")



# iuran_jht_per_bulan = income_per_bulan*(2/100)
# print("Iuran Jaminan Hari Tua per Bulan Anda (2% mengurangi penghasilan, sedangkan 3.7% nya tanpa mengurangi penghasilan): ", iuran_jht_per_bulan)

# Utk iuran JHT, 5.7% terdiri dari: 2% ditanggung pekerja, 3.7% ditanggung perusahaan
# 2% mengurangi penghasilan, sedangkan 3.7% nya tanpa mengurangi penghasilan

# iuran_jht_per_th = iuran_jht_per_bulan*12
# print("Iuran JHT per Tahun Anda: ", iuran_jht_per_th, "\n")

print("Biaya Jabatan, 5% dari gaji per bulan")
biaya_jabatan = total_penghasilan_kotor_1_th*(5/100)
x = int(6000000)

if biaya_jabatan >= x:
    print("Biaya Jabatan per Tahun: ", int(6000000),"\n","\n")
    
elif biaya_jabatan < x:
    print("Biaya Jabatan per Tahun: ", int(total_penghasilan_kotor_1_th*(5/100)),"\n","\n")



# print("---Biaya Jabatan---", "\n")
# nett_income = total_penghasilan_kotor_1_th-iuran_pensiun_per_th-iuran_jht_per_th-tunjangan_1_tahun
# y = int(6000000)

# if biaya_jabatan >= y:
#     print("Nett Income per Tahun Sebesar: ", nett_income-y)
# elif biaya_jabatan < y:
#     print("Nett Income per Tahun Sebesar: ", nett_income-int(total_penghasilan_kotor_1_th*(5/100)))
# print(" ")

print("---Jumlah Pengurang Gaji Kotor (per tahun)---", "\n")
# i = biaya_jabatan
o = float(input("Masukkan Biaya Jabatan Anda: "))
# jumlah = iuran_pensiun_1_tahun + i
jumlah = iuran_pensiun_1_tahun + o
print(f"Jumlah Pengurangnya: Rp{jumlah:,.0f}", "\n")

nett_income = total_penghasilan_kotor_1_th - jumlah
print(f"Total Penghasilan Bersih dalam 1 Tahun: Rp{nett_income:,.0f}", "\n", "\n" )



print("---PTKP---")
print(f"(dalam juta rupiah)", "\n")

z = float(input("Masukkan Tanggungan Anda (isi '4' jika Anda bukan Tidak Kawin): " ))

print("-----Pria/Wanita Tidak Kawin-----")
if z == 0:
    print(int(54*1000000),"\n")
elif z == 1:
    print(float(58.5*1000000),"\n")
elif z == 2:
    print(int(63*1000000),"\n")
elif z == 3:
    print(float(67.5*1000000),"\n")
else: 
    print("Status Anda bukan Pria/Wanita Tidak Kawin \n")



a = float(input("Masukkan Tanggungan Anda (Isi '4' jika Anda bukan Pria Kawin):"))

print("-----Pria Kawin-----")
if a==0:
    print(float(58.5*1000000),"\n")
elif a==1:
    print(int(63*1000000),"\n")
elif a==2:
    print(float(67.5*1000000),"\n")
elif a==3:
    print(int(72*1000000),"\n")
else: 
    print("Status Anda Bukan Pria Kawin \n")



b = float(input("Masukan Tanggungan Anda (Isi '4' jika Anda bukan Suami & Istri Digabung):"))

print("-----Suami & Istri Digabung-----")
if b==0:
    print(float(112.5*1000000),"\n")
elif b==1:
    print(int(117*1000000),"\n")
elif b==2:
    print(float(121.5*1000000),"\n")
elif b==3:
    print(int(126*1000000),"\n")
else:
    print("Status Anda Bukan Suami & Istri Digabung \n \n")




print("---Penghitungan Penghasilan Kena Pajak (PKP)---\n") 
input_ptkp = float(input("Masukkan PTKP: Rp"))
print(f"PTKP Anda: Rp{input_ptkp:,.0f}")
pkp = nett_income - input_ptkp
print(f"PKP Anda: Rp{pkp:,.0f}", "\n")


print(f"Nilai Maks. Lapisan ke-1: 60,000,000")
print(f"Nilai Maks. Lapisan ke-2: 250,000,000")
print(f"Nilai Maks. Lapisan ke-3: 500,000,000")
print(f"Nilai Maks. Lapisan ke-4: 5,000,000,000\n")

print("---ALOKASI TARIF PROGRESIF---\n")
number_1 = float(input("Masukkan PKP: Rp"))
number_2 = float(input("Nilai Maks. Lapisan ke-1: Rp"))
number_3 = float(input("Nilai Maks. Lapisan ke-2: Rp"))
number_4 = float(input("Nilai Maks. Lapisan ke-3: Rp"))
number_5 = float(input("Nilai Maks. Lapisan ke-4: Rp"))
print(" ")



# Perhitungan PKP untuk Lapisan ke-1
if pkp >= number_1 :
    print(f"Nilai lapisan ke-1: Rp{number_2:,.0f}")
elif pkp < number_2:
    print(f"Nilai untuk lapisan ke-1: Rp{pkp:,.0f}")


hasil_alokasi_1 = number_1 - number_2
print(f"Nilai untuk lapisan ke-2: Rp{hasil_alokasi_1:,.0f}")

hasil_alokasi_2 = number_2 - number_3
print(f"Nilai untuk lapisan ke-3: Rp{hasil_alokasi_2:,.0f}")

hasil_alokasi_3 = number_3 - number_4
print(f"Nilai untuk lapisan ke-4: Rp{hasil_alokasi_2:,.0f}")

hasil_alokasi_4 = number_5 - 0
print(f"Nilai untuk lapisan ke-5: Rp{hasil_alokasi_2:,.0f}", "\n")

print(f"*Note = Jika nilainya negatif(minus) tidak masuk ke tarif progresif\n\n")


print("---TARIF PROGRESIF--- \n")


print("Lapisan Penghasilan Kena Pajak:")

print("1 : Rp0-Rp60 jt        = 5%")
print("2 : >60 jt-Rp250 jt    = 15%")
print("3 : >Rp250 jt-Rp500 jt = 25%")
print("4 : >Rp500 jt-Rp5 M    = 30%")
print("5 : >Rp5 M             = 35% \n")




hitung_pkp_1= float(input("Masukkan PKP (Lapisan 1), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_1 = hitung_pkp_1*(5/100)
if hitung_pkp_1 == 0:
    print("Selesai")
elif hitung_pkp_1 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_1:,.0f}")

print(" ")



hitung_pkp_2= float(input("Masukkan PKP (Lapisan 2), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_2 = hitung_pkp_2*(15/100)
if hitung_pkp_2 == 0:
    print("Selesai")
elif hitung_pkp_2 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_2:,.0f}")

print(" ")



hitung_pkp_3= float(input("Masukkan PKP (Lapisan 3), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_3 = hitung_pkp_3*(25/100)
if hitung_pkp_3 == 0:
    print("Selesai")
elif hitung_pkp_3 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_3:,.0f}")

print(" ")



hitung_pkp_4= float(input("Masukkan PKP (Lapisan 4), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_4 = hitung_pkp_4*(30/100)
if hitung_pkp_4 == 0:
    print("Selesai")
elif hitung_pkp_3 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_4:,.0f}")

print(" ")



hitung_pkp_5= float(input("Masukkan PKP (Lapisan 5), (ketik '0' jika lapisan Anda tdk sampai di sini): "))
hasil_5 = hitung_pkp_5*(35/100)
if hitung_pkp_5 == 0:
    print("Selesai")
elif hitung_pkp_3 > 1:
    print(f"Pajak per Tahun Anda: Rp{hasil_5:,.0f}")

print(" ")

print(f"===Pajak Terutang per Tahun===")

angka_1 = float(input("Masukkan lapisan 1: "))
angka_2 = float(input("Masukkan lapisan 2: "))
angka_3 = float(input("Masukkan lapisan 3: "))
angka_4 = float(input("Masukkan lapisan 4: "))
angka_5 = float(input("Masukkan lapisan 5: "))
print(" ")


hasil_pajak = angka_1 + angka_2 + angka_3 + angka_4 + angka_5
print(f"Pajak Terutang per Tahun: Rp{hasil_pajak:,.0f}")

    


# nilai = float(input("Masukkan Pajak Anda per Tahun: "))
result = hasil_pajak/12
print(f"Pajak Terutang per Bulan: Rp{result:,.0f} \n")
print(f"Selesai \n")


print("CREATED BY: MUHAMMAD HAIKAL MUTHAHHARI")
print("#ayobayarpajak!")


















