FROM python:3.8

RUN mkdir code
WORKDIR code

# RUN apk add postgresql-client build-base postgresql-dev

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/

# RUN adduser --disabled-password service-user
#
# USER service-user
