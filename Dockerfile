FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "src:create_app()", "--bind", "0.0.0.0:8000", "--workers", "3"]