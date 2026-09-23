#JAWABAN KASUS NOMOR 1

antrean_cucian = ["Baju Harian", "Celana Jeans", "Selimut"]
cucian_tambahan = ["Jaket", "Sprei"]

#MENYISIPKAN SERAGAM KERJA DI ANTREAN CUCIAN
antrean_cucian.insert(0, "Seragam Kerja")

#PENGGABUNGAN LIST CUCI
antrean_cucian = antrean_cucian + cucian_tambahan

# MESIN CUCI BERBUNYI BAJU HARIAN SUDAH SELESAI
antrean_cucian = antrean_cucian [1:]

#CEK JAKET APAKAH MASUK KE DALAM ANTREAN CUCIAN
print("STATUS JAKET :", "Jaket" in antrean_cucian)

#CEK DAFTAR ANTREAN CUCIAN
print("DAFTAR ANTREAN CUCIAN:", antrean_cucian)

#JAWABAN KASUS NOMOR 2
batch_1 = ["<HEADER_API>", "Data_A", "Data_B", "Data_C", "<FOOTER_API>"]
batch_2 = ["Data_D", "Data_E", "<ERROR_TIMEOUT>"]

#MENGHILANGKAN HEADER API DAN FOOTER API
batch_1 = batch_1[1:4]

#MENGHILANGKAN ERROR TIMEOUT
batch_2 = batch_2[:-1]

#Menyisipkan Data kalibrasi antara DATA_C dan DATA_D
batch_2.insert(1, "dataset_final")

#Gabungan Batch 1 dan Batch 2
dataset_final = batch_1 + batch_2

#Jumlah panjang dataset_final
dataset_final_baris=len(dataset_final)

print (dataset_final)
print(dataset_final_baris)

#JAWABAN KASUS NOMOR 3
riwayat_aksi = ["Ketik 'Halo'", "Ketik 'Dunia'", "Format 'Bold'"]

#Menghilangkan format bold
riwayat_aksi = riwayat_aksi [:-1]

#Menambahkan "Ketik 'python'" ke dalam riwayat aksi
riwayat_aksi.insert(0, "Ketik 'python'")

#Menambahkan fitur widget history
widget_history = riwayat_aksi[:-2]

print(riwayat_aksi)
print(widget_history)