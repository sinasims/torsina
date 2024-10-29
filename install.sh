#!/bin/bash

# دانلود فایل torsina.py
wget https://raw.githubusercontent.com/sinasims/torsina/refs/heads/main/torsina.py -O torsina.py

# تغییر دسترسی به فایل autoTOR.py
chmod 777 torsina.py

# ایجاد دایرکتوری
mkdir -p /usr/share/torsina

# کپی کردن فایل به دایرکتوری
cp torsina.py /usr/share/torsina/torsina.py

# ایجاد اسکریپت برای اجرای torsina.py
cmnd='#! /bin/sh \n exec python3 /usr/share/torsina/torsina.py "$@"'
echo -e $cmnd > /usr/bin/torsina

# تغییر دسترسی به اسکریپت
chmod +x /usr/bin/torsina
chmod +x /usr/share/torsina/torsina.py

# اجرای برنامه torsina
torsina

echo "Installation completed successfully."
