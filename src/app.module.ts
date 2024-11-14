import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { OcrController } from './controllers/ocr.controller';
import { BcaFormService } from './services/bca-form.service';
import { PlainOcrService } from './services/plain-ocr.service';
import { KtpFormService } from './services/ktp-form.service';
import { OcrBaseService } from './services/ocr-base.service';

@Module({
  imports: [],
  controllers: [AppController, OcrController],
  providers: [
    AppService,
    OcrBaseService,
    BcaFormService,
    PlainOcrService,
    KtpFormService,
  ],
})
export class AppModule {}
