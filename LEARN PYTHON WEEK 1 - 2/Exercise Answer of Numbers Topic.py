#Jawaban Soalan Nomor 1

#Diketahui
ukuran_panjang_taman = 110.5 #Dalam Meter
lebar_panjang_taman = 55.2 #Dalam Meter

#Menghitung luas taman
luas_taman = ukuran_panjang_taman * lebar_panjang_taman
print("Luas taman adalah: ", f"{luas_taman:.2f}", "m^2")

#--

#Jawaban Soalan Nomor 2

#Diketahui
Mangga_Dibeli = 9 #Dalam Kilogram
Harga_Mangga_Per_Kg = 1.49
Uang_Dibayar = 20

#Menghitung total harga mangga
total_harga_mangga = Mangga_Dibeli * Harga_Mangga_Per_Kg
print("Total harga mangga adalah: ", f"${total_harga_mangga:.2f}")

#Menghitung Kembalian
kembalian = Uang_Dibayar - total_harga_mangga
print("Kembalian yang diterima adalah: ", f"${kembalian:.2f}")


#--

#Jawaban Soalan Nomor 3 

#Diketahui
panjang_karpet = 150 #Dalam Centimeter
harga_karpet_per_centimeter =3.50 #Dalam Dollar

#Menghitung Luas Karpet
luas_karpet = panjang_karpet * panjang_karpet
print("Luas karpet adalah: ", f"{luas_karpet:.2f}", "cm^2")

#Menghitung total harga karpet
total_harga_karpet = luas_karpet * harga_karpet_per_centimeter
print("Total harga karpet adalah: ", f"${total_harga_karpet:.2f}")

#--

#Jawaban Soalan Nomor 4

#Diketahui
id_produk = 150

#Merubah tipe data id_produk menjadi biner
id_produk_biner = bin(id_produk)
print("ID Produk dalam biner adalah: ", bin(150)[2:])
