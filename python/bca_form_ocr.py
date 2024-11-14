import sys
import easyocr
import json
import logging

logging.getLogger("easyocr.easyocr").setLevel(logging.ERROR)

def clean_and_structure_data(texts):
    data = {
        "form_type": "DPBCA",
        "form_title": "Formulir Pengunduran Diri Sebagai Peserta Dana Pensiun BCA",
        "peserta": {
            "nama": "",
            "nip": "",
            "alamat": "",
            "email": "",
            "hp": "",
            "tanggal_dokumen": ""
        },
        "pengunduran_diri": {
            "tanggal": "",
            "alasan": ""
        },
        "rekening": {
            "bank": "",
            "nomor": "",
            "pemilik": ""
        },
        "kontak_darurat": {
            "nama": "",
            "telepon": ""
        }
    }

    for i, text in enumerate(texts):
        # Clean the text
        text = text.replace('"', '').strip()

        # Fill in the structured data
        if "Nama Peserta" in text and i+1 < len(texts):
            data["peserta"]["nama"] = texts[i+1]
        elif "NIP BCA" in text and i+1 < len(texts):
            data["peserta"]["nip"] = texts[i+1]
        elif "Tanggal Dokumen" in text and i+1 < len(texts):
            data["peserta"]["tanggal_dokumen"] = texts[i+1]
        elif "Alamat Peserta" in text and i+1 < len(texts):
            data["peserta"]["alamat"] = texts[i+1]
        elif "Alamat Email" in text and i+1 < len(texts):
            data["peserta"]["email"] = texts[i+1]
        elif "HP" in text and i+1 < len(texts):
            data["peserta"]["hp"] = texts[i+1]
        elif "mengundurkan diri sebagai karyawan" in text.lower() and i+1 < len(texts):
            data["pengunduran_diri"]["tanggal"] = texts[i+1]
        elif "Nama Bank" in text and i+1 < len(texts):
            data["rekening"]["bank"] = texts[i+1]
        elif "No. Rekening" in text and i+1 < len(texts):
            data["rekening"]["nomor"] = texts[i+1]
        elif "Nama Pemilik Rekening" in text and i+1 < len(texts):
            data["rekening"]["pemilik"] = texts[i+1]
        elif "Pihak yang dapat dihubungi" in text and i+1 < len(texts):
            data["kontak_darurat"]["nama"] = texts[i+1]
        elif "Telepon/HP" in text and i+1 < len(texts):
            data["kontak_darurat"]["telepon"] = texts[i+1]

    return data

def read_image(image_path):
    try:
        reader = easyocr.Reader(['id'], verbose=False, download_enabled=False)
        result = reader.readtext(image_path)
        texts = [item[1] for item in result]

        # Structure the data
        structured_data = clean_and_structure_data(texts)

        # Print single line JSON without indentation
        print(json.dumps(structured_data, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        read_image(image_path)
    else:
        print(json.dumps({"error": "No image path provided"}, ensure_ascii=False))
