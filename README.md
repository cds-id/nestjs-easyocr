# Easy OCR Nestjs

A NestJS application that uses EasyOCR to extract text from images. Currently supports BCA Form OCR processing.

## Prerequisites

Before you begin, ensure you have installed:

- Node.js (v16 or higher)
- Python (v3.8 or higher)
- pip (Python package manager)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ocr
```

### 2. Install Node.js dependencies

```bash
npm install
```

### 3. Install Python dependencies

```bash
# Install EasyOCR and its dependencies
pip install easyocr pillow numpy

# If you're using Windows and encounter issues, you might need:
pip install torch torchvision torchaudio
```

### 4. Create required directories

```bash
mkdir uploads
```

## Project Structure

```
ocr/
├── src/
│   ├── controllers/
│   │   └── ocr.controller.ts
│   ├── services/
│   │   ├── ocr-base.service.ts
│   │   └── bca-form.service.ts
│   ├── types/
│   │   └── bca-form.type.ts
│   ├── app.module.ts
│   └── main.ts
├── python/
│   └── bca_form_ocr.py
├── uploads/        # Temporary storage for uploaded files
└── README.md
```

## Usage

### 1. Start the server

```bash
# Development mode
npm run start:dev

# Production mode
npm run build
npm run start:prod
```

### 2. API Endpoints

#### Process BCA Form
```http
POST /ocr/bca-form
Content-Type: multipart/form-data

body:
  - image: <file>
```

Example using cURL:
```bash
curl -X POST -F "image=@/path/to/your/image.jpg" http://localhost:3000/ocr/bca-form
```

Response:
```json
{
  "form_type": "DPBCA",
  "form_title": "Formulir Pengunduran Diri Sebagai Peserta Dana Pensiun BCA",
  "peserta": {
    "nama": "Example Name",
    "nip": "12345678",
    "alamat": "Example Address",
    "email": "example@email.com",
    "hp": "081234567890",
    "tanggal_dokumen": "01 Jan 2024"
  },
  "pengunduran_diri": {
    "tanggal": "15 Jan 2024",
    "alasan": ""
  },
  "rekening": {
    "bank": "BCA",
    "nomor": "1234567890",
    "pemilik": "Example Name"
  },
  "kontak_darurat": {
    "nama": "Emergency Contact",
    "telepon": "081234567890"
  }
}
```

## Features

- Image text extraction using EasyOCR
- Support for BCA Form processing
- Automatic file cleanup after processing
- File type validation (jpg, jpeg, png, pdf)
- File size limit (5MB)
- Error handling
- Type-safe responses

## Development

### Add New Form Type

1. Create new type definition in `src/types/`
2. Create new service extending `OcrBaseService`
3. Add new Python script in `python/`
4. Add new endpoint in `OcrController`

### Testing

```bash
# unit tests
npm run test

# e2e tests
npm run test:e2e

# test coverage
npm run test:cov
```

## Error Handling

The API returns error responses in the following format:

```json
{
  "error": "Error message description"
}
```

Common errors:
- File type not supported
- File size exceeds limit
- OCR processing failed
- Invalid or corrupted image

## License

[MIT License](LICENSE)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
```

This README provides:
1. Clear installation instructions
2. Project structure overview
3. Usage examples with API documentation
4. Development guidelines
5. Testing information
6. Error handling details
7. License and contribution guidelines

You can customize it further based on your specific needs or add more sections as the project grows.
