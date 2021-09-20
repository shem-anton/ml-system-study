FROM python:3.9.7-slim
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP ml-system-study/api/app.py
EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
