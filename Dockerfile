FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENV FLASK_APP=app/main.py

# CMD ["python", "main.py"]
CMD ["flask", "run", "--host=0.0.0.0"]
