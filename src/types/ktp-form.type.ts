export interface KtpFormResult {
  nik: string;
  nama: string;
  tempat_lahir: string;
  tanggal_lahir: string;
  jenis_kelamin: string;
  golongan_darah: string;
  alamat: {
    jalan: string;
    rt_rw: string;
    kelurahan: string;
    kecamatan: string;
  };
  agama: string;
  status_perkawinan: string;
  pekerjaan: string;
  kewarganegaraan: string;
  provinsi: string;
  kabupaten: string;
}
