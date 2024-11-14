import { Injectable } from '@nestjs/common';
import { OcrBaseService } from './ocr-base.service';
import { BcaFormResult } from '../types/bca-form.type';

@Injectable()
export class BcaFormService extends OcrBaseService {
  async readBcaForm(imagePath: string): Promise<BcaFormResult> {
    return this.executePythonScript('bca_form_ocr.py', imagePath);
  }
}
