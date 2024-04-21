FROM python:3.11

RUN set +x \
 && apt update \
 && apt upgrade -y \
 && apt install -y curl gcc build-essential \
 && apt-get install -y firefox-esr


COPY requirements.txt .
RUN pip install -r requirements.txt

COPY /app /app
WORKDIR /app

CMD ["python", "main.py"]
