import {
  Controller,
  Post,
  UploadedFile,
  UseInterceptors,
  BadRequestException,
} from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { BcaFormService } from '../services/bca-form.service';
import { diskStorage } from 'multer';
import * as path from 'path';
import { BcaFormResult } from '../types/bca-form.type';
import { PlainOcrResult } from 'src/types/plain-ocr.type';
import { PlainOcrService } from 'src/services/plain-ocr.service';
import { KtpFormService } from 'src/services/ktp-form.service';
import { KtpFormResult } from 'src/types/ktp-form.type';

@Controller('ocr')
export class OcrController {
  constructor(
    private readonly bcaFormService: BcaFormService,
    private readonly plainOcrService: PlainOcrService,
    private readonly ktpFormService: KtpFormService,
  ) {}

  @Post('bca-form')
  @UseInterceptors(
    FileInterceptor('image', {
      storage: diskStorage({
        destination: './uploads',
        filename: (req, file, cb) => {
          // Validate file type
          const allowedTypes = ['.jpg', '.jpeg', '.png', '.pdf'];
          const ext = path.extname(file.originalname).toLowerCase();
          if (!allowedTypes.includes(ext)) {
            return cb(
              new BadRequestException('Only image and PDF files are allowed'),
              null,
            );
          }

          const uniqueName = `${Date.now()}-${Math.round(
            Math.random() * 1e9,
          )}${ext}`;
          cb(null, uniqueName);
        },
      }),
      limits: {
        fileSize: 5 * 1024 * 1024, // 5MB limit
      },
    }),
  )
  async uploadBcaForm(
    @UploadedFile() file: Express.Multer.File,
  ): Promise<BcaFormResult> {
    try {
      return await this.bcaFormService.readBcaForm(file.path);
    } catch (error) {
      throw new BadRequestException(error.message);
    }
  }

  @Post('extract-text')
  @UseInterceptors(
    FileInterceptor('image', {
      storage: diskStorage({
        destination: './uploads',
        filename: (req, file, cb) => {
          const allowedTypes = ['.jpg', '.jpeg', '.png', '.pdf'];
          const ext = path.extname(file.originalname).toLowerCase();
          if (!allowedTypes.includes(ext)) {
            return cb(
              new BadRequestException('Only image and PDF files are allowed'),
              null,
            );
          }

          const uniqueName = `${Date.now()}-${Math.round(
            Math.random() * 1e9,
          )}${ext}`;
          cb(null, uniqueName);
        },
      }),
      limits: {
        fileSize: 5 * 1024 * 1024, // 5MB limit
      },
    }),
  )
  async extractText(
    @UploadedFile() file: Express.Multer.File,
  ): Promise<PlainOcrResult> {
    try {
      return await this.plainOcrService.extractText(file.path);
    } catch (error) {
      throw new BadRequestException(error.message);
    }
  }

  @Post('ktp')
  @UseInterceptors(
    FileInterceptor('image', {
      storage: diskStorage({
        destination: './uploads',
        filename: (req, file, cb) => {
          const allowedTypes = ['.jpg', '.jpeg', '.png'];
          const ext = path.extname(file.originalname).toLowerCase();
          if (!allowedTypes.includes(ext)) {
            return cb(
              new BadRequestException('Only image files are allowed'),
              null,
            );
          }

          const uniqueName = `${Date.now()}-${Math.round(
            Math.random() * 1e9,
          )}${ext}`;
          cb(null, uniqueName);
        },
      }),
      limits: {
        fileSize: 5 * 1024 * 1024, // 5MB limit
      },
    }),
  )
  async extractKtp(
    @UploadedFile() file: Express.Multer.File,
  ): Promise<{ success: boolean; data?: KtpFormResult; error?: string }> {
    try {
      return await this.ktpFormService.readKtp(file.path);
    } catch (error) {
      throw new BadRequestException(error.message);
    }
  }
}
