FROM phusion/baseimage
MAINTAINER Tobias Jone <tobiasjone@gmail.com> 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y python \
	python-pip \
	python-lxml \
	python-defusedxml \
	build-essential \
	python-dev \
	python-sklearn \
	python-scipy \
	python-numpy \
    && pip install django==1.9.5 \
	django-tastypie==0.13.3 \
	tornado==4.2.1 \
	cython


COPY hashtag_battles /hashtag_battles 


WORKDIR /hashtag_battles
