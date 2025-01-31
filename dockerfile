# Gunakan image Python sebagai base
FROM python:3.9-slim

# Set working directory di dalam container
WORKDIR /app

# Salin requirements.txt ke container
COPY requirements.txt /app/

# Install dependensi dari requirements.txt
RUN pip install -r requirements.txt

# Salin semua file aplikasi ke dalam container
COPY . /app/

# Expose port aplikasi (default Flask port adalah 5000)
EXPOSE 5000

# Perintah untuk menjalankan aplikasi Flask
CMD ["python", "app.py"]
