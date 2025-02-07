FROM python:3.7
ADD . /src
WORKDIR /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt