import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from image_converter import ImageConverter
import os

class ImageToWebPGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("圖片轉WebP工具")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # 設置窗口居中顯示
        self.center_window()
        
        # 設置窗口圖標（如果有的話）
        try:
            # 這裡可以設置窗口圖標
            pass
        except:
            pass
        
        self.converter = ImageConverter()
        self.selected_files = []
        self.output_directory = ""
        
        self.create_widgets()
    
    def center_window(self):
        """將窗口居中顯示"""
        self.root.update_idletasks()
        width = 700
        height = 600
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def create_widgets(self):
        # 設置主窗口的最小尺寸
        self.root.minsize(600, 500)
        
        # 設置主窗口背景色以支援 dark mode
        self.root.configure(bg='#2b2b2b')
        
        # 使用 Frame 而不是 ttk.Frame 來更好地控制顏色
        main_frame = tk.Frame(self.root, bg='#2b2b2b')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # 標題 - 使用明顯的白色文字
        title_label = tk.Label(main_frame, text="圖片轉WebP工具", 
                              font=("Arial", 18, "bold"),
                              fg='white', bg='#2b2b2b')
        title_label.pack(pady=(0, 20))
        
        # 檔案選擇說明
        file_label = tk.Label(main_frame, text="選擇要轉換的圖片檔案:", 
                             font=("Arial", 12), fg='white', bg='#2b2b2b')
        file_label.pack(anchor=tk.W, pady=(0, 10))
        
        # 按鈕框架
        button_frame = tk.Frame(main_frame, bg='#2b2b2b')
        button_frame.pack(fill=tk.X, pady=(0, 15))
        
        # 使用 tk.Button 來確保在 dark mode 下可見
        select_files_btn = tk.Button(button_frame, text="選擇檔案", command=self.select_files, 
                                   width=15, bg='#4a4a4a', fg='white', 
                                   activebackground='#5a5a5a', activeforeground='white',
                                   relief='raised', bd=2)
        select_files_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        select_output_btn = tk.Button(button_frame, text="選擇輸出資料夾", command=self.select_output_directory, 
                                    width=15, bg='#4a4a4a', fg='white',
                                    activebackground='#5a5a5a', activeforeground='white',
                                    relief='raised', bd=2)
        select_output_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        clear_btn = tk.Button(button_frame, text="清除選取", command=self.clear_files, 
                            width=10, bg='#4a4a4a', fg='white',
                            activebackground='#5a5a5a', activeforeground='white',
                            relief='raised', bd=2)
        clear_btn.pack(side=tk.LEFT)
        
        # 檔案清單框架 - 使用 tk.LabelFrame 來控制顏色
        files_frame = tk.LabelFrame(main_frame, text="已選擇的檔案", 
                                   bg='#2b2b2b', fg='white', 
                                   font=("Arial", 11), bd=2, relief='groove')
        files_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # 使用Frame包裝以便加入滾動條
        listbox_frame = tk.Frame(files_frame, bg='#2b2b2b')
        listbox_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 設置 listbox 的顏色以支援 dark mode
        self.files_listbox = tk.Listbox(listbox_frame, selectmode=tk.EXTENDED, height=10, 
                                       font=("Arial", 10),
                                       bg='#3a3a3a', fg='white',
                                       selectbackground='#5a5a5a', selectforeground='white')
        self.files_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        files_scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.files_listbox.yview,
                                     bg='#4a4a4a', troughcolor='#2b2b2b')
        files_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.files_listbox.configure(yscrollcommand=files_scrollbar.set)
        
        # 輸出資料夾顯示
        output_frame = tk.Frame(main_frame, bg='#2b2b2b')
        output_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(output_frame, text="輸出資料夾:", font=("Arial", 11), 
                fg='white', bg='#2b2b2b').pack(side=tk.LEFT)
        self.output_label = tk.Label(output_frame, text="未選擇", foreground="gray", 
                                   font=("Arial", 10), bg='#2b2b2b')
        self.output_label.pack(side=tk.LEFT, padx=(10, 0))
        
        # 品質設定
        quality_frame = tk.Frame(main_frame, bg='#2b2b2b')
        quality_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(quality_frame, text="品質設定:", font=("Arial", 11), 
                fg='white', bg='#2b2b2b').pack(side=tk.LEFT)
        self.quality_var = tk.IntVar(value=90)
        quality_scale = tk.Scale(quality_frame, from_=10, to=100, variable=self.quality_var, 
                               orient=tk.HORIZONTAL, length=250,
                               bg='#4a4a4a', fg='white', troughcolor='#3a3a3a',
                               activebackground='#5a5a5a', highlightthickness=0)
        quality_scale.pack(side=tk.LEFT, padx=(10, 15))
        self.quality_label = tk.Label(quality_frame, text="90", font=("Arial", 11, "bold"),
                                    fg='white', bg='#2b2b2b')
        self.quality_label.pack(side=tk.LEFT)
        
        quality_scale.configure(command=self.update_quality_label)
        
        # 進度條 - 保持 ttk 樣式但添加背景框架
        progress_frame = tk.Frame(main_frame, bg='#2b2b2b')
        progress_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.progress = ttk.Progressbar(progress_frame, mode='determinate')
        self.progress.pack(fill=tk.X)
        
        # 狀態標籤
        self.status_label = tk.Label(main_frame, text="準備就緒", font=("Arial", 10),
                                   fg='white', bg='#2b2b2b')
        self.status_label.pack(anchor=tk.W, pady=(0, 15))
        
        # 轉換按鈕 - 使用 tk.Button 來確保在 dark mode 下可見
        self.convert_button = tk.Button(main_frame, text="開始轉換", command=self.start_conversion, 
                                      width=20, font=("Arial", 12, "bold"),
                                      bg='#0078d4', fg='white',
                                      activebackground='#106ebe', activeforeground='white',
                                      relief='raised', bd=3, cursor='hand2')
        self.convert_button.pack(pady=15)
        
        # 強制更新GUI顯示
        self.root.update_idletasks()
    
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
            self.output_label.config(text=directory, foreground="white")
    
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