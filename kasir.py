# Program kasir sederhana

print("=== Program Kasir Sederhana ===")

total = 0
while True:
    nama_barang = input("\nNama barang (ketik 'selesai' untuk berhenti): ")
    if nama_barang.lower() == "selesai":
        break
    try:
        harga = float(input("Harga barang: Rp"))
        jumlah = int(input("Jumlah: "))
    except ValueError:
        print("Input salah, coba lagi.")
        continue

    subtotal = harga * jumlah
    total += subtotal
    print(f"Subtotal {nama_barang}: Rp{subtotal}")

print(f"\nTotal belanja: Rp{total}")

# Pembayaran
try:
    bayar = float(input("Uang yang dibayarkan: Rp"))
except ValueError:
    print("Input salah, transaksi dibatalkan.")
    exit()

if bayar >= total:
    kembalian = bayar - total
    print(f"Kembalian: Rp{kembalian}")
else:
    print(f"Uang kurang Rp{total-bayar}")
