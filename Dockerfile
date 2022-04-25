FROM python:latest

MAINTAINER tarsasov74@gmail.com

RUN mkdir /automation

COPY ./API_testing /automation/API_testing
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install

