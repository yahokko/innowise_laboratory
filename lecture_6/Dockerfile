FROM python:3.13.5
EXPOSE 8000

WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3\
    CMD curl -f http://localhost:8000/healthcheck || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]