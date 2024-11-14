import { Injectable } from '@nestjs/common';
import { OcrBaseService } from './ocr-base.service';
import { PlainOcrResult } from '../types/plain-ocr.type';

@Injectable()
export class PlainOcrService extends OcrBaseService {
  async extractText(imagePath: string): Promise<PlainOcrResult> {
    return this.executePythonScript('plain_ocr.py', imagePath);
  }
}
