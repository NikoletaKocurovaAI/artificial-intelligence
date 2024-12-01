FROM python:3.11-slim

WORKDIR /app

COPY run_app.py /app/
COPY articles/ /app/articles/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "run_app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]