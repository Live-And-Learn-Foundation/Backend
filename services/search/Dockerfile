FROM python:3.12-slim

WORKDIR /app/search

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:9005", "main:app"]
# RUN python main.py

EXPOSE 9005