
# Paste script dari atas
import requests
import os
from colorama import init, Fore, Style

init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.CYAN + Style.BRIGHT + r"""
 _   _  ___   _   _ ___ __  __ ___ 
| \ | |/ _ \ | \ | |_ _|  \/  | _ \
|  \| | | | ||  \| || || |\/| |  _/
|_|\__|_| |_|_| \_|___|_|  |_|_|
    """)
    print(Fore.YELLOW + "="*40)
    print(Fore.GREEN + "        N0N1M IP Tracker Tool")
    print(Fore.YELLOW + "="*40 + "\n")

def track_ip(ip=None):
    if ip is None:
        url = "http://ip-api.com/json/"
    else:
        url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url).json()
    if response["status"] == "success":
        print(Fore.MAGENTA + "\n=== Informasi Geolokasi ===")
        for key, value in response.items():
            print(Fore.CYAN + f"{key.capitalize():<15}: {Fore.WHITE}{value}")
    else:
        print(Fore.RED + "Gagal mendapatkan informasi.")

def menu():
    while True:
        banner()
        print(Fore.BLUE + "1." + Fore.WHITE + " Lacak IP Website")
        print(Fore.BLUE + "2." + Fore.WHITE + " Lacak IP Publik (IP kamu)")
        print(Fore.BLUE + "3." + Fore.WHITE + " Lacak IP Manual")
        print(Fore.BLUE + "4." + Fore.WHITE + " Exit")
        choice = input(Fore.YELLOW + "\nPilih menu (1-4): " + Fore.WHITE)
        if choice == "1":
            domain = input("Masukkan domain (contoh: google.com): ")
            try:
                ip = os.popen(f"ping -c 1 {domain}").read().split(" ")[2].strip("():")
                track_ip(ip)
            except:
                print(Fore.RED + "Gagal mendapatkan IP dari domain.")
        elif choice == "2":
            track_ip()
        elif choice == "3":
            ip = input("Masukkan IP target: ")
            track_ip(ip)
        elif choice == "4":
            print(Fore.GREEN + "\nTerima kasih sudah menggunakan N0N1M Tracker!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid.")
        input(Fore.YELLOW + "\nTekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    menu()
