# Program Klasifikasi Usia

# 1. TODO: Baca input dari pengguna
umur = int(input("berapa umur anda: "))

# 2. TODO Tentukan kategori berdasarkan usia
if umur < 12:
    print("kategori anak-anak")
elif umur < 17:
    print("kategori: Remaja")
elif umur < 59:
    print("kategori: dewasa")
else:
    print("kategori: lansia")