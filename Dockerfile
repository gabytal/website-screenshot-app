FROM debian:10

MAINTAINER Gaby Tal "gabytal333@gmail.com"

COPY . /app

WORKDIR /app

RUN  apt update && apt install python3.7 wget python3-pip firefox-esr -y 

RUN  wget -q https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz \
    && tar -xvf geckodriver-v0.24.0-linux64.tar.gz \
    && mv geckodriver /usr/local/bin/ \
    && rm geckodriver-v0.24.0-linux64.tar.gz 

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3.7", "app.py"]