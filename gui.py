import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from image_converter import ImageConverter
import os

class ImageToWebPGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("圖片轉WebP工具")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        self.converter = ImageConverter()
        self.selected_files = []
        self.output_directory = ""
        
        self.create_widgets()
    
    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        ttk.Label(main_frame, text="選擇要轉換的圖片檔案:", font=("Arial", 12)).grid(
            row=0, column=0, columnspan=2, sticky=tk.W, pady=(0, 5)
        )
        
        select_frame = ttk.Frame(main_frame)
        select_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        select_frame.columnconfigure(1, weight=1)
        
        ttk.Button(select_frame, text="選擇檔案", command=self.select_files).grid(
            row=0, column=0, padx=(0, 10)
        )
        
        ttk.Button(select_frame, text="選擇輸出資料夾", command=self.select_output_directory).grid(
            row=0, column=1, padx=(0, 10)
        )
        
        ttk.Button(select_frame, text="清除選取", command=self.clear_files).grid(
            row=0, column=2
        )
        
        files_frame = ttk.LabelFrame(main_frame, text="已選擇的檔案", padding="5")
        files_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        files_frame.columnconfigure(0, weight=1)
        files_frame.rowconfigure(0, weight=1)
        
        self.files_listbox = tk.Listbox(files_frame, selectmode=tk.EXTENDED)
        self.files_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        files_scrollbar = ttk.Scrollbar(files_frame, orient=tk.VERTICAL, command=self.files_listbox.yview)
        files_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.files_listbox.configure(yscrollcommand=files_scrollbar.set)
        
        output_frame = ttk.Frame(main_frame)
        output_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        output_frame.columnconfigure(1, weight=1)
        
        ttk.Label(output_frame, text="輸出資料夾:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.output_label = ttk.Label(output_frame, text="未選擇", foreground="gray")
        self.output_label.grid(row=0, column=1, sticky=tk.W)
        
        quality_frame = ttk.Frame(main_frame)
        quality_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ttk.Label(quality_frame, text="品質設定:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        self.quality_var = tk.IntVar(value=90)
        quality_scale = ttk.Scale(quality_frame, from_=10, to=100, variable=self.quality_var, 
                                orient=tk.HORIZONTAL, length=200)
        quality_scale.grid(row=0, column=1, padx=(0, 10))
        self.quality_label = ttk.Label(quality_frame, text="90")
        self.quality_label.grid(row=0, column=2)
        
        quality_scale.configure(command=self.update_quality_label)
        
        self.progress = ttk.Progressbar(main_frame, mode='determinate')
        self.progress.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.status_label = ttk.Label(main_frame, text="準備就緒")
        self.status_label.grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        self.convert_button = ttk.Button(main_frame, text="開始轉換", command=self.start_conversion)
        self.convert_button.grid(row=7, column=0, columnspan=2, pady=10)
    
    def select_files(self):
        filetypes = [
            ("支援的圖片格式", "*.png *.jpg *.jpeg *.bmp *.tiff *.gif"),
            ("PNG", "*.png"),
            ("JPEG", "*.jpg *.jpeg"),
            ("BMP", "*.bmp"),
            ("TIFF", "*.tiff"),
            ("GIF", "*.gif"),
            ("所有檔案", "*.*")
        ]
        
        files = filedialog.askopenfilenames(
            title="選擇要轉換的圖片檔案",
            filetypes=filetypes
        )
        
        if files:
            valid_files = []
            for file in files:
                if self.converter.is_supported_format(file):
                    valid_files.append(file)
                else:
                    messagebox.showwarning("格式警告", f"不支援的檔案格式: {os.path.basename(file)}")
            
            self.selected_files.extend(valid_files)
            self.selected_files = list(set(self.selected_files))
            self.update_files_display()
    
    def select_output_directory(self):
        directory = filedialog.askdirectory(title="選擇輸出資料夾")
        if directory:
            self.output_directory = directory
            self.output_label.config(text=directory, foreground="black")
    
    def clear_files(self):
        self.selected_files = []
        self.update_files_display()
    
    def update_files_display(self):
        self.files_listbox.delete(0, tk.END)
        for file in self.selected_files:
            self.files_listbox.insert(tk.END, os.path.basename(file))
    
    def update_quality_label(self, value):
        self.quality_label.config(text=str(int(float(value))))
    
    def start_conversion(self):
        if not self.selected_files:
            messagebox.showwarning("警告", "請先選擇要轉換的圖片檔案!")
            return
        
        if not self.output_directory:
            messagebox.showwarning("警告", "請先選擇輸出資料夾!")
            return
        
        self.convert_button.config(state='disabled')
        self.progress['maximum'] = len(self.selected_files)
        self.progress['value'] = 0
        
        thread = threading.Thread(target=self.convert_images)
        thread.daemon = True
        thread.start()
    
    def convert_images(self):
        quality = self.quality_var.get()
        success_count = 0
        total_count = len(self.selected_files)
        
        for i, file_path in enumerate(self.selected_files):
            self.root.after(0, lambda: self.status_label.config(
                text=f"正在轉換: {os.path.basename(file_path)}"
            ))
            
            success, message = self.converter.convert_to_webp(file_path, self.output_directory, quality)
            
            if success:
                success_count += 1
            
            self.root.after(0, lambda v=i+1: self.progress.config(value=v))
        
        self.root.after(0, lambda: self.conversion_complete(success_count, total_count))
    
    def conversion_complete(self, success_count, total_count):
        self.convert_button.config(state='normal')
        self.status_label.config(text=f"轉換完成: {success_count}/{total_count} 成功")
        
        if success_count > 0:
            result = messagebox.askyesno(
                "轉換完成", 
                f"成功轉換 {success_count} 個檔案!\n\n是否要開啟輸出資料夾?"
            )
            if result:
                if os.name == 'nt':
                    os.startfile(self.output_directory)
                elif os.name == 'posix':
                    os.system(f'open "{self.output_directory}"')
        else:
            messagebox.showerror("轉換失敗", "沒有檔案成功轉換，請檢查檔案格式或權限!")

def main():
    root = tk.Tk()
    app = ImageToWebPGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()