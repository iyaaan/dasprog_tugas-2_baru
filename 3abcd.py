# Menerima input angka dari pengguna, dipisahkan dengan spasi
input_numbers = input("Masukan angka yang dipisahkan dengan spasi: ")

# Mengubah string input menjadi list angka 
numbers = list(map(float, input_numbers.split()))

# Menghitung total jumlah semua angka
total = sum(numbers)

# Menghitung nilai rata-rata
average = total / len(numbers) if numbers else 0

# Menghilang nilai terbesar dan terkecil 
largest = max(numbers)
smallest = min(numbers)

# Menampilkan hasil
print("daftar nomor:", numbers)
print("Jumlah total:", total)
print("Nilai rata-rata:", average)
print("Nilai terbesar:", largest)
print("Nilai terkecil:", smallest)