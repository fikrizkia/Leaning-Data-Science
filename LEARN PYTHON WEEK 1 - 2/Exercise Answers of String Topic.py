#Jawaban Soalan Nomor 1
import string

raw_data = "   22-Sept-2026_TOTTY COFFEE_  cappuccino   _Rp35.000,-   "
cleaned_data = raw_data.strip().replace("_", "|").replace("_", "|").replace("_", "|").replace("Rp", " ").replace(",-", " ").upper()

cleaned_data = cleaned_data.replace("  ", "")

print(cleaned_data)

#Jawaban Soalan Nomor 2
import string

username = "  Data_Science_Pro  "
kampus = " Universitas muhammadiyah yogyakarta "

username_cleaned = username.strip().replace("_", "-").title()
kampus_cleaned = kampus.strip().replace(" ", "-").title()

gabungan_kalimat= username_cleaned + kampus_cleaned

print(gabungan_kalimat)

#Jawaban Soalan Nomor 3
import string

Data_mentah_scrapping = "   [makan_malam] >>> ayam geprek agas ::: 650 KALORI  "

cleaned_data_scrapping = Data_mentah_scrapping.strip().replace("[", "").replace("]", "").replace(">>>", ":").replace(":::", "").replace("650", "").replace("KALORI", "(650 kalori)").upper()
cleaned_data_scrapping = cleaned_data_scrapping.replace("  ", "")

print(cleaned_data_scrapping)