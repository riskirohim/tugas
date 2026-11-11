# 1. Gunakan Base Image Python
FROM python:3.10-slim

# 2. Set Working Directory
WORKDIR /app

# 3. Copy file kebutuhan & install modul
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy seluruh kode aplikasi
COPY . .

# 5. Expose Port 5000
EXPOSE 5000

# 6. Jalankan Aplikasi
CMD ["python", "app.py"]
