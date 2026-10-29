def baca_data(path):
    data = []

    with open(path, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 3:
                continue

            nim, nama, nilai = bagian

            try:
                nilai = float(nilai)
            except ValueError:
                continue

            data.append({
                "nim": nim,
                "nama": nama,
                "nilai": nilai
            })

    return data