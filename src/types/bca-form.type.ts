export interface BcaFormResult {
  form_type: string;
  form_title: string;
  peserta: {
    nama: string;
    nip: string;
    alamat: string;
    email: string;
    hp: string;
    tanggal_dokumen: string;
  };
  pengunduran_diri: {
    tanggal: string;
    alasan: string;
  };
  rekening: {
    bank: string;
    nomor: string;
    pemilik: string;
  };
  kontak_darurat: {
    nama: string;
    telepon: string;
  };
}
