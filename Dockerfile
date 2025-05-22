FROM python:3.11-slim

WORKDIR /app

COPY gen.py .

ENTRYPOINT ["python", "gen.py"]