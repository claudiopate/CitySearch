FROM python:3.6
RUN apt-get update
WORKDIR /backend
COPY . /backend/
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]
