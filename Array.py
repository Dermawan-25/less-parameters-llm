# NAMA : DERMAWAN
# NIM : D0425319
# SISTEM INFORMASI B

mahasiswa = {
    "nama": "DERMAWAN",
    "nim": "D0425319",
    "jurusan": "Teknik Sistem Informasi",
    "kelas": " B ",
    "angkatan": 2025,
    "alamat": "Sibunoang, Sulawesi Barat",

    "nilai": {
        "algoritma_pemrograman": 95,
        "struktur_data": 80,
        "basis_data": 80,
        "pemrograman_python": 95
    },

    "mata_kuliah_diambil": [
        "Algoritma Pemrograman",
        "Basis Data",
        "Pemrograman Python",
        "Kalkulus Informatika"
    ]
}

# Menampilkan seluruh data
print("\nData Mahasiswa:", mahasiswa)

# Mengakses data
print("Nama:", mahasiswa["nama"])
print("Kelas:", mahasiswa["kelas"])
print("Nilai Python:", mahasiswa["nilai"]["pemrograman_python"])

# Update nilai
mahasiswa["nilai"]["pemrograman_python"] = 95
print("Nilai Python Setelah Update:", mahasiswa["nilai"]["pemrograman_python"])
