# syntax=docker/dockerfile:1
#FROM python:3.11
#This Dockerfile contains all the information for creating a 
#Docker container. Not included in this example is the environment.yml 
#file that is needed, specifying all the necessary packages to install 
#to create the needed conda environment.

FROM continuumio/miniconda3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY environment.yml /code/

RUN conda init
RUN conda env create --name postgis_running --file environment.yml 
#RUN conda activate postgis_running

COPY . /code/