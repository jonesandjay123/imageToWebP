#!/usr/bin/env python3

import sys
from gui import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n程式被使用者中斷")
        sys.exit(0)
    except Exception as e:
        print(f"程式執行錯誤: {e}")
        sys.exit(1)