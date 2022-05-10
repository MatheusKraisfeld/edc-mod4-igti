FROM gcr.io/spark-operator/spark-py:v3.0.0
LABEL MAINTAINER Matheus Kraisfeld
LABEL EMAIL matheuskraisfeld@gmail.com.br

USER root:root

RUN mkdir -p /app

#RUN apt-get install -y wget

#RUN wget -q "https://repos.spark-packages.org/graphframes/graphframes/0.8.1-spark3.0-s_2.12/graphframes-0.8.1-spark3.0-s_2.12.jar" -P ./jars/

COPY ./jars/ /opt/spark/jars

WORKDIR /app

USER root