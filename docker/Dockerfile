# FROM python:latest
FROM continuumio/anaconda3
RUN apt-get update
RUN apt-get -y install tesseract-ocr
WORKDIR /root/num_padding/docker
ADD ./requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /root/num_padding