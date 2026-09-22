# JAWABAN UNTUK SOAL NOMOR 1

#--

#Diketahui
Total_Jarak_Ditempuh = 325.5
efisiensi_bahan_bakar_liter = 8.0

#Menghitung total bahan bakar yang dihabiskan
total_bahan_bakar = Total_Jarak_Ditempuh / efisiensi_bahan_bakar_liter
print("Total bahan bakar yang dihabiskan adalah: ", f"{total_bahan_bakar:.2f}", "liter")

#JAWABAN UNTUK SOAL NOMOR 2

#--

#Diketahui
waktu_perjalanan_kurir = 435 #dalam menit

#Menghitung waktu perjalanan dalam jam 
waktu_perjalanan_jam = waktu_perjalanan_kurir // 60
print("Waktu perjalanan kurir dalam jam adalah: ", f"{waktu_perjalanan_jam:.2f}", "jam")

#Menghitung Sisa Menit
waktu_perjalanan_sisa_menit = waktu_perjalanan_kurir % 60
print("Sisa menit perjalanan kurir adalah: ", waktu_perjalanan_sisa_menit, "menit")


#JAWABAN UNTUK SOAL NOMOR 3

#--

#Diketahui
target_paket  = 42
insentif_per_paket = 3500
bonus_kerajinan = 50000 #Dalam Rupiah

#Menghitung total insentif
total_insentif = (target_paket * insentif_per_paket) 
print("Total insentif yang diterima kurir adalah: ", f"Rp {total_insentif:,.0f}".replace(",", "."))

#Menghitung Pendapatan Akhir
total_pendapatan_akhir = total_insentif + bonus_kerajinan
print("Total pendapatan akhir kurir adalah: ", f"Rp {total_pendapatan_akhir:,.0f}".replace(",", "."))
