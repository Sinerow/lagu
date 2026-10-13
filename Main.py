import subprocess
import sys


def buka_tambah_lagu():
    subprocess.run([sys.executable, "tambah_lagu.py"])


def buka_tampil_lagu():
    subprocess.run([sys.executable, "tampil_lagu.py"])


def menu_utama():
    while True:
        print("\n" + "-" * 40)
        print(" SISTEM DATA LAGU ".center(40, "="))
        print("-" * 40)
        print("1. Tambah Lagu")
        print("2. Tampilkan Lagu")
        print("0. Keluar")
        print("-" * 40)

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            buka_tambah_lagu()

        elif pilihan == "2":
            buka_tampil_lagu()

        elif pilihan == "0":
            print("Terima kasih telah menggunakan program.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu_utama()