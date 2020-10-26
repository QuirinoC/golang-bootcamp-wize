FROM python

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP server.py
ENV FLASK_DEBUG 1

COPY server.py server.py

CMD flask run --host=0.0.0.0 --port=8080