def validasi_nilai(nilai):
    return 0 <= nilai <= 100


def hitung_statistik(data):
    if not data:
        return {
            "rata_rata": 0,
            "minimum": 0,
            "maksimum": 0
        }

    nilai = [mahasiswa["nilai"] for mahasiswa in data]

    return {
        "rata_rata": sum(nilai) / len(nilai),
        "minimum": min(nilai),
        "maksimum": max(nilai)
    }


def tentukan_status(nilai, kkm=60):
    if nilai >= kkm:
        return "Tuntas"
    return "Belum tuntas"


def hitung_ketuntasan(data, kkm=60):
    tuntas = 0
    belum_tuntas = 0

    for mahasiswa in data:
        if tentukan_status(mahasiswa["nilai"], kkm) == "Tuntas":
            tuntas += 1
        else:
            belum_tuntas += 1

    return {
        "tuntas": tuntas,
        "belum_tuntas": belum_tuntas
    }