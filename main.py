#!/usr/bin/env python3

import os
import sys

# 消除macOS Tk deprecation警告
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from gui import ImageToWebPGUI

def start_app():
    root = tk.Tk()
    app = ImageToWebPGUI(root)
    root.mainloop()

if __name__ == "__main__":
    try:
        start_app()
    except KeyboardInterrupt:
        print("\n程式被使用者中斷")
        sys.exit(0)
    except Exception as e:
        print(f"程式執行錯誤: {e}")
        sys.exit(1)