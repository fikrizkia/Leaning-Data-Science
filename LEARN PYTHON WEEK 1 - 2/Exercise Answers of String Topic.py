import string

kota_pelanggan_1 = "   jakarta pusat "
kota_pelanggan_2 = "bandung"
kota_pelanggan_3 = "  SURABAYA BARAT  "
kota_pelanggan_4 = "yogyakarta"

# Menghapus spasi di awal dan akhir string
bersih_kota_1 = kota_pelanggan_1.strip().upper()
bersih_kota_2 = kota_pelanggan_2.strip().upper()
bersih_kota_3 = kota_pelanggan_3.strip().upper()
bersih_kota_4 = kota_pelanggan_4.strip().upper()

# Menggabungkan semua kota 
kota_dituju = [bersih_kota_1, bersih_kota_2, bersih_kota_3, bersih_kota_4]

print("Daftar kota tujuan pelanggan:")
for huruf, kota in zip(string.ascii_uppercase, kota_dituju):
    print(f"{huruf}. {kota}")