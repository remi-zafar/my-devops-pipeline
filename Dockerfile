FROM python:3.9-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod -R 777 /code
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]