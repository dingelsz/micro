FROM python:3

WORKDIR /usr/src/app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ ./src/

CMD ["python", "./src/app.py"]
