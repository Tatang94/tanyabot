# Judul untuk bot ChatGPT
# Saya menyimpan teks dan judul di sini untuk menghindari kekacauan dalam kode utama.

# Kami memiliki 4 jenis pesan sambutan
# Dua yang pertama adalah normal dan dua lainnya untuk deep-linking
# Pengguna baru (/start):
welcome_1: str = (
    "Hai {}\n\n"
    "Selamat datang di TanyakanBot!\n"
    "Silahkan Mulai Bertanya ..."
)
# Pengguna sudah memiliki akun (/start):
welcome_2: str = (
    "Selamat datang kembali {}\n"
    "Mari mulai percakapan!"
)
# Pengguna baru (/start=create):
welcome_3: str = (
    "Hai {}\n"
    "Akun Anda telah dibuat! Nikmati."
)
# Pengguna sudah memiliki akun (/start?create):
welcome_4: str = (
    "Hai {}\n"
    "Anda sudah memiliki akun."
)

# Peringatan tanpa akun untuk pengguna yang belum memiliki akun:
no_account_warn: str = (
    "Yth. {}\n\n"
    "Anda perlu memulai bot sebelum menggunakannya! "
    "Kami perlu membuat akun untuk Anda terlebih dahulu:\n\n"
    "t.me/{}?start=create"
)

# Pemberitahuan riwayat dihapus:
history_cleared: str = (
    "Yth. {}\n\n"
    "Riwayat Anda berhasil dihapus."
)

# Dan mode untuk perintah /danmode
# Dan mode diaktifkan:
dan_mode_enabled: str = (
    "DAN mode _versi 10.0!_\n"
    "Status: *Diaktifkan*"
)
# Dan mode dinonaktifkan:
dan_mode_disabled: str = (
    "DAN mode _versi 10.0!_\n"
    "Status: *Dinonaktifkan*\n\n"
    "Catatan: File riwayat juga direset!"
)

# Fitur untuk perintah (/features)
features: str = (
    "*Fitur utama*:\n"
    "1. Memiliki memori jangka panjang\n"
    "2. Mendukung peran dan mode DAN\n"
    "3. Mendukung chat di grup dan privat\n"
    "4. Termasuk opsi regenerasi\n"
    "5. Respon suara\n\n"
    "*Fitur lainnya*:\n"
    "1. MarkdownV2 escaper\n"
    "2. Pengecek dan perbaikan riwayat\n\n"
    "*Fitur yang akan datang*:\n"
    "1. Opsi balasan pintar\n"
    "2. Generator kode\n"
    "3. Generator gambar\n"
    "5. Multi bahasa\n\n"
    "Silakan kirim masalah atau permintaan Anda di sini:\n"
    "https://github.com/Tatang94/tanyabot/issues\n\n"
    "*Perubahan terbaru*:\n"
    "# Menambahkan lebih banyak penyedia.\n"
    "# Menambahkan Remix AI."
)

# Bantuan penggunaan untuk perintah (/chat):
chat_help: str = (
    "Hai {}\n"
    "Silakan ajukan pertanyaan Anda setelah /chat\n\n"
    "*Contoh*: /chat hai"
)

# Penggunaan untuk perintah (/tts):
tts_help: str = (
    "Hai {}\n"
    "Silakan ajukan pertanyaan Anda setelah /tts\n\n"
    "*Contoh*: /tts hai"
)

# Prompt respon:
response_prompt: str = (
    "Menghasilkan respon... Mohon tunggu."
)

# Prompt respon suara:
tts_response_prompt: str = (
    "Menghasilkan respon suara... Mohon tunggu. (Ini bisa memakan waktu hingga satu menit!)"
)

# Kesalahan respon GPT:
response_error: str = (
    "Kesalahan!\n"
    "ChatGPT tidak merespons saat ini!"
)

# Prompt pengaturan
settings_prompt: str = (
    "Penyedia Anda:\n"
    "Anda bisa Aktifkan/Nonaktifkan dengan mengkliknya."
)
