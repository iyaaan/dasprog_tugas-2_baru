import statistics

# Meminta input dari pengguna (minimal 5 angka)
input_numbers = input("Masukan minimal 5 angka, pisahkan dengan spasi :")

# Mengubah input string menjadi list angka 
numbers = list(map(float, input_numbers.split()))

# Validasi jumlah angka minimal 5 
if len(numbers) < 5 :
    print("Anda harus memasukan minimal 5 angka.")
else:
    # Menghitung statistik
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    median = statistics.median(numbers)

    # Menampilkan list yang sudah diurutkan 
    sorted_numbers = sorted(numbers)

    # Menampilkan hasil
    print("\nStatistik:")
    print("List yang diurutkan:", sorted_numbers)
    print("Nilai minimum:", minimum)
    print("Nilai maksimum:", maximum)
    print("Nilai rata-rata:", average)
    print("Nilai median:", median)
    