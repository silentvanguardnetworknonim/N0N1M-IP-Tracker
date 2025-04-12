N0N1M IP Tracker

N0N1M IP Tracker 
adalah tools sederhana untuk melacak informasi geolokasi dari alamat IP atau domain.

 Fitur
- Lacak IP Website
- Lacak IP Publik (otomatis IP kamu)
- Lacak IP Manual
- Tampilan warna-warni dengan banner keren
- Informasi lengkap: kota, negara, ISP, lokasi, timezone, dll

 Cara Install (di Termux)

bash
pkg update && pkg upgrade
pkg install python git
pip install requests colorama
git clone https://github.com/silentvar/N0N1M-IP-Tracker.git
cd N0N1M-IP-Tracker
python N0N1M-IP-Tracker.py
