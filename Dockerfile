FROM python:3.10

RUN apt update && apt install -y git nano

RUN mkdir /interview
WORKDIR /interview

# INSTALL REQUIREMENTS
RUN pip install -U pip setuptools wheel

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

# COPY PROJECT FILES AND INSTALL APP
COPY . .

CMD while sleep 1000; do :; done
