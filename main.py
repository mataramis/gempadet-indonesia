
import deteksi_gempa

if __name__ == '__main__':
    print("jalankan aplikasi")
    hasil = deteksi_gempa.ekstraksi_data()
    deteksi_gempa.tampilkan_data(hasil)


print("============================ IIIIIIIIIIIIIIIIIIIII =================")

import gempadet

if __name__ == '__main__':
    print("apk gempadet.")
    jadi = gempadet.ekstraksi_data()
    gempadet.tampilkan_data(jadi)