# Jawaban untuk Soalan Nomor 1

berat_cucian = [3, 2, 5, 2] # Berat cucian dalam kg
total_berat = 0

for berat in berat_cucian :
    total_berat = total_berat + berat

print(total_berat)

#Jawaban untuk Soalan Nomor 2
playlist_lagu = ["Fix You", "Yellow", "Sparks", "Viva La Vida"]

for i in range (len(playlist_lagu)):
    Nomor = i + 1
    Nama = playlist_lagu[i]
    print("Nomor Urut:", Nomor, "Nama Lagu:", Nama)

#Jawaban untuk Soalan Nomor 3
antrean_tiket = ["Reguler", "Refund", "VIP", "Tiket Palsu", "Reguler"]

for tiket in antrean_tiket:
    
    
    if tiket == "Refund":
        print("Tiket sudah dikembalikan, lewati")  
        continue                                  
        
    
    elif tiket == "Tiket Palsu":
        print("BAHAYA: Penyusup terdeteksi! Sistem dimatikan.") 
        break                                                   
        
    
    else:
        print("Silakan masuk, tiket Anda:", tiket) 

print("==== PROSES SELESAI ===")