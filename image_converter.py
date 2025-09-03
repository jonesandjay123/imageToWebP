from PIL import Image
import os
from pathlib import Path
from typing import List, Tuple

class ImageConverter:
    SUPPORTED_FORMATS = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif'}
    
    def __init__(self):
        pass
    
    def is_supported_format(self, file_path: str) -> bool:
        return Path(file_path).suffix.lower() in self.SUPPORTED_FORMATS
    
    def convert_to_webp(self, input_path: str, output_dir: str, quality: int = 90) -> Tuple[bool, str]:
        try:
            if not self.is_supported_format(input_path):
                return False, f"不支援的檔案格式: {Path(input_path).suffix}"
            
            with Image.open(input_path) as img:
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGBA')
                else:
                    img = img.convert('RGB')
                
                input_filename = Path(input_path).stem
                output_path = os.path.join(output_dir, f"{input_filename}.webp")
                
                img.save(output_path, 'WEBP', quality=quality, optimize=True)
                
            return True, f"成功轉換: {output_path}"
            
        except Exception as e:
            return False, f"轉換失敗: {str(e)}"
    
    def batch_convert(self, input_files: List[str], output_dir: str, quality: int = 90) -> List[Tuple[str, bool, str]]:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
        
        results = []
        
        for file_path in input_files:
            success, message = self.convert_to_webp(file_path, output_dir, quality)
            results.append((file_path, success, message))
        
        return results