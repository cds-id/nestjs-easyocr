import sys
import easyocr
import json
import logging
import numpy as np
import re

logging.getLogger("easyocr.easyocr").setLevel(logging.ERROR)

def clean_text(text):
    return text.strip().replace('"', '').replace(':', '').replace('/', '')

def extract_nik(text):
    # Look for 16-digit NIK
    nik_match = re.search(r'\b\d{16}\b', text)
    return nik_match.group(0) if nik_match else ""

def extract_date(text):
    # Look for date in format DD-MM-YYYY
    date_match = re.search(r'\d{2}-\d{2}-\d{4}', text)
    return date_match.group(0) if date_match else ""

def parse_ktp_data(texts):
    data = {
        "nik": "",
        "nama": "",
        "tempat_lahir": "",
        "tanggal_lahir": "",
        "jenis_kelamin": "",
        "golongan_darah": "",
        "alamat": {
            "jalan": "",
            "rt_rw": "",
            "kelurahan": "",
            "kecamatan": ""
        },
        "agama": "",
        "status_perkawinan": "",
        "pekerjaan": "",
        "kewarganegaraan": "",
        "provinsi": "",
        "kabupaten": ""
    }

    combined_text = " ".join(texts)

    # Extract NIK
    data["nik"] = extract_nik(combined_text)

    for i, text in enumerate(texts):
        text = clean_text(text)

        if "NIK" in text:
            data["nik"] = extract_nik(text)
        elif "Nama" in text and i + 1 < len(texts):
            data["nama"] = clean_text(texts[i + 1])
        elif "Tempat" in text and "Lahir" in text and i + 1 < len(texts):
            # Split birth place and date
            birth_info = texts[i + 1]
            if "," in birth_info:
                place, date = birth_info.split(",", 1)
                data["tempat_lahir"] = clean_text(place)
                data["tanggal_lahir"] = extract_date(date)
        elif "Jenis Kelamin" in text and i + 1 < len(texts):
            data["jenis_kelamin"] = clean_text(texts[i + 1])
        elif "Gol" in text and "Darah" in text and i + 1 < len(texts):
            data["golongan_darah"] = clean_text(texts[i + 1])
        elif "Alamat" in text and i + 1 < len(texts):
            data["alamat"]["jalan"] = clean_text(texts[i + 1])
        elif "RT" in text and "RW" in text and i + 1 < len(texts):
            data["alamat"]["rt_rw"] = clean_text(texts[i + 1])
        elif "Kel" in text and "Desa" in text and i + 1 < len(texts):
            data["alamat"]["kelurahan"] = clean_text(texts[i + 1])
        elif "Kecamatan" in text and i + 1 < len(texts):
            data["alamat"]["kecamatan"] = clean_text(texts[i + 1])
        elif "Agama" in text and i + 1 < len(texts):
            data["agama"] = clean_text(texts[i + 1])
        elif "Status Perkawinan" in text and i + 1 < len(texts):
            data["status_perkawinan"] = clean_text(texts[i + 1])
        elif "Pekerjaan" in text and i + 1 < len(texts):
            data["pekerjaan"] = clean_text(texts[i + 1])
        elif "Kewarganegaraan" in text and i + 1 < len(texts):
            data["kewarganegaraan"] = clean_text(texts[i + 1])
        elif "PROVINSI" in text.upper():
            data["provinsi"] = clean_text(text.replace("PROVINSI", ""))
        elif "KABUPATEN" in text.upper():
            data["kabupaten"] = clean_text(text.replace("KABUPATEN", ""))

    return data

def read_image(image_path):
    try:
        reader = easyocr.Reader(['id'], verbose=False, download_enabled=False)
        result = reader.readtext(image_path)
        texts = [item[1] for item in result]

        # Parse KTP data
        ktp_data = parse_ktp_data(texts)

        print(json.dumps({
            "success": True,
            "data": ktp_data
        }, ensure_ascii=False))

    except Exception as e:
        print(json.dumps({
            "success": False,
            "error": str(e)
        }, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        read_image(image_path)
    else:
        print(json.dumps({
            "success": False,
            "error": "No image path provided"
        }, ensure_ascii=False))
