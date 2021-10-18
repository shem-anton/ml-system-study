FROM python:3.9.7-slim
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5000"]
