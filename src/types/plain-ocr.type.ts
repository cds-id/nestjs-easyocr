export interface Position {
  top_left: [number, number];
  top_right: [number, number];
  bottom_right: [number, number];
  bottom_left: [number, number];
}

export interface ExtractedText {
  text: string;
  confidence: number;
  position: Position;
}

export interface PlainOcrResult {
  success: boolean;
  data?: ExtractedText[];
  error?: string;
}
