import { Injectable } from '@nestjs/common';
import { PythonShell } from 'python-shell';
import * as path from 'path';
import * as fs from 'fs';

@Injectable()
export class OcrBaseService {
  protected async executePythonScript(
    scriptName: string,
    imagePath: string,
  ): Promise<any> {
    try {
      const options = {
        scriptPath: path.join(process.cwd(), 'python'),
        args: [imagePath],
      };

      const results = await PythonShell.run(scriptName, options);

      // Clean up the uploaded file
      if (fs.existsSync(imagePath)) {
        fs.unlinkSync(imagePath);
      }
      return JSON.parse(results[0]);
    } catch (error) {
      // Clean up the uploaded file in case of error
      if (fs.existsSync(imagePath)) {
        fs.unlinkSync(imagePath);
      }
      throw error;
    }
  }
}
