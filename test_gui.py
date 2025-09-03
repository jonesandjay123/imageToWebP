#!/usr/bin/env python3

import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import ttk

def test_gui():
    root = tk.Tk()
    root.title("測試GUI")
    root.geometry("400x300")
    
    # 添加一些簡單元素
    label = tk.Label(root, text="GUI測試成功！", font=("Arial", 16))
    label.pack(pady=20)
    
    button = tk.Button(root, text="測試按鈕", command=lambda: print("按鈕被點擊"))
    button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    test_gui()