# Jawaban Soalan Nomor 1

def kasir_nostra (Harga_gelas, jumlah_pesanan):
    total_harga = Harga_gelas * jumlah_pesanan
    return total_harga

total_dibayar = kasir_nostra (50000, 2)

print ("TOTAL PEMBAYARAN :", total_dibayar)


#Jawaban Soalan Nomor 2

def cek_pembelian_game (saldo_wallet, harga_game):
    pembelian = saldo_wallet - harga_game

    if saldo_wallet >= harga_game:
        return "Berhasil Beli"

    else: 
        return "Saldo Kurang"

saldo_saya = 50000
harga_game = 10000

pembelian_game = cek_pembelian_game (50000, 10000)

print("Status Pembelian : ", pembelian_game)

#Jawaban Soalan Nomor 3

def rekap_struk (daftar_struk):
    total = 0

    for struk in daftar_struk :
     total = total + struk
    return total

rekapan_warmindo = [15000, 12000, 18000, 20000]

total_minggu_ini = rekap_struk (rekapan_warmindo)

print ("TOTAL WARMINDO MINGGU INI :", total_minggu_ini)