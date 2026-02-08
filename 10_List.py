# List bisa berisi string,angka,dan campur
buah =['Apel', 'Mangga', 'Pisang'] # index dimulai dari  0
buah[1] = 'Jeruk' # Mengubah isi list

print(buah[0]) # Menampilkan Apel
print(buah[1])

buah.append('anggur') # Menambahkan di list terakhir
buah.insert(1, 'nanas') # Menambahkan di posisi tertentu

print(buah)
# buah.remove('Apel') # Menghapus dengan string dan int
# del  buah[1] # Menghapus berdasarkan index
# buah.pop(0) # Menghapus berdasarkan index dan bisa dikembalikan datannya

