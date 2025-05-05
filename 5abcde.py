# Membuat list kosong sebagai daftar belanja 
daftar_belanja = []

# Meminta pengguna untuk memasukkan 5 item belanja
print("Silahkan masukkan 5 item belanja:")
for i in range(5):
    item = input(f"Masukkan item {i+1}:")
    daftar_belanja.append(item)

# Menampilkan seluruh daftar belanja
print("\nDaftar belanja anda:")
print(daftar_belanja)

# Meminta pengguna untuk menghapus lebih dari satu item yang sudah dibeli
items_yang_dihapus = input("\nMasukkan iitem yang sudah dibeli dan ingin dihapus (pisahkan dengan spasi): ")

# Mengubah input menjadi list berdasarkan spasi dan menghapus item ada dalam daftar
items_yang_dihapus = [item.strip() for item in items_yang_dihapus.split()]

# Menghapus item-item yang sudah dibeli dari daftar belanja
for item in items_yang_dihapus:
    if item in daftar_belanja:
        daftar_belanja.remove(item)
    else:
        print(f"{item} tidak ada dalam daftar belanja anda.")

# Menampilkan daftar belanja yang sudah diperbarui
print("\nDaftar belanja yang diperbarui: ")
print(daftar_belanja)
