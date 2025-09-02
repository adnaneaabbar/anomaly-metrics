FROM python:3.12.8-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY optimizer ./optimizer
COPY app.py .
COPY .env .

# Create data and output directories (if not mounted)
RUN mkdir -p data output

CMD ["python", "app.py"]