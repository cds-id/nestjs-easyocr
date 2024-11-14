import { Injectable } from '@nestjs/common';
import { OcrBaseService } from './ocr-base.service';
import { KtpFormResult } from '../types/ktp-form.type';

@Injectable()
export class KtpFormService extends OcrBaseService {
  async readKtp(
    imagePath: string,
  ): Promise<{ success: boolean; data?: KtpFormResult; error?: string }> {
    return this.executePythonScript('ktp_form_ocr.py', imagePath);
  }
}
